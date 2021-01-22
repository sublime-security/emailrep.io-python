import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    "python-dateutil",
    "requests",
    "setuptools",
    "PySocks"
]

setuptools.setup(
    name="emailrep",
    version="0.0.5",
    author="Sublime Security",
    author_email="hi@sublimesecurity.com",
    description="Python interface for the EmailRep API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://emailrep.io",
    download_url="https://github.com/sublime-security/emailrep.io-python",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Developers",
    ],
    entry_points={"console_scripts": ["emailrep = emailrep.cli:main"]},
    keywords=["security", "phishing", "analysts", "soc", "threat intelligence"],
    license="MIT",
)
