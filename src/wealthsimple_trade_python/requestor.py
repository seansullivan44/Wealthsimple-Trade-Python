import requests


class APIRequestor:
    def __init__(self, session, APIMainURL):
        self.session = session
        self.APIMainURL = APIMainURL
        self.session.auth = ("username", "yolo")

    def makeRequest(self, method, endpoint, params=None, returnValue=None):
        URL = self.APIMainURL + endpoint

        if method == "POST":
            return self.post(URL, params)
        elif method == "GET":
            return self.get(URL, params)
        else:
            raise Exception(f"Invalid request method: {method}")

    def post(self, URL, params=None):
        return self.session.post(URL, params)

    def get(self, URL, params=None):
        auth = self.session.headers["Authorization"]
        response = requests.get(URL, headers={"Authorization": auth})
        return response
