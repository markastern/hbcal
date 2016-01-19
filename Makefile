# Makefile for hbcal

# Copyright 2015 Mark Stern
#
# This file is part of Hbcal.
#
# Hbcal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# Hbcal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hbcal.  If not, see <http://www.gnu.org/licenses/>.

INSTALL_DIR = /usr/local/bin
LIB_DIR = /usr/lib/python2.7/site-packages/hbcal

tar:	Makefile ./*.py ./hebrew_calendar/*.py ./tests/*.py \
		./hebrew_calendar/tests/*.py templates/*
	find . -name "*.py" -o -name "Makefile" -o -name "COPYING" \
	-o -name "templates" | tar --transform 's/^\./hbcal/' -czf \
        target/hbcal.tar.gz -T -
        
clean:
		rm target/*

test:
		python -m unittest discover

install:
		pip install enum34
		pip install freezegun
		install -d $(INSTALL_DIR)
		install -d $(LIB_DIR)
		install -D *.py $(LIB_DIR)
		install -d $(LIB_DIR)/hebrew_calendar
		install -D hebrew_calendar/*.py $(LIB_DIR)/hebrew_calendar
		install -d $(LIB_DIR)/templates
		install -D templates/* $(LIB_DIR)/templates
		install -d $(LIB_DIR)/tests
		install -D tests/*.py $(LIB_DIR)/tests
		install -d $(LIB_DIR)/hebrew_calendar/tests
		install -D hebrew_calendar/tests/*.py \
			$(LIB_DIR)/hebrew_calendar/tests
		ln -sf $(LIB_DIR)/hbcal.py $(INSTALL_DIR)/hbcal
