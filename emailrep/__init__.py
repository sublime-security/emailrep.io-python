import sys
import requests

BASE_URL = "https://emailrep.io"

class EmailRep():
    QUERY = "QUERY"
    REPORT = "REPORT"

    def __init__(self, key=None):
        self.base_url = BASE_URL
        self.headers = {}
        self.headers["User-Agent"] = "python/emailrep.io"
        self.headers["Content-Type"] = "application/json"
        if key:
            self.headers["Key"] = key
        self.banner = """
   ____           _ _____
  / __/_ _  ___ _(_) / _ \___ ___
 / _//  ' \/ _ `/ / / , _/ -_) _ \\
/___/_/_/_/\_,_/_/_/_/|_|\__/ .__/
                           /_/
"""


    def query(self, email):
        result = requests.get("%s/%s?summary=true" % (self.base_url, email), headers=self.headers)
        return result.json()

    def report(self, email, tags, description=None, timestamp=None, expires=None):
        base_url = self.base_url + "/report"
        params = {}
        params["email"] = email
        params["tags"] = tags

        if description:
            params["description"] = description

        if timestamp:
            params["timestamp"] = timestamp

        if expires:
            params["expires"] = expires

        result = requests.post(base_url, json=params, headers=self.headers)
        return result.json()

    def format_query_output(self, result):
        print(self.banner)
        print("Email address: %s\n" % result["email"])
        print("\033[91mRISKY\033[0m\n") if result["suspicious"] else None
        print(result["summary"])

