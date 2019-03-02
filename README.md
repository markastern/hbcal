# hbcal
Hebrew date calendar conversion

hbcal is a command line utility to convert dates between the Hebrew calendar and the Civil calendar. It can also optionally display other information about the date e.g. the weekly portion of the Torah, the daily page of Talmud.

## Pre-requisites
* python version 2.7 or 3.4+ (3.3 might also work, but is not tested)
* pip

## Installation

### Easy way - use pip

`pip install hbcal`
### From Repository
Clone the repository:
```
git clone https://github.com/markastern/hbcal
```
To install, run the installation program:

* `python setup.py test` (optional)
* `[sudo] python setup.py install`

## Running
For help type:
`hbcal --help`
## Example
To convert 1st January 2016 to Hebrew calendar and display also the weekly portion of the Torah and the daily page of Talmud:

```
$ hbcal --sedrah --input civil --output hebrew daf -- 1 1 2016
יום שישי 20 טבת 5776
גיטין 19
שמות

## Changes in version 0.8.0
Structure reorganized. Makefile replaced with a python setup script.

## Changes in version 0.9.0
Now compatible with python version 3.4+. Python 3.3 might also work, but is not tested).

## Changes in version 0.9.1
Uses the Python 3 argument-less version of super.

## Changes in version 0.9.2
Fixed setup script so that enum34 is installed only for python < 3.4.

## Changes in version 0.10.0
Month can now be specified as a word instead of a number.

## Changes in version 0.10.1
Fixed html output when displaying time of molad.

By Mark Stern (markalexstern@gmail.com)
