# Haircut

This Python script calculates basic statistics pulled from [my haircut page](https://splorp.com/about/haircut/).

Based on the original [Gist](https://gist.github.com/kylefox/654113) created by [Kyle Fox](https://github.com/kylefox/).

## Sample Output

```
Number of haircuts recorded: 106 (Since October 10, 1998)
Shortest period between haircuts: 9 days (July 21, 2016 to July 30, 2016)
Longest period between haircuts: 120 days (August 11, 2007 to December 09, 2007)
Average period between haircuts: 74 days
Median period between haircuts: 73 days
Your last haircut was 82 days ago. (March 05, 2020)
You probably should’ve had a haircut 8 days ago. (May 18, 2020)
```

## Requirements

+ [Python 2](https://www.python.org/downloads/)
+ [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)

## Change Log

### 20230121
+ Added fix for [failed certificate verification](https://web.archive.org/web/20190428084018/http://blog.pengyifan.com/how-to-fix-python-ssl-certificate_verify_failed/) related to the `urllib2.py` library

### 20220617
+ Updated to [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
+ Added `html.parser` argument to `BeautifulSoup()` constructor

### 20211130
+ Added “User-agent” header to fix `urllib2.HTTPError: HTTP Error 406: Not Acceptable`
+ Standardized variable naming and value quoting because consistency

### 20201010
+ Added calculation of the median period between haircuts

### 20200922
+ Modified output for even more consistent display of days and dates
+ Added newlines before and after output because readability

### 20200714
+ Modified output for haircuts occuring one day ago

### 20200526
+ Modified output for consistent display of days and dates
+ Added more descriptive “next haircut” strings
+ Added logic to display “day zero” status
+ Updated URLs to use https

### 20180327
+ Added note regarding [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) requirement

### 20131109
+ Set UTF-8 encoding

### 20131023
+ Educated the apostrophes
+ Minor edits and formatting tweaks

### 20121114
+ Initial release as a [Gist](https://gist.github.com/kylefox/654113) by [Kyle Fox](https://github.com/kylefox/)
