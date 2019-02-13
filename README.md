# landScraper.py

This tool is designed to take user input for a starting URL and domain, and scrape that URL and any subdirectories that are linked for emails in that domain.

### Instructions

Pretty straightforward, just run this script using python3 and it will ask for input variables or use command line arguments

For the starting URL, don't specify a filename (index.html), but rather the URL directory it's in (http://test.local/). The script currently only supports http: or https:, not both. 

For the domain, if you want all email domains, just leave it blank. The script currently only supports single domains. 

Example command line argument: python3 landScraper.py -u https://domain.local -d domain.local -e @domain.local -o emails.txt

### Future plans/wishlist

As with all github accounts, I plan on adding more features. If I don't get too distracted, these should be fairly easy to implement

-Support for multiple specified email domains (again, should be fairly easy to do)

-Add in threading to speed it up (this will take the longest since it's the thing I have the least experience with)

### Credit

Credit to Michael Shilov from scraping.pro/simple-email-crawler-python for the majority of the code this script is based on. 

### Disclaimer

This has been provided for testing and academic purposes only. Do not use this tool against networks that you do not own or have express/strict written consent to test against. Do not use for illegal purposes.
