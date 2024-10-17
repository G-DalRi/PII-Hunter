<h1 align="center"> PII Hunter </h1>
PII Hunter is a Python-based Burp Suite extension designed to identify Personally Identifiable Information (PII) in HTTP traffic. This tool helps security professionals and penetration testers find sensitive data such as emails, valid CPFs, valid credit card numbers, phone numbers, and dates of birth.

# Features
* Email detection: Scans for common email formats in HTTP responses.
* Valid CPF detection: Uses Brazil’s CPF validation algorithm to find and verify CPF numbers.
* Credit card detection: Identifies and validates credit card numbers using the Luhn algorithm.
* Phone number detection: Finds Brazilian phone numbers in the format (xx) xxxxxxxxx.
* Date of birth detection: Searches for dates in the format dd/mm/yyyy.

# Installation
1. Clone or download the repository.
2. Open Burp Suite and navigate to the Extender tab.
3. In the Extensions section, click Add.
4. Set Extension type to Python.
5. Load the PII_Hunter.py script.
6. The extension will automatically start scanning for PII in HTTP traffic.

# Usage
Once the extension is loaded in Burp Suite, it will automatically scan HTTP responses for sensitive information.

* All matches for PII (emails, CPFs, credit card numbers, phone numbers, and dates) will be displayed in the Burp console.
* The extension works passively, so you don’t need to configure any additional scans.
 
# Limitations
* This extension focuses on Brazilian PII formats (CPF and phone numbers).
* It detects PII within the HTTP response bodies, so if PII is stored or transmitted elsewhere, it won't be detected.
* The phone number detection currently only supports Brazilian phone numbers.

# Contributing
I am new in the community, so, if you’d like to contribute to the project or suggest new features, feel free to open a pull request or issue on GitHub.
