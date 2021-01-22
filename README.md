# Python EmailRep

This is a python 3 library and cli module for interacting with the [EmailRep](https://emailrep.io) service.

## Installation
`pip3 install emailrep --upgrade` or `python3 -m pip install --upgrade emailrep`

## Quick Start (cli)
```sh
# setup your api key (optional)
emailrep setup -k <your api key>

# query an email address
emailrep bill@microsoft.com

# report an email address (key required)
emailrep --report foo@bar.com --tags "bec, maldoc" --description "Phishing email targeting CEO"

```

## Quick Start (python library)
```py
from emailrep import EmailRep

# setup your api key (optional)
emailrep = EmailRep('<your api key>')

# query an email address
emailrep.query("bill@microsoft.com")

# report an email address (key required)
emailrep.report("foo@bar.com", ["bec", "maldoc"], "Phishing email targeting CEO")

```

Full API docs can be found [here](https://docs.emailrep.io).
