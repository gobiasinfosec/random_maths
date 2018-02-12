# Python3
# Credit to Michael Shilov from scraping.pro/simple-email-crawler-python for the majority of this code
#
# As a reminder, web scraping for the purpose of SPAM or hacking is illegal. This tool has been provided for
# legitimate testers to validate the information provided on a website that they have explicit legal right to
# scrape.

import re
from collections import deque
from urllib.parse import urlsplit

import requests.exceptions
from bs4 import BeautifulSoup

# set starting url
starting_url = str(input(r'Put in the full URL of where you want to start crawling (ex: http://test.local/local): '))

# set email domain
email_domain = str(input(r'Put in the email domain you are looking for (ex: @test.local): '))

# set output file
outfile = str(input(r'Path and filename for results output (ex: /home/test/crawled_emails.txt): '))

# a queue of urls to be crawled
new_urls = deque([starting_url])

# a set of urls that we have already crawled
processed_urls = set()

# a set of crawled emails
emails = set()

# process urls one by one until we exhaust the queue
while len(new_urls):

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
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors
        continue

    # extract all email addresses and add them into the resulting set
    new_emails = set(re.findall(r"[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)

    # create a beautiful soup for the html document
    soup = BeautifulSoup(response.text)

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
            # only add urls that are sub urls of the starting url
            if starting_url in link:
                new_urls.append(link)

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
