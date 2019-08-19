import sys
import requests
from dateutil import parser

from emailrep.exceptions import RequestException

base_url = "https://emailrep.io"
class EmailRep():
    QUERY = "QUERY"
    REPORT = "REPORT"

    def __init__(self, key=None):
        self.base_url = base_url
        self.headers = {}
        self.headers["User-Agent"] = "python/emailrep.io"
        self.headers["Content-Type"] = "application/json"
        if key:
            self.headers["Key"] = key
        self.banner = """
 _____                 _ _ ____
| ____|_ __ ___   __ _(_) |  _ \ ___ _ __
|  _| | '_ ` _ \ / _` | | | |_) / _ \ '_ \\
| |___| | | | | | (_| | | |  _ <  __/ |_) |
|_____|_| |_| |_|\__,_|_|_|_| \_\___| .__/
                                    |_|"""

    def query(self, email):
        result = requests.get("%s/%s?summary=true" % (self.base_url, email), headers=self.headers)
        result_json = result.json()
        if result.status_code != 200:
            raise RequestException(result_json["reason"])
        else:
            self.format_query_output(result_json)

    def report(self, email, tags, description=None, ts=None, expires=None):
        base_url = self.base_url + "/report"
        params = {}
        params["email"] = email
        params["tags"] = tags.split(",")

        if description:
            params["description"] = description
        if ts:
            try:
                ts = parser.parse(ts)
            except Exception as e:
                print("invalid timestamp: %s" % str(e))
                sys.exit()
            params["timestamp"] = int(ts.timestamp())
        if expires:
            params["expires"] = expires

        result = requests.post(base_url, json=params, headers=self.headers)
        result_json = result.json()
        if result.status_code == 200:
            if result_json['status'] == 'success':
                print("Successfully reported %s" % email)
            else:
                print(result_json)
        else:
            print(result_json)

    def format_query_output(self, result):
        print(self.banner + "\n\n")
        print("Email address: %s\n" % result["email"])
        print("RISKY\n") if result["suspicious"] else None
        print(result["summary"])

