import requests

BASE_URL = "https://emailrep.io"


class EmailRep():
    QUERY = "QUERY"
    REPORT = "REPORT"

    def __init__(self, key=None, proxy=None):
        self.base_url = BASE_URL
        self.headers = {}
        self.version = "0.0.5"
        self.headers["User-Agent"] = "python/emailrep.io v%s" % self.version
        self.headers["Content-Type"] = "application/json"

        if key:
            self.headers["Key"] = key
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"https": "{}".format(proxy)}

        self.banner = """
   ____           _ _____
  / __/_ _  ___ _(_) / _ \___ ___
 / _//  ' \/ _ `/ / / , _/ -_) _ \\
/___/_/_/_/\_,_/_/_/_/|_|\__/ .__/
                           /_/
"""

    def query(self, email):
        url = "{}/{}?summary=true".format(self.base_url, email)

        result = self.session.get(url, headers=self.headers)
        return result.json()

    def report(self, email, tags, description=None, timestamp=None, expires=None):
        url = self.base_url + "/report"
        params = {}
        params["email"] = email
        params["tags"] = tags

        if description:
            params["description"] = description

        if timestamp:
            params["timestamp"] = timestamp

        if expires:
            params["expires"] = expires

        result = self.session.post(url, json=params, headers=self.headers)
        return result.json()

    def format_query_output(self, result):
        print(self.banner)
        print("Email address: %s\n" % result["email"])
        print("\033[91mRISKY\033[0m\n") if result["suspicious"] else None
        print(result["summary"])
