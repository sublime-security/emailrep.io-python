import os
import sys
import argparse
from argparse import Namespace
from configparser import ConfigParser

from emailrep import EmailRep

CONF_PATH = os.path.expanduser("~/.config/sublime")
CONF_FILE = os.path.join(CONF_PATH, "setup.cfg")
CONF_DEFAULTS = {"emailrep": {"key": ""}}


def parse_args():
    parser = argparse.ArgumentParser(
        prog='emailrep',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
EmailRep - emailrep.io command line interface

Query an email address:
--------------------
emailrep foo@bar.com

Report an email address:
--------------------
emailrep --report foo@bar.com --tags "bec, maldoc" --description "Contact impersonation to CEO"

Setup your API key:
--------------------
emailrep setup -k <your api key>

""")

    # this allows us to parse the email address to query as a positional argument
    parser.add_argument('query', nargs='?')
    parser.add_argument('-r', '--report', help='Email address to report',
                        action='store', dest='report', type=str, required=False)
    parser.add_argument('--tags', help='Tags that should be applied',
                        action='store', dest='tags', type=str, required=False)
    parser.add_argument('--description', help='Additional information and context',
                        action='store', dest='description', type=str, required=False)
    parser.add_argument('--timestamp', help=(
                        'When this activity occurred as a string, defaults to now(). '
                        'Example: "Sun Aug 18 22:51:32 EDT 2019" or "08/18/2019 22:51:32 EDT"'
                        ), action='store', dest='timestamp', type=str, required=False)
    parser.add_argument('--expires', help=(
                        'Number of hours the email should be considered risky'
                        ), action='store', dest='expires', type=int, required=False)
    parser.add_argument('--proxy', help=(
                        'Proxy to use for requests. Example: "socks5://10.10.10.10:8000"'
                        ), action='store', dest='proxy', type=str, required=False),

    args, unknown = parser.parse_known_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()

    elif sys.argv[1] == "setup":
        setup()

    elif not args.report:
        return (EmailRep.QUERY, Namespace(query=sys.argv[1]), args.proxy)

    else:
        if not args.report or not args.tags:
            print("--report and --tags are required for reporting email addresses")
            sys.exit()
        return (EmailRep.REPORT, args, args.proxy)


def setup():
    if len(sys.argv) == 4 and sys.argv[2] == "-k":
        if not os.path.isfile(CONF_FILE):
            if not os.path.exists(CONF_PATH):
                os.makedirs(CONF_PATH)

        config = ConfigParser()
        config["emailrep"] = {}
        config["emailrep"]["key"] = sys.argv[3]
        with open(CONF_FILE, "w") as f:
            config.write(f)
            print("Success! ~/.config/sublime/setup.cfg file generated.")
            sys.exit()
    else:
        print(
            "Setup requires an API key.\n"
            "Usage: emailrep setup -k <api key>"
        )
        sys.exit()


def load_config():
    config = ConfigParser()
    if not os.path.isfile(CONF_FILE):
        config.read_dict(CONF_DEFAULTS)
        return config

    config.read(CONF_FILE)
    return config
