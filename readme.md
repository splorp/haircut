# Haircut

This Python script calculates basic statistics pulled from [my haircut page](https://splorp.com/about/haircut/).

Based on the original [Gist](https://gist.github.com/kylefox/654113) created by [Kyle Fox](https://github.com/kylefox/).

## Sample Output

```
Number of haircuts recorded: 140 (Since October 10, 1998)
Shortest time between haircuts: 9 days (July 21, 2016 to July 30, 2016)
Longest time between haircuts: 138 days (November 28, 2022 to April 15, 2023)
Median time between haircuts: 69.0 days
Average time between haircuts: 68.8 days
Average time between last six haircuts: 50.8 days
Your last haircut was 2 days ago. (December 17, 2024)
You probably should get another haircut in about 48 days. (February 05, 2025)
```

## Requirements

+ [Python 3](https://www.python.org/downloads/)
+ [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)

## Installation

These installation instructions pertain specifically to my primary developer machine, a 2015 MacBook Pro running macOS 10.13.6 High Sierra. They are included here mainly for my own reference.

Your mileage will very likely vary.

**Install MacPorts**

Download the legacy [MacPorts Installer](https://www.macports.org/install.php) applicable to the macOS version you’re using.

In this case, for [High Sierra](https://github.com/macports/macports-base/releases/download/v2.12.5/MacPorts-2.12.5-10.13-HighSierra.pkg).

Run the installer.

**Install Python 3**

In a new Terminal window:

`$ sudo port install python311`

Set this version of Python as the default run by either the `python` or `python3` commands.

`$ sudo port select --set python python311`

`$ sudo port select --set python3 python311`

**Install Beautiful Soup 4**

`$ sudo port install py311-beautifulsoup4`

## Operation

In the Terminal, `cd` to the directory where `haircut.py` resides

`$ python haircut.py`

## Change Log

### 20250825
+ Changed deprecated method `findAll` to `find_all`

### 20241218
+ Ported script to Python 3
+ Replaced `urllib2` library with `urllib.request` library
+ Removed exception handling for malformed dates
+ Median and average times are now formatted with a single decimal place
+ Moved the script for Python 2 to the `/legacy/` directory

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
