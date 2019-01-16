#! python3
# emailScraper.py -v 1.3
# Author- David Sullivan
#
# Credit to Michael Shilov from scraping.pro/simple-email-crawler-python for the majority of this code
#
# As a reminder, web scraping for the purpose of SPAM or hacking is illegal. This tool has been provided for
# legitimate testers to validate the information provided on a website that they have explicit legal right to
# scrape.
#
# Revision  1.0     -   02/12/2018- Initial creation of script
# Revision  1.1     -   04/06/2018- Added in some more error handling
# Revision  1.2     -   04/18/2018- Added in ability to blacklist words in links (to avoid looping), and the ability to
#                                   process sub-domains
# Revision  1.3     -   08/07/2018- Added in functionality to write to output as it runs, in case the script breaks
# Revision  1.4     -   01/16/2019- Added a timeout for stale requests, supression for error messages related to SSL

import re
from collections import deque
from urllib.parse import urlsplit

# disable insecure request warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests.exceptions
from bs4 import BeautifulSoup

# set starting url
starting_url = str(input(r'Put in the full URL of where you want to start crawling (ex: http://test.local/local): '))

# set domain name
domain_name = str(input(r'If you want to include different subdomains, enter the domain name here(ex: To include '
                        r'"my.test.local" as well as "test.local", enter "test.local") If you want to stick to the '
                        r'subdomain of the starting URL, leave this blank: '))

domain_name = starting_url if domain_name == '' else domain_name

# set email domain
email_domain = str(input(r'Put in the email domain you are looking for (ex: @test.local): '))

# set output file
outfile = str(input(r'Path and filename for results output (ex: /home/test/crawled_emails.txt): '))

# a queue of urls to be crawled
new_urls = deque([starting_url])

# a set of urls that we have already crawled
processed_urls = set()

# create an empty list for the emails variable
emails = list()

# don't include links with the following (to avoid loops)
bad_link_words = ['##', '.pdf', '.mp3', '.mp4', '.mpg', '.wav', '.jpg', '.png', '.gif']


# process to handle checking the bad_link_words list
def avoid_loops(links, words):
    return any(word in links for word in words)


# process urls one by one until we exhaust the queue
while len(new_urls):

    # noinspection PyBroadException
    try:
        # move next url from the queue to the set of processed urls
        url = new_urls.popleft()
        processed_urls.add(url)

        # extract base url to resolve relative links
        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        # get url's content
        print("Processing %s" % url)
        try:
            response = requests.get(url, verify=False, timeout=10)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # ignore pages with errors
            continue

        # extract all email addresses
        new_emails = set(re.findall(r"[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+", response.text, re.I))

        # write them to output file
        f = open(outfile, 'a+')
        for email in new_emails:
            f.write(email + '\n')
        f.close()

        # noinspection PyBroadException
        try:
            # create a beautiful soup for the html document
            soup = BeautifulSoup(response.text, "html.parser")

            # find and process all the anchors in the document
            for anchor in soup.find_all("a"):
                # extract link url from the anchor
                link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                # resolve relative links
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                # add the new url to the queue if it was not enqueued nor processed yet
                if not (link in new_urls or link in processed_urls):
                    # only add the new url if not in the bad_link_words list
                    if not avoid_loops(link, bad_link_words):
                        # only add urls that are part of the domain_name
                        if domain_name in link:
                            new_urls.append(link)
        except Exception:
            # if the URL is too long this can error out
            continue

    except Exception:
        # if some error occurs
        continue

# open the output file and import all the crawled emails
f = open(outfile, 'r')
for email in f:
    email = email.replace('\n', '')
    emails.append(email)
f.close()

# remove duplicates from emails
emails = set([email.lower() for email in emails])

# create a list for final_emails
final_emails = list()

# remove emails not in the set domain
for email in emails:
    if email_domain in email:
        final_emails.append(email)

# write output
f = open(outfile, 'w')
for email in final_emails:
    f.write(email + '\n')
f.close()
