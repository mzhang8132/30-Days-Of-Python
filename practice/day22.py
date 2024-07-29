# Day 22: 30 Days of python programming

import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
title = soup.title
if soup:
    title = title.get_text()
else:
    title = "No title"
body = soup.body
if body:
    body = body.get_text().split("\n")
    cleaned = []
    for i in body:
        if i == "" or i == " ":
            continue
        if re.findall("\t", i):
            cleaned.append(i.strip("\t"))
        else:
            cleaned.append(i) 
    body = cleaned 
else:
    body = "No body"
data = {"title": title, "body": body}
with open('day22/bu_facts_stats.json', 'w') as f:
    json.dump(data, f, indent = 4)

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
table = soup.find_all("table")[0].get_text().split("\n")
for i in table:
    if i != "":
        cleaned.append(i)
cleaned = cleaned[99:]
number = []
name = []
term = []
party = []
election = []
vp = []
for i in range(0, len(cleaned), 6):
    number.append(cleaned[i])
    name.append(cleaned[i+1])
    term.append(cleaned[i+2])
    party.append(cleaned[i+3].split("  "))
    election.append(cleaned[i+4].split("  "))
    vp.append(cleaned[i+5].split("  "))
data = {
    "President Number": number,
    "President Name": name,
    "Term": term,
    "Party": party,
    "Election Year(s)": election,
    "Vice President": vp
}
with open('day22/presidents.json', 'w') as f:
    json.dump(data, f, indent = 4)