from emailrep.utils import parse_args, setup, load_config
from emailrep.api import EmailRep
from emailrep.exceptions import RequestException

def main():
    action, args = parse_args()
    config = load_config()

    emailrep = EmailRep(config.get('emailrep', 'key'))
    try:
        if action == EmailRep.QUERY:
            emailrep.query(args.query)
        elif action == EmailRep.REPORT:
            emailrep.report(args.report, args.tags, args.description, args.timestamp, args.expires)

    except RequestException as e:
        print(e)

if __name__ == "__main__":
    main()
