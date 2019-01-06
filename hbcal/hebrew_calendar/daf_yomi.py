"""This file contains classes Tractate and DafYomiCycle."""

# Copyright 2015, 2016, 2019 Mark Stern
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
from enum import Enum

from future.builtins import super

from .abs_time import AbsTime, DAY
from .hebrew_letters import HebrewString
from .date import Month, Year, Date, DateBeforeCreation, BadDate


HEBREW_TRACTATE_NAMES = [
    None,
    u"{BET}{RESH}{KAF}{VAV}{TAV}",
    u"{SHIN}{BET}{TAV}",
    u"{AYIN}{YOD}{RESH}{VAV}{BET}{YOD}{FINAL_NUN}",
    u"{PE}{SAMECH}{CHET}{YOD}{FINAL_MEM}",
    u"{SHIN}{QOF}{LAMED}{YOD}{FINAL_MEM}",
    u"{YOD}{VAV}{MEM}{ALEF}",
    u"{SAMECH}{VAV}{KAF}{HE}",
    u"{BET}{YOD}{TZADE}{HE}",
    u"{RESH}{ALEF}{SHIN} {HE}{SHIN}{NUN}{HE}",
    u"{TAV}{AYIN}{NUN}{YOD}{TAV}",
    u"{MEM}{GIMEL}{YOD}{LAMED}{HE}",
    u"{MEM}{VAV}{AYIN}{DALET} {QOF}{TET}{FINAL_NUN}",
    u"{CHET}{GIMEL}{YOD}{GIMEL}{HE}",
    u"{YOD}{BET}{MEM}{VAV}{TAV}",
    u"{KAF}{TAV}{VAV}{BET}{VAV}{TAV}",
    u"{NUN}{DALET}{RESH}{YOD}{FINAL_MEM}",
    u"{NUN}{ZAYIN}{YOD}{RESH}",
    u"{SAMECH}{VAV}{TET}{HE}",
    u"{GIMEL}{YOD}{TET}{YOD}{FINAL_NUN}",
    u"{QOF}{YOD}{DALET}{VAV}{SHIN}{YOD}{FINAL_NUN}",
    u"{BET}{BET}{ALEF} {QOF}{MEM}{ALEF}",
    u"{BET}{BET}{ALEF} {MEM}{TZADE}{YOD}{AYIN}{ALEF}",
    u"{BET}{BET}{ALEF} {BET}{TAV}{RESH}{ALEF}",
    u"{SAMECH}{NUN}{HE}{DALET}{RESH}{YOD}{FINAL_NUN}",
    u"{MEM}{KAF}{VAV}{TAV}",
    u"{SHIN}{BET}{VAV}{AYIN}{VAV}{TAV}",
    u"{AYIN}{BET}{VAV}{DALET}{HE} {ZAYIN}{RESH}{HE}",
    u"{HE}{VAV}{RESH}{YOD}{VAV}{TAV}",
    u"{ZAYIN}{BET}{CHET}{YOD}{FINAL_MEM}",
    u"{MEM}{NUN}{CHET}{VAV}{TAV}",
    u"{CHET}{VAV}{LAMED}{YOD}{FINAL_NUN}",
    u"{BET}{KAF}{VAV}{RESH}{VAV}{TAV}",
    u"{AYIN}{RESH}{KAF}{YOD}{FINAL_NUN}",
    u"{TAV}{MEM}{VAV}{RESH}{HE}",
    u"{KAF}{RESH}{YOD}{TAV}{VAV}{TAV}",
    u"{MEM}{AYIN}{YOD}{LAMED}{HE}",
    u"{NUN}{DALET}{HE}"]


class Tractate(Month):
    """An enumeration class of tractates of Talmud Bavi"""
    BERACHOS = 1
    SHABBOS = 2
    ERUVIN = 3
    PESACHIM = 4
    SHEKALIM = 5
    YOMA = 6
    SUCCAH = 7
    BEITZAH = 8
    ROSH_HASHANAH = 9
    TAANIS = 10
    MEGILAH = 11
    MOED_KATAN = 12
    CHAGIGAH = 13
    YEVAMOS = 14
    KESUVOS = 15
    NEDARIM = 16
    NAZIR = 17
    SOTAH = 18
    GITIN = 19
    KIDDUSHIN = 20
    BAVA_KAMA = 21
    BAVA_METZIA = 22
    BAVA_BASRA = 23
    SANHEDRIN = 24
    MAKKOS = 25
    SHEVUOS = 26
    AVODA_ZARAH = 27
    HORAYOS = 28
    ZEVACHIM = 29
    MENACHOS = 30
    CHULIN = 31
    BECHOROS = 32
    ERCHIN = 33
    TEMURAH = 34
    KERISUS = 35
    MEILAH = 36
    NIDAH = 37

    def __format__(self, fmt):
        if fmt == "":
            return self.name()
        return HebrewString(HEBREW_TRACTATE_NAMES[self]).__format__(fmt)

    @staticmethod
    def start_year_month():
        return Tractate.BERACHOS

    @staticmethod
    def end_year_month():
        return Tractate.NIDAH


HEBREW_SUBTRACTATE_NAMES = [
    None,
    u"{QOF}{NUN}{YOD}{FINAL_MEM}",
    u"{TAV}{MEM}{YOD}{DALET}",
    u"{MEM}{DALET}{VAV}{TAV}"]


class SubTractate(Enum):
    """An enumeration class of parts of Meilah in the Talmud"""
    KINNIM = 1
    TAMID = 2
    MIDDOS = 3

    def __format__(self, fmt):
        if fmt == "":
            return self.name
        return HebrewString(
            HEBREW_SUBTRACTATE_NAMES[self._value_]).__format__(fmt)


class DateBeforeDafYomi(BadDate):
    """An exception class for dates before the first Daf Yomi cycle."""
    pass


class DafYomiCycle(Year):
    """Subclass of Year for the Daf Yomi calendar.

    A cycle of Daf Yomi is considered equivalent to a year.
    A tractate is considered equivalent to a month.
    A page is considered equivalent to a date."""

    FIRST_YEAR = 1
    START_FIRST_YEAR = AbsTime(296475, 2, 6, 0)
    # For the 8th cycle of Daf Yomi, a different edition of Shekalim was used,
    # with 21 daf instead of 12
    SHEKALIM_ORIGINAL = 12
    SHEKALIM_NOW = 21
    SHEKALIM_CHANGE = 8

    def _shekalim_dapim(self):
        """Return the number of pages in Shekalim."""
        return self.SHEKALIM_ORIGINAL if self.value < self.SHEKALIM_CHANGE \
            else self.SHEKALIM_NOW

    # The number of pages in each tractate. This is not the number of last
    # page (because tractates always start with page 2).
    DAPIM = [None,
             63, 156, 104, 120, _shekalim_dapim, 87, 55, 39, 34, 30, 31, 28,
             26, 121, 111, 90, 65, 48, 89, 81, 118, 118, 175, 112, 23, 48, 75,
             13, 119, 109, 141, 60, 33, 33, 27, 36, 72]

    # Kinnim, Tamid and Middos appear on pages 22 to 37 of Meilah (in the
    # standard Vilna edition).
    MEILAH_PARTS = {22: (Tractate.MEILAH, SubTractate.KINNIM),
                    23: (SubTractate.KINNIM, ),
                    24: (SubTractate.KINNIM, ),
                    25: (SubTractate.KINNIM, SubTractate.TAMID),
                    26: (SubTractate.TAMID, ),
                    27: (SubTractate.TAMID, ),
                    28: (SubTractate.TAMID, ),
                    29: (SubTractate.TAMID, ),
                    30: (SubTractate.TAMID, ),
                    31: (SubTractate.TAMID, ),
                    32: (SubTractate.TAMID, ),
                    33: (SubTractate.TAMID, ),
                    34: (SubTractate.MIDDOS, ),
                    35: (SubTractate.MIDDOS, ),
                    36: (SubTractate.MIDDOS, ),
                    37: (SubTractate.MIDDOS, )}

    CYCLE_DAYS_ORIGINAL = sum(x for x in DAPIM
                              if isinstance(x, int)) + SHEKALIM_ORIGINAL
    CYCLE_DAYS_NOW = CYCLE_DAYS_ORIGINAL + SHEKALIM_NOW - SHEKALIM_ORIGINAL
    START_SHEKALIM_CHANGE_YEAR = START_FIRST_YEAR + \
        (SHEKALIM_CHANGE - FIRST_YEAR) * CYCLE_DAYS_ORIGINAL * DAY

    @Year.value.setter
    def value(self, value):
        difference = value - self._value
        if difference >= 0:
            while self._value < value:
                self._start += self.duration()
                self._value += 1
        else:
            while self._value > value:
                self._value -= 1
                self._start -= self.duration()

    def days_in_month(self, month):
        dapim = self.DAPIM[month]
        if isinstance(dapim, int):
            return dapim
        elif callable(dapim):
            return dapim(self)
        else:
            raise TypeError

    def days_in_year(self):
        return self.CYCLE_DAYS_ORIGINAL if self.value < self.SHEKALIM_CHANGE \
            else self.CYCLE_DAYS_NOW

    def duration(self):
        return self.days_in_year() * DAY

    def months_in_year(self):
        return len(self.DAPIM) - 1

    @classmethod
    def month_class(cls):
        return Tractate

    @staticmethod
    def first_day():
        """Tractates start with daf bet."""
        return 2

    def last_day(self, month):
        return self.days_in_month(month) + self.first_day() - 1

    def adjust_date(self, month, date):
        try:
            return super().adjust_date(month, date)
        except DateBeforeCreation:
            raise DateBeforeDafYomi

    @classmethod
    def current_year(cls, atime):
        if atime < cls.START_FIRST_YEAR:
            raise DateBeforeDafYomi
        else:
            if atime < cls.START_SHEKALIM_CHANGE_YEAR:
                year, remainder = divmod(atime - cls.START_FIRST_YEAR,
                                         cls.CYCLE_DAYS_ORIGINAL * DAY)
                year += cls.FIRST_YEAR
            else:
                year, remainder = divmod(atime -
                                         cls.START_SHEKALIM_CHANGE_YEAR,
                                         cls.CYCLE_DAYS_NOW * DAY)
                year += cls.SHEKALIM_CHANGE
            return(cls(year), remainder)

    @classmethod
    def min_date(cls):
        """Calculate the minimum date for this class.

        We only need to do it once per class."""
        if cls.MIN_DATE is None:
            cls.MIN_DATE = Date(cls, cls.START_FIRST_YEAR)
        return cls.MIN_DATE

    def format_date(self, tractate, page, fmt):
        tractate_name = format(tractate, fmt).replace("_", " ")
        date_fmt = u"{page} {extra}{tractate}" if fmt == "#R" \
            else u"{tractate}{extra} {page}"
        if tractate == Tractate.MEILAH and page in self.MEILAH_PARTS:
            index = -1 if fmt == "#R" else 1
            extra = ''.join((' ',
                             '(' +
                             "/".join([format(x, fmt)
                                       for x in self.MEILAH_PARTS[page]
                                       [::index]]) +
                             ")")[::index])
        else:
            extra = ""
        return date_fmt.format(tractate=tractate_name, page=page, extra=extra)
