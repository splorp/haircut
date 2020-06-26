# coding=utf-8
#
# This script calculates basic statistics from my haircut page.
# See: http://splorp.com/about/haircut/
#
# Requires BeautifulSoup 3
# https://www.crummy.com/software/BeautifulSoup/
#
# Sample output:
#
#    Number of haircuts since December 22, 1998: 53
#    Average days between haircuts: 77
#    Shortest time between haircuts: April 10, 1999 to May 25, 1999 (45 days)
#    Longest time between haircuts: August 11, 2007 to December 09, 2007 (120 days)
#    You’ll probably want a haircut in about 63 days (March 08, 2010)

import datetime
import urllib2
from BeautifulSoup import BeautifulSoup

HAIRCUTS = "http://splorp.com/about/haircut/"
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
    print "Shortest time between haircuts: %s to %s (%d days)" % (mn[0].strftime(STR), mn[1].strftime(STR), (mn[1]-mn[0]).days)
    print "Longest time between haircuts: %s to %s (%d days)" % (mx[0].strftime(STR), mx[1].strftime(STR), (mx[1]-mx[0]).days)
    print "You’ll probably want a haircut in about %s days (%s)" % ((next-datetime.date.today()).days, next.strftime(STR))
    print "Last haircut (%s) was %s days ago." % (last.strftime(STR), (today-last).days)
