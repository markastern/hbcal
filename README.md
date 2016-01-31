# hbcal
Hebrew date calendar conversion

hbcal is a command line utility to convert dates between the Hebrew calendar and the Civil calendar. It can also optionally display other information about the date e.g. the weekly portion of the Torah, the daily page of Talmud.

## pre-requisites
* python version 2.7 (python 3 version coming soon)
* pip

## installation
To install, run the installation program:

* `python setup.py test` (optional)
* `[sudo] python setup.py install`

## running
For help type:

`hbcal --help`

## example
To convert 1st January 2016 to Hebrew calendar and display also the weekly portion of the Torah and the daily page of Talmud:
```
$ hbcal --sedrah --input civil --output hebrew daf -- 1 1 2016
יום שישי 20 טבת 5776
גיטין 19
שמות
```
## changes in version 0.8.0
Structure reorganized. Makefile replaced with a python setup script.

By Mark Stern (markalexstern@gmail.com)
