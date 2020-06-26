# coding=utf-8
#
# A script to calculate some basic stats on Grant Hutchinson’s haircuts.
# See: https://splorp.com/about/haircut/
#
# Requires BeautifulSoup 3
# https://www.crummy.com/software/BeautifulSoup/
#
# Sample output:
#
# Number of haircuts since October 10, 1998: 106
# Average days between haircuts: 74
# Shortest time between haircuts: 9 days (July 21, 2016 to July 30, 2016)
# Longest time between haircuts: 120 days (August 11, 2007 to December 09, 2007)
# Your last haircut was 82 days ago. (March 05, 2020)
# You probably should’ve had a haircut 8 days ago. (May 18, 2020)

import datetime
import urllib2
from BeautifulSoup import BeautifulSoup

HAIRCUTS = "https://splorp.com/about/haircut/"
MONTHS = 'january february march april may june july august september october november december'.split()

def fetch_dates():
  soup = BeautifulSoup(urllib2.urlopen(HAIRCUTS).read())
  return [span.string for span in soup.findAll('span', {"class": "dtstart"})]

def get_dates():
    dates = []
    for d in fetch_dates():
        day, month, year = d.lower().split()
        try:
            date = datetime.date(int(year), int(MONTHS.index(month))+1, int(day))
        except ValueError, e:
            print '*** uh oh: %s' % e
            continue
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
    
if __name__ == '__main__':
    STR = "%B %d, %Y"
    dates = get_dates()
    mn, mx, deltas = get_deltas(dates)
    avg = (sum(deltas) / len(deltas))
    today = datetime.date.today()
    last = dates[-1]
    next = (last + datetime.timedelta(days=avg))
    print "Number of haircuts since %s: %d" % (dates[0].strftime("%B %d, %Y"), len(dates))
    print "Average days between haircuts: %d" % avg
    print "Shortest time between haircuts: %d days (%s to %s)" % ((mn[1]-mn[0]).days, mn[0].strftime(STR), mn[1].strftime(STR))
    print "Longest time between haircuts: %d days (%s to %s)" % ((mx[1]-mx[0]).days, mx[0].strftime(STR), mx[1].strftime(STR))
    if (today-last).days == 0:
    	print "You got your haircut today. Awesome."
    if (today-last).days > 0:
    	print "Your last haircut was %s days ago. (%s)" % ((today-last).days, last.strftime(STR))
    if (next-datetime.date.today()).days <= -1:
    	print "You probably should’ve had a haircut %s days ago. (%s)" % (abs((next-datetime.date.today()).days), next.strftime(STR))
    if (next-datetime.date.today()).days >= 1:
    	print "You probably should get another haircut in about %s days. (%s)" % ((next-datetime.date.today()).days, next.strftime(STR))
