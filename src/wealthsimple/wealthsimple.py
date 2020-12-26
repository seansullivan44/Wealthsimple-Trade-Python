from .requestor import APIRequestor
from requests import Session
import os
import json


class WSTrade:
    """
    Wealthsimple Trade API wrapper

    Attributes
    ----------
    session : session
        A requests Session object to be associated with the class
    APIMainURL : str
        Main URL endpoint for API
    TradeAPI : APIRequester
        APIRequester object to handle API calls

    Methods
    -------
    login(email=None, password=None, two_factor_callback=None)
        Login to Wealthsimple Trade account
    get_accounts()
        Get Wealthsimple Trade accounts
    get_account_ids()
        Get Wealthsimple Trade account ids
    get_account(id)
        Get a Wealthsimple Trade account given an id
    get_account_history(id, time="all")
        Get Wealthsimple Trade account history
    get_activities()
        Get Wealthsimple Trade activities
    get_orders(symbol=None)
        Get Wealthsimple Trade orders 
    get_security(symbol)
        Get information about a security
    get_positions(id)
        Get positions
    get_person()
        Get Wealthsimple Trade person object
    get_me()
        Get Wealthsimple Trade user object
    get_bank_accounts():
        Get list of bank accounts tied to Wealthsimple Trade account
    get_deposits()
        Get list of deposits
    get_forex()
        Get foreign exchange rate
    """

    def __init__(self, email: str, password: str, two_factor_callback: callable = None):
        """
        Parameters
        ----------
        email : str
            Wealthsimple Trade login email
        password : str
            Wealthsimple Trade login password
        two_factor_callback: function
            Callback function that returns user input for 2FA code
        """
        self.session = Session()
        self.APIMAIN = "https://trade-service.wealthsimple.com/"
        self.TradeAPI = APIRequestor(self.session, self.APIMAIN)
        self.login(email, password, two_factor_callback=two_factor_callback)

    def login(
            self,
            email: str = None,
            password: str = None,
            two_factor_callback: callable = None,
    ) -> None:
        """Login to Wealthsimple Trade account

        Parameters
        ----------
        email : str
            Wealthsimple Trade account email
        password : str
            Wealthsimple Trade account password
        two_factor_callback: function
            Callback function that returns user input for 2FA code

        Returns
        -------
        None
        """
        if email and password:

            # Login credentials to pass in request
            data = [
                ("email", email),
                ("password", password),
            ]

            response = self.TradeAPI.makeRequest("POST", "auth/login", data)

            # Check if account requires 2FA
            if "x-wealthsimple-otp" in response.headers:
                if two_factor_callback == None:
                    raise Exception(
                        "This account requires 2FA. A 2FA callback function must be provided"
                    )
                else:
                    # Obtain 2FA code using callback function
                    MFACode = two_factor_callback()
                    # Add the 2FA code to the body of the login request
                    data.append(("otp", MFACode))
                    # Make a second login request using the 2FA code
                    response = self.TradeAPI.makeRequest("POST", "auth/login", data)

            if response.status_code == 401:
                raise Exception("Invalid Login")

            # Update session headers with the API access token
            self.session.headers.update(
                {"Authorization": response.headers["X-Access-Token"]}
            )
        else:
            raise Exception("Missing login credentials")

    def get_accounts(self) -> list:
        """Get Wealthsimple Trade accounts

        Returns
        -------
        list
            A list of Wealthsimple Trade account dictionary objects
        """
        response = self.TradeAPI.makeRequest("GET", "account/list")
        response = response.json()
        response = response["results"]
        return response

    def get_account_ids(self) -> list:
        """Get Wealthsimple Trade account ids

        Returns
        -------
        list
            A list of Wealthsimple Trade account ids
        """
        userAccounts = self.get_accounts()
        accountIDList = []
        for account in userAccounts:
            accountIDList.append(account["id"])
        return accountIDList

    def get_account(self, id: str) -> dict:
        """Get a Wealthsimple Trade account given an id

        Parameters
        ----------
        id : str
            Wealthsimple Trade account id

        Returns
        -------
        dict
            A dictionary containing the Wealthsimple Trade account
        """
        userAccounts = self.get_accounts()
        for account in userAccounts:
            if account["id"] == id:
                return account
        raise NameError(f"{id} does not correspond to any account")

    def get_account_history(self, id: str, time: str = "all") -> dict:
        """Get Wealthsimple Trade account history

        Parameters
        ----------
        id : str
            Wealthsimple Trade account id
        time : str
            String containing time interval for history

        Returns
        -------
        dict
            A dictionary containing the historical Trade account data
        """
        response = self.TradeAPI.makeRequest(
            "GET", f"account/history/{time}?account_id={id}"
        )
        response = response.json()
        if "error" in response:
            if response["error"] == "Record not found":
                raise NameError(f"{id} does not correspond to any account")

        return response

    def get_activities(self) -> list:
        """Get Wealthsimple Trade activities

        Returns
        -------
        list
            A list of dictionaries containing Wealthsimple Trade activities
        """
        response = self.TradeAPI.makeRequest("GET", "account/activities")
        response = response.json()
        return response["results"]

    def get_orders(self, symbol: str = None) -> list:
        """Get Wealthsimple Trade orders

        Parameters
        ----------
        symbol : str
            Symbol for security to filter orders on

        Returns
        -------
        list
            A list containing Wealthsimple Trade order dictionaries
        """
        response = self.TradeAPI.makeRequest("GET", "orders")
        response = response.json()
        # Check if order must be filtered:
        if symbol:
            filteredOrders = []
            for order in response["results"]:
                if order["symbol"] == symbol:
                    filteredOrders.append(order)
            return filteredOrders
        else:
            return response

    def get_security(self, id: str) -> dict:
        """Get information about a security

        Parameters
        ----------
        id : str
            Wealthsimple Security ID to search on

        Returns
        -------
        dict
            Dictionary containing information for security
        """

        response = self.TradeAPI.makeRequest("GET", f"securities/{id}")
        response = response.json()
        return response

    def get_securities_from_ticker(self, symbol: str) -> list:
        """Get information about a securities with matching ticker symbols

        Parameters
        ----------
        symbol : str
            Symbol for security to search on

        Returns
        -------
        list
            A list containing matching securities
        """
        response = self.TradeAPI.makeRequest("GET", f"securities?query={symbol}")
        response = response.json()
        return response["results"]

    def get_positions(self, id: str) -> list:
        """Get positions

        Parameters
        ----------
        id : str
            Wealthsimple Trade account id

        Returns
        -------
        list
            A list containing positions
        """
        response = self.TradeAPI.makeRequest(
            "GET", f"account/positions?account_id={id}"
        )
        response = response.json()
        return response["results"]

    def get_person(self) -> dict:
        """Get Wealthsimple Trade person object

        Returns
        -------
        dict
            A dictionary containing a person object
        """
        response = self.TradeAPI.makeRequest("GET", "person")
        return response.json()

    def get_me(self) -> dict:
        """Get Wealthsimple Trade user object

        Returns
        -------
        dict
            A dictionary containing a user object
        """
        response = self.TradeAPI.makeRequest("GET", "me")
        return response.json()

    def get_bank_accounts(self) -> list:
        """Get list of bank accounts tied to Wealthsimple Trade account

        Returns
        -------
        list
            A list of dictionaries containing bank account objects
        """
        response = self.TradeAPI.makeRequest("GET", "bank-accounts")
        response = response.json()
        return response["results"]

    def get_deposits(self) -> list:
        """Get list of deposits

        Returns
        -------
        list
            A list of dictionaries containing deposit objects
        """
        response = self.TradeAPI.makeRequest("GET", "deposits")
        response = response.json()
        return response["results"]

    def get_forex(self) -> dict:
        """Get foreign exchange rate

        Returns
        -------
        dict
            A dictionary containing foreign exchange rates
        """
        response = self.TradeAPI.makeRequest("GET", "forex")
        return response.json()

    def get_security_id_from_stock_symbol(self, stock_symbol: str) -> str:
        """Get Wealthsimple Security ID of a specific stock symbol (ticker)

        Parameters
        ----------
        stock_symbol : str
            Security symbol to search for

        Returns
        -------
        str
            A str containing Wealthsimple Security ID for the stock
        """
        response = self.TradeAPI.makeRequest("GET", f"securities?query={stock_symbol}")
        response = response.json()
        if response['total_count'] == 1:
            # This check ensure we have an exact match for our search
            return response["results"][0]['id']
        else:
            return ''

    def place_order(self, order: dict) -> dict:

        """Posts an order (market) to Wealthsimple API

        Parameters
        ----------
        :param order:
            The order dict containing the data to be submitted

        Returns
        -------
        dict
            A dict representing the  submitted order
        """

        response = self.TradeAPI.makeRequest("POST", "orders", order)
        response = response.json()
        return response["results"]

    def market_buy(self, account_id, security_id, quantity):

        """Places a market buy order for to the Wealthsimple API under the specified account id
                Parameters
        ----------
        :param quantity: int
            The The number of securities to Buy
        :param security_id:
            The Wealthsimple Security ID
        :param account_id : str
            The Wealthsimple Account id

        Returns
        -------
        dict
            A dict representing the returned order

        """

        quote = self.get_security(security_id)['quote']['amount']
        if quote:
            order = {
                "account_id": account_id,
                "security_id": security_id,
                "limit_price": quote,
                "quantity": quantity,
                "order_type": "buy_quantity",
                "order_sub_type": "market",
                "time_in_force": "day",
            }
            return self.place_order(order)
        raise RuntimeError('Failed to get quote amount when submitting market buy order')

    def market_sell(self, account_id, security_id, quantity):

        """Places a market sell order for to the Wealthsimple API under the specified account id
                Parameters
        ----------
        :param quantity: int
            The The number of securities to Buy
        :param security_id:
            The Wealthsimple Security ID
        :param account_id : str
            The Wealthsimple Account id

        Returns
        -------
        dict
            A dict representing the returned order

        """
        quote = self.get_security(security_id)['quote']['amount']
        if quote:
            order = {
                "account_id": account_id,
                "security_id": security_id,
                "quantity": quantity,
                "limit_price": quote,
                "order_type": "sell_quantity",
                "order_sub_type": "market",
                "time_in_force": "day",
            }
            return self.place_order(order)
        raise RuntimeError('Failed to get quote amount when submitting market sell order')

    def limit_buy(self, account_id, security_id, quantity, limit_price) -> dict:

        """ Places a limit buy order for the Wealthsimple API with the specified account_id and security_id
                Parameters
        ----------
        :param account_id:
        :param security_id:
        :param quantity:
        :param limit_price:

        Returns
        ----------
        dict
            A dict representing the order returned from the API
        """

        order = {
            "account_id": account_id,
            "security_id": security_id,
            "quantity": quantity,
            "limit_price": limit_price,
            "order_type": "buy_quantity",
            "order_sub_type": "limit",
            "time_in_force": "day",
        }

        return self.place_order(order)

    def limit_sell(self, account_id, security_id, quantity, limit_price) -> dict:

        """ Places a limit sell order for the Wealthsimple API with the specified parameters
                Parameters
        ----------
        :param account_id:
        :param security_id:
        :param quantity:
        :param limit_price:

        Returns
        ----------
        dict
            A dict representing the order returned from the API
        """

        order = {
            "account_id": account_id,
            "security_id": security_id,
            "quantity": quantity,
            "limit_price": limit_price,
            "order_type": "sell_quantity",
            "order_sub_type": "limit",
            "time_in_force": "day",
        }
        return self.place_order(order)
