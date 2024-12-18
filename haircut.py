# coding=utf-8
#
# A script to calculate some basic stats on Grant Hutchinson’s haircuts.
# See: https://splorp.com/about/haircut/
#
# Requires Beautiful Soup 4
# https://www.crummy.com/software/BeautifulSoup/
#
# Sample output:
#
# Number of haircuts recorded: 139 (Since October 10, 1998)
# Shortest time between haircuts: 9 days (July 21, 2016 to July 30, 2016)
# Longest time between haircuts: 138 days (November 28, 2022 to April 15, 2023)
# Median time between haircuts: 69 days
# Average time between haircuts: 69 days
# Average time between last six haircuts: 48 days
# Your last haircut was 2 days ago. (November 09, 2024)
# You probably should get another haircut in about 46 days. (December 27, 2024)

import datetime
import urllib.request
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup

calendar = 'january february march april may june july august september october november december'.split()

url = 'https://splorp.com/about/haircut'
hdr = { 'User-agent' : 'Mozilla 5.10' }

page = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(page)

def fetch_dates():
	soup = BeautifulSoup(response, 'html.parser')
	return [span.string for span in soup.findAll('span', {'class': 'dtstart'})]

def get_dates():
	dates = []
	for d in fetch_dates():
		day, month, year = d.lower().split()
		date = datetime.date(int(year), int(calendar.index(month))+1, int(day))
		dates.append(date)
	dates.sort()
	return dates

def get_deltas(dates):
	deltas = []
	mx = None
	mx_delta = None
	mn = None
	mn_delta = None
	for idx in range(0, len(dates)):
		if idx > 0:
			days = (dates[idx] - dates[idx-1]).days
			if mx_delta is None or mx_delta < days:
				mx_delta = days
				mx = (dates[idx-1], dates[idx])
			if mn_delta is None or mn_delta > days:
				mn_delta = days
				mn = (dates[idx-1], dates[idx])
			deltas.append(days)
	return mn, mx, deltas

def median(data):
    quotient, remainder = divmod(len(data), 2)
    if remainder:
        return sorted(data)[quotient]
    return sum(sorted(data)[quotient - 1:quotient + 1]) / 2.

if __name__ == '__main__':
	str = '%B %d, %Y'
	dates = get_dates()
	mn, mx, deltas = get_deltas(dates)
	mdn = median(deltas)
	avg = (sum(deltas) / len(deltas))
	avgm = (sum(deltas[-6:]) / 6)
	today = datetime.date.today()
	last = dates[-1]
	next = (last + datetime.timedelta(days=avgm))
	print("")
	print(f"Number of haircuts recorded: {len(dates)} (Since {dates[0].strftime('%B %d, %Y')})")
	print(f"Shortest time between haircuts: {(mn[1]-mn[0]).days} days ({mn[0].strftime(str)} to {mn[1].strftime(str)})")
	print(f"Longest time between haircuts: {(mx[1]-mx[0]).days} days ({mx[0].strftime(str)} to {mx[1].strftime(str)})")
	print(f"Median time between haircuts: {mdn:.1f} days")
	print(f"Average time between haircuts: {avg:.1f} days")
	print(f"Average time between last six haircuts: {avgm:.1f} days")
	if (today-last).days == 0:
		print("You got your haircut today. Awesome.")
	if (today-last).days == 1:
		print("Your last haircut was yesterday.")
	if (today-last).days > 1:
		print(f"Your last haircut was {(today-last).days} days ago. ({last.strftime(str)})")
	if (next-datetime.date.today()).days <= -1:
		print(f"You probably should’ve had a haircut {abs((next-datetime.date.today()).days)} days ago. ({next.strftime(str)})")
	if (next-datetime.date.today()).days >= 1:
		print(f"You probably should get another haircut in about {abs((next-datetime.date.today()).days)} days. ({next.strftime(str)})")
	print("")
