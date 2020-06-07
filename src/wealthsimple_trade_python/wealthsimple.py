import requests
from requestor import APIRequestor
from requests import Session
import os
import json


class WSTrade:
    def __init__(self, email, password):
        self.session = requests.Session()
        self.APIMAIN = "https://trade-service.wealthsimple.com/"
        self.TradeAPI = APIRequestor(self.session, self.APIMAIN)
        self.login(email, password)

    def login(self, email=None, password=None, two_factor_callback=None):
        """Login to Wealthsimple Trade account

        Parameters
        ----------
        email : str
            Wealthsimple Trade account email
        password : str
            Wealthsimple Trade account password

        Returns
        -------
        None
        """
        if email and password:
            data = [
                ("email", email),
                ("password", password),
            ]
            try:
                response = self.TradeAPI.makeRequest("POST", "auth/login", data)
            except Exception as err:
                print(err)
            print(response)
            print(response.headers)
            print(response.content)
            print("ACCESS TOKEN:")
            print(response.headers["X-Access-Token"])
            self.session.headers.update(
                {"Authorization": response.headers["X-Access-Token"]}
            )
            print(self.session.headers)
        else:
            raise Exception("Missing login credentials")

    def get_accounts(self):
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

    def get_account_ids(self):
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
        print(accountIDList)
        return accountIDList

    def get_account(self, id):
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

    def get_account_history(self, id, time="all"):
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

    def get_activities(self):
        """Get Wealthsimple Trade activities

        Returns
        -------
        list
            A list of dictionaries containing Wealthsimple Trade activities
        """
        response = self.TradeAPI.makeRequest("GET", "account/activities")
        response = response.json()
        return response["results"]

    def get_orders(self, symbol=None):
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

    def get_security(self, symbol):
        """Get information about a security

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

    def get_positions(self, id):
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

    def get_person(self):
        """Get Wealthsimple Trade person object

        Returns
        -------
        dict
            A dictionary containing a person object
        """
        response = self.TradeAPI.makeRequest("GET", "person")
        return response.json()

    def get_me(self):
        """Get Wealthsimple Trade user object

        Returns
        -------
        dict
            A dictionary containing a user object
        """
        response = self.TradeAPI.makeRequest("GET", "me")
        return response.json()

    def get_bank_accounts(self):
        """Get list of bank accounts tied to Wealthsimple Trade account

        Returns
        -------
        list
            A list of dictionaries containing bank account objects
        """
        response = self.TradeAPI.makeRequest("GET", "bank-accounts")
        response = response.json()
        return response["results"]

    def get_deposits(self):
        """Get list of deposits

        Returns
        -------
        list
            A list of dictionaries containing deposit objects
        """
        response = self.TradeAPI.makeRequest("GET", "deposits")
        response = response.json()
        return response["results"]

    def get_forex(self):
        """Get foreign exchange rate

        Returns
        -------
        dict
            A dictionary containing foreign exchange rates
        """
        response = self.TradeAPI.makeRequest("GET", "forex")
        return response.json()


WS = WSTrade(os.environ["WSUSER"], os.environ["WSP"])
print("\n\n\n\n")
id = WS.get_account_ids()
# account = WS.get_account(id[2])
# history = WS.get_account_history(time="1y", id="lol")
# me = WS.get_positions(id[2])
me = WS.get_positions(id=id[2])
print(me)
# print(me["results"])
"""
for x in me:
    print(x)
    print("\n")
"""
