# Haircut

This Python script calculates basic statistics pulled from [my haircut page](https://splorp.com/about/haircut/).

Based on the original [Gist](https://gist.github.com/kylefox/654113) created by [Kyle Fox](https://github.com/kylefox/).

## Sample Output

```
Number of haircuts recorded: 139 (Since October 10, 1998)
Shortest time between haircuts: 9 days (July 21, 2016 to July 30, 2016)
Longest time between haircuts: 138 days (November 28, 2022 to April 15, 2023)
Median time between haircuts: 69 days
Average time between haircuts: 69 days
Average time between last six haircuts: 48 days
Your last haircut was 2 days ago. (November 09, 2024)
You probably should get another haircut in about 46 days. (December 27, 2024)
```

## Requirements

+ [Python 2](https://www.python.org/downloads/)
+ [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)

## Change Log

### 20241111
+ Added calculation of the average time between the previous six haircuts
+ The next haircut date is now based on the previous six haircut average
+ Changed terminology from “period” to “time” in the output

### 20230121
+ Added fix for [failed certificate verification](https://web.archive.org/web/20190428084018/http://blog.pengyifan.com/how-to-fix-python-ssl-certificate_verify_failed/) related to the `urllib2.py` library

### 20220617
+ Updated to [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
+ Added `html.parser` argument to `BeautifulSoup()` constructor

### 20211130
+ Added “User-agent” header to fix `urllib2.HTTPError: HTTP Error 406: Not Acceptable`
+ Standardized variable naming and value quoting because consistency

### 20201010
+ Added calculation of the median time between haircuts

### 20200922
+ Modified output for even more consistent display of days and dates
+ Added newlines before and after output because readability

### 20200714
+ Modified output for haircuts occurring one day ago

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
