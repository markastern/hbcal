"""This file contains classes HebrewMonth and HebrewYear."""

# Copyright 2015, 2019 Mark Stern
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

#  We start counting the months from Nissan (Exodus 12:2). This may
#  be a little confusing, since the year changes in Tishri. In other
#  words, the 1st day of the 7th month (Tishri) 5763 occurs before
#  the 1st day of the 1st month (Nissan) 5763. An advantage of this
#  approach is that, with the exception of Purim (an easy workaround),
#  festivals have a fixed date. If we were to count the months from
#  Tishri, Pesach would sometimes occur in the 7th month (Nissan) and
#  sometimes in the 8th month (Nissan in a leap year).
from __future__ import division
from enum import IntEnum

from future.builtins import range

from . import abs_time
from .abs_time import DAY
from .weekday import DAYS_IN_WEEK, Weekday
from .hebrew_letters import HebrewString
from .date import MonthNotInRange, DateNotInRange, Month, RegularYear

HEBREW_MONTH_NAMES = [
    None,
    u"{NUN}{YOD}{SAMECH}{FINAL_NUN}",
    u"{ALEF}{YOD}{YOD}{RESH}",
    u"{SAMECH}{YOD}{VAV}{FINAL_NUN}",
    u"{TAV}{MEM}{VAV}{ZAYIN}",
    u"{ALEF}{BET}",
    u"{ALEF}{LAMED}{VAV}{LAMED}",
    u"{TAV}{SHIN}{RESH}{YOD}",
    u"{CHET}{SHIN}{VAV}{FINAL_NUN}",
    u"{KAF}{SAMECH}{LAMED}{VAV}",
    u"{TET}{BET}{TAV}",
    u"{SHIN}{BET}{TET}",
    u"{ALEF}{DALET}{RESH} {ALEF}{GERESH}",
    u"{ALEF}{DALET}{RESH} {BET}{GERESH}"]


class HebrewMonth(Month):
    """An enumeration class for Hebrew months"""
    NISSAN = 1
    IYAR = 2
    SIVAN = 3
    TAMMUZ = 4
    AV = 5  # pylint: disable=invalid-name
    ELLUL = 6
    TISHRI = 7
    CHESHVAN = 8
    KISLEV = 9
    TEVETH = 10
    SHEVAT = 11
    ADAR_RISHON = 12
    ADAR_SHENI = 13

    def __format__(self, fmt):
        if fmt == "":
            return self.name()
        return HebrewString(HEBREW_MONTH_NAMES[self]).__format__(fmt)

    @staticmethod
    def start_year_month():
        return HebrewMonth.TISHRI

    @staticmethod
    def end_year_month():
        return HebrewMonth.ELLUL


HEBREW_SEDRAH_NAMES = [
    None,
    u"{BET}{RESH}{ALEF}{SHIN}{YOD}{TAV}",
    u"{NUN}{CHET}",
    u"{LAMED}{FINAL_KAF} {LAMED}{FINAL_KAF}",
    u"{VAV}{YOD}{RESH}{ALEF}",
    u"{CHET}{YOD}{YOD} {SHIN}{RESH}{HE}",
    u"{TAV}{VAV}{LAMED}{DALET}{TAV}",
    u"{VAV}{YOD}{TZADE}{ALEF}",
    u"{VAV}{YOD}{SHIN}{LAMED}{CHET}",
    u"{VAV}{YOD}{SHIN}{BET}",
    u"{MEM}{QOF}{FINAL_TZADE}",
    u"{VAV}{YOD}{GIMEL}{SHIN}",
    u"{VAV}{YOD}{CHET}{YOD}",
    u"{SHIN}{MEM}{VAV}{TAV}",
    u"{VAV}{ALEF}{RESH}{ALEF}",
    u"{BET}{ALEF}",
    u"{BET}{SHIN}{LAMED}{CHET}",
    u"{YOD}{TAV}{RESH}{VAV}",
    u"{MEM}{SHIN}{PE}{TET}{YOD}{FINAL_MEM}",
    u"{TAV}{RESH}{VAV}{MEM}{HE}",
    u"{TAV}{TZADE}{VAV}{HE}",
    u"{KAF}{YOD} {TAV}{SHIN}{ALEF}",
    u"{VAV}{YOD}{QOF}{HE}{LAMED}",
    u"{PE}{QOF}{VAV}{DALET}{YOD}",
    u"{VAV}{YOD}{QOF}{RESH}{ALEF}",
    u"{TZADE}{VAV}",
    u"{SHIN}{MEM}{YOD}{NUN}{YOD}",
    u"{TAV}{ZAYIN}{RESH}{YOD}{AYIN}",
    u"{MEM}{TZADE}{RESH}{AYIN}",
    u"{ALEF}{CHET}{RESH}{YOD} {MEM}{VAV}{TAV}",
    u"{QOF}{DALET}{SHIN}{YOD}{FINAL_MEM}",
    u"{ALEF}{MEM}{RESH}",
    u"{BET}{HE}{RESH}",
    u"{BET}{CHET}{QOF}{TAV}{YOD}",
    u"{BET}{MEM}{DALET}{BET}{RESH}",
    u"{NUN}{SHIN}{ALEF}",
    u"{BET}{HE}{AYIN}{LAMED}{TAV}{FINAL_KAF}",
    u"{SHIN}{LAMED}{CHET} {LAMED}{FINAL_KAF}",
    u"{QOF}{RESH}{CHET}",
    u"{CHET}{QOF}{TAV}",
    u"{BET}{LAMED}{QOF}",
    u"{PE}{YOD}{NUN}{CHET}{SAMECH}",
    u"{MEM}{TET}{VAV}{TAV}",
    u"{MEM}{SAMECH}{AYIN}{YOD}",
    u"{DALET}{BET}{RESH}{YOD}{FINAL_MEM}",
    u"{VAV}{ALEF}{TAV}{CHET}{NUN}{FINAL_NUN}",
    u"{AYIN}{QOF}{BET}",
    u"{RESH}{ALEF}{HE}",
    u"{SHIN}{PE}{TET}{YOD}{FINAL_MEM}",
    u"{KAF}{YOD} {TAV}{TZADE}{ALEF}",
    u"{KAF}{YOD} {TAV}{BET}{VAV}{ALEF}",
    u"{NUN}{TZADE}{BET}{YOD}{FINAL_MEM}",
    u"{VAV}{YOD}{LAMED}{FINAL_KAF}",
    u"{HE}{ALEF}{ZAYIN}{YOD}{NUN}{VAV}",
    u"{VAV}{ZAYIN}{ALEF}{TAV} {HE}{BET}{RESH}{KAF}{HE}",
    u"{VAV}{YOD}{QOF}{HE}{LAMED} - {PE}{QOF}{VAV}{DALET}{YOD}",
    u"{TAV}{ZAYIN}{RESH}{YOD}{AYIN} - {MEM}{TZADE}{RESH}{AYIN}",
    u"{ALEF}{CHET}{RESH}{YOD} - {QOF}{DALET}{SHIN}{YOD}{FINAL_MEM}",
    u"{BET}{HE}{RESH} - {BET}{CHET}{QOF}{TAV}{YOD}",
    u"{CHET}{QOF}{TAV} - {BET}{LAMED}{QOF}",
    u"{MEM}{TET}{VAV}{TAV} - {MEM}{SAMECH}{AYIN}{YOD}",
    u"{NUN}{TZADE}{BET}{YOD}{FINAL_MEM} - {VAV}{YOD}{LAMED}{FINAL_KAF}"]


class Sedrah(IntEnum):
    """An enumeration class for weekly sedrahs"""
    BERESHITH = 1
    NOACH = 2
    LECH_LECHA = 3
    VAYYERA = 4
    CHAYYE_SARAH = 5
    TOLEDOTH = 6
    VAYYETZE = 7
    VAYYISHLACH = 8
    VAYYESHEV = 9
    MIKKETZ = 10
    VAYYIGASH = 11
    VAYYECHI = 12
    SHEMOTH = 13
    VAAYRA = 14
    BO = 15  # pylint: disable=invalid-name
    BESHALLACH = 16
    YITHRO = 17
    MISHPATIM = 18
    TERUMAH = 19
    TETZAVEH = 20
    KI_THISSA = 21
    VAYYAKHEL = 22
    PEKUDEY = 23
    VAYYIKRA = 24
    TZAV = 25
    SHEMINI = 26
    THAZRIA = 27
    METZORA = 28
    ACHAREY_MOS = 29
    KEDOSHIM = 30
    EMOR = 31
    BEHAR = 32
    BECHUKOSAI = 33
    BEMIDBAR = 34
    NASO = 35
    BEHAALOSECHA = 36
    SHELACH_LECHA = 37
    KORACH = 38
    CHUKKAS = 39
    BALAK = 40
    PINCHAS = 41
    MATTOS = 42
    MASSEY = 43
    DEVARIM = 44
    VAETHCHANAN = 45
    EKEV = 46
    REEH = 47
    SHOFETIM = 48
    KI_THETZE = 49
    KI_THAVO = 50
    NITZAVIM = 51
    VAYYELECH = 52
    HAAZINU = 53
    VZOTH_HABERACHAH = 54
    VAYYAKHEL_PEKUDEY = 55
    THAZRIA_METZORA = 56
    ACHAREY_KEDOSHIM = 57
    BEHAR_BECHUKOSAI = 58
    CHUKKAS_BALAK = 59
    MATTOS_MASSEY = 60
    NITZAVIM_VAYYELECH = 61

    def __str__(self):
        return self._name_.title()

    def __format__(self, fmt):
        return (self.__str__().replace("_",
                                       "-" if self > Sedrah.VZOTH_HABERACHAH
                                       else " ") if fmt == ""
                else HebrewString(HEBREW_SEDRAH_NAMES[self]).__format__(fmt))


RH_SAT_TABLE = (Sedrah.HAAZINU,           # Rosh Hashonah
                Sedrah.HAAZINU,
                Sedrah.VZOTH_HABERACHAH,  # Succoth
                Sedrah.VZOTH_HABERACHAH,  # Shmini Atzereth / Simchat Torah
                Sedrah.VZOTH_HABERACHAH)  # Simchat Torah (Diaspora) midweek

RH_MON_TUE_TABLE = (Sedrah.VAYYELECH,
                    Sedrah.HAAZINU,
                    Sedrah.VZOTH_HABERACHAH,  # Succoth
                    Sedrah.VZOTH_HABERACHAH)  # Simchat Torah

RH_THU_TABLE = (Sedrah.HAAZINU,
                Sedrah.VZOTH_HABERACHAH,  # Yom Kippur
                Sedrah.VZOTH_HABERACHAH,  # Succoth
                Sedrah.VZOTH_HABERACHAH)  # Simchat Torah

RH_TABLE = {Weekday.SATURDAY: RH_SAT_TABLE,
            Weekday.MONDAY: RH_MON_TUE_TABLE,
            Weekday.TUESDAY: RH_MON_TUE_TABLE,
            Weekday.THURSDAY: RH_THU_TABLE}

# The following table is used in a regular (not leap) year if:
#     Pesach falls on Thursday (Israel only)
#     Pesach falls on Tuesday
#     Pesach falls on Sunday (only if the year is lacking)
SEDRAH_TABLE1 = (Sedrah.VAYYAKHEL_PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,  # PESACH
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA_METZORA,
                 Sedrah.ACHAREY_KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR_BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a regular (not leap) year if:
#     Pesach falls on Thursday (Diaspora only)
SEDRAH_TABLE2 = (Sedrah.VAYYAKHEL_PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,  # PESACH
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA_METZORA,
                 Sedrah.ACHAREY_KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR_BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,  # SHAVUOS
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS_BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a regular (not leap) year if:
#     Pesach falls on Sunday (only if the year is full)
SEDRAH_TABLE3 = (Sedrah.VAYYAKHEL,
                 Sedrah.PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,  # PESACH
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA_METZORA,
                 Sedrah.ACHAREY_KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR_BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a regular (not leap) year if:
#     Pesach falls on Saturday (Israel only)
SEDRAH_TABLE4 = (Sedrah.VAYYAKHEL_PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,  # PESACH
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA_METZORA,
                 Sedrah.ACHAREY_KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR,
                 Sedrah.BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a regular (not leap) year if:
#     Pesach falls on Saturday (Diaspora only)
SEDRAH_TABLE5 = (Sedrah.VAYYAKHEL_PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,  # PESACH
                 Sedrah.SHEMINI,  # PESACH
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA_METZORA,
                 Sedrah.ACHAREY_KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR_BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a leap year if:
#     Pesach falls on Saturday (Israel only)
SEDRAH_TABLE6 = (Sedrah.VAYYAKHEL,
                 Sedrah.PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA,
                 Sedrah.METZORA,
                 Sedrah.ACHAREY_MOS,  # PESACH
                 Sedrah.ACHAREY_MOS,
                 Sedrah.KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR,
                 Sedrah.BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS,
                 Sedrah.MASSEY)

# The following table is used in a leap year if:
#     Pesach falls on Saturday (Diaspora only)
SEDRAH_TABLE7 = (Sedrah.VAYYAKHEL,
                 Sedrah.PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA,
                 Sedrah.METZORA,
                 Sedrah.ACHAREY_MOS,  # PESACH
                 Sedrah.ACHAREY_MOS,  # PESACH
                 Sedrah.ACHAREY_MOS,
                 Sedrah.KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR,
                 Sedrah.BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a leap year if:
#     Pesach falls on Thursday (Israel only)
#     Pesach falls on Tuesday (only if the year is lacking)
SEDRAH_TABLE8 = (Sedrah.VAYYAKHEL,
                 Sedrah.PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA,
                 Sedrah.METZORA,
                 Sedrah.ACHAREY_MOS,  # PESACH
                 Sedrah.ACHAREY_MOS,
                 Sedrah.KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR,
                 Sedrah.BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS,
                 Sedrah.BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a leap year if:
#     Pesach falls on Thursday (Diaspora only)
SEDRAH_TABLE9 = (Sedrah.VAYYAKHEL,
                 Sedrah.PEKUDEY,
                 Sedrah.VAYYIKRA,
                 Sedrah.TZAV,
                 Sedrah.SHEMINI,
                 Sedrah.THAZRIA,
                 Sedrah.METZORA,
                 Sedrah.ACHAREY_MOS,  # PESACH
                 Sedrah.ACHAREY_MOS,
                 Sedrah.KEDOSHIM,
                 Sedrah.EMOR,
                 Sedrah.BEHAR,
                 Sedrah.BECHUKOSAI,
                 Sedrah.BEMIDBAR,
                 Sedrah.NASO,        # SHAVUOS
                 Sedrah.NASO,
                 Sedrah.BEHAALOSECHA,
                 Sedrah.SHELACH_LECHA,
                 Sedrah.KORACH,
                 Sedrah.CHUKKAS_BALAK,
                 Sedrah.PINCHAS,
                 Sedrah.MATTOS_MASSEY)

# The following table is used in a leap year if:
#     Pesach falls on Tuesday (only if the year is full)
#     Pesach falls on Sunday
SEDRAH_TABLE10 = (Sedrah.VAYYAKHEL,
                  Sedrah.PEKUDEY,
                  Sedrah.VAYYIKRA,
                  Sedrah.TZAV,
                  Sedrah.SHEMINI,
                  Sedrah.THAZRIA,
                  Sedrah.METZORA,
                  Sedrah.ACHAREY_MOS,
                  Sedrah.KEDOSHIM,  # PESACH
                  Sedrah.KEDOSHIM,
                  Sedrah.EMOR,
                  Sedrah.BEHAR,
                  Sedrah.BECHUKOSAI,
                  Sedrah.BEMIDBAR,
                  Sedrah.NASO,
                  Sedrah.BEHAALOSECHA,
                  Sedrah.SHELACH_LECHA,
                  Sedrah.KORACH,
                  Sedrah.CHUKKAS,
                  Sedrah.BALAK,
                  Sedrah.PINCHAS,
                  Sedrah.MATTOS,
                  Sedrah.MASSEY)

# Rambam Hilchot Kiddush Hachodesh 6:3
LUNAR_CYCLE = abs_time.RelTime(4, 1, 12, 793)

# Any molad can be calculated by multiplying the number of months since a known
# molad by the lunar cycle (above) and adding it to the time of the known
# molad. For this purpose, the Rambam (ibid. 6:8) uses a mythical molad known
# as BaHaRaD (Day 2, 5 hours, 204 Chalakim) which would have occurred twelve
# months before the real first molad. If we add 12 cycles to this figure, it
# turns out that the molad of Tishri in the creation year took place at 8am on
# the sixth day of creation. I presume that the Rambam knew this from an Agadic
# source and performed the same calculation backwards to derive BaHaRaD. I
# prefer to use the real first molad.
FIRST_MOLAD = abs_time.AbsTime(0, Weekday.FRIDAY, 14)

SIX_HOURS = abs_time.RelTime(0, 0, 6)


class BadYearType(ValueError):
    """An exception class for an invalid Year Type"""
    pass


class YearType(IntEnum):
    """An enumeration class for type of year"""
    DEFECTIVE = 1
    REGULAR = 2
    FULL = 3


class HebrewYear(RegularYear):
    """Subclass of Year for the Hebrew calendar.

    Also handles sedrahs and day of the omer."""

    # Rambam Hilchot Kiddush Hachodesh 6:4
    MONTHS_IN_SIMPLE_YEAR = 12
    MONTHS_IN_LEAP_YEAR = 13

    # Rambam Hilchot Kiddush Hachodesh 6:10
    YEARS_IN_CYCLE = 19
    LEAP_YEARS_IN_CYCLE = 7

    # Rambam Hilchot Kiddush Hachodesh 8:2
    SHORT_MONTH = 29
    LONG_MONTH = 30

    MONTHS_IN_CYCLE = LEAP_YEARS_IN_CYCLE * MONTHS_IN_LEAP_YEAR +\
        (YEARS_IN_CYCLE - LEAP_YEARS_IN_CYCLE) * MONTHS_IN_SIMPLE_YEAR

    # Rambam Hilchot Kiddush Hachodesh 8:6 (loosely)
    REGULAR_YEAR_DAYS = 354  # On average, can be 353, 354 or 355
    LEAP_YEAR_DAYS = 384     # On average, can be 383, 384 or 385

    # The year of the first molad
    FIRST_YEAR = 2

    START_FIRST_YEAR = FIRST_MOLAD

    # GaTRaD and BTUTKPaT are explained in start_year below.
    # GaTRaD : Gimmel = Day 3 (Tuesday), Tet = 9 (Hours),
    # Reish Dalet = 204 chalakim
    GaTRaD = (abs_time.RelTime(50, Weekday.SATURDAY, 18) -
              MONTHS_IN_SIMPLE_YEAR * LUNAR_CYCLE)

    # BTUTKPaT: Bet = Day 2 (Monday), Tet Vav = 15 (Hours),
    # Taf Kuf Pay Tet = 589 (Chalakim)
    BTUTKPaT = (abs_time.RelTime(-55, Weekday.TUESDAY, 18) +
                MONTHS_IN_LEAP_YEAR * LUNAR_CYCLE)

    # Date in Tishri of Simchat Torah
    SIMCHAT_TORAH_ISRAEL = 22
    SIMCHAT_TORAH_DIASPORA = 23
    SIMCHAT_TORAH = (SIMCHAT_TORAH_DIASPORA, SIMCHAT_TORAH_ISRAEL)

    def months(self):
        """A generator for the months of the current year."""
        for month in range(HebrewMonth.start_year_month(),
                           self.months_in_year() + 1):
            yield HebrewMonth(month)
        for month in range(1, HebrewMonth.end_year_month() + 1):
            yield HebrewMonth(month)

    def months_in_year(self):
        """Return the number of months in a year.

        The method is (arguably) simpler than the method given by
        Rambam Hilchot Kiddush Hachodesh 6:11"""
        return (self.MONTHS_IN_LEAP_YEAR if (self.value * 7 + 1) % 19 < 7 else
                self.MONTHS_IN_SIMPLE_YEAR)

    def year_type(self):
        """Return the year type of the current year.

        A Defective year has 353 or 383 days.
        A Regular year has 354 or 384 days.
        A Full year has 355 or 385 days.

        Source: Rambam Hilchot Kiddush Hachodesh 8:6 (loosely)"""
        return (YearType.DEFECTIVE, YearType.REGULAR,
                YearType.FULL)[(self.days_in_year() - 3) % 5]

    def _cheshvan_days(self):
        """Return the number of days in Cheshvan."""
        return self.LONG_MONTH if (YearType.FULL ==
                                   self.year_type()) else self.SHORT_MONTH

    # Rambam Hilchot Kiddush Hachodesh 8:7
    def _kislev_days(self):
        """Return the number of days in Kislev."""

        return (self.SHORT_MONTH if self.year_type() == YearType.DEFECTIVE else
                self.LONG_MONTH)

    # Rambam Hilchot Kiddush Hachodesh 8:5
    def _adar1_days(self):
        """Return the number of days in Adar Rishon (Adar in regular year."""
        return self.SHORT_MONTH if (self.MONTHS_IN_SIMPLE_YEAR ==
                                    self.months_in_year()) else self.LONG_MONTH

    # Rambam Hilchot Kiddush Hachodesh 8:5
    MONTH_DAYS = (None, LONG_MONTH, SHORT_MONTH, LONG_MONTH, SHORT_MONTH,
                  LONG_MONTH, SHORT_MONTH, LONG_MONTH, _cheshvan_days,
                  _kislev_days, SHORT_MONTH, LONG_MONTH, _adar1_days,
                  SHORT_MONTH)

    def days_in_month(self, month):
        """Return the number of days in a given month."""
        month_days = HebrewYear.MONTH_DAYS[month]
        return month_days if isinstance(month_days, int) else month_days(self)

    @staticmethod
    def month_class():
        return HebrewMonth

    def adjust_date(self, month, date):
        """Check if the month and date supplied are valid for the current year.

        Returns a tuple comprising the month and date, adjusted if necessary
        to make them valid, as follows.

        In a regular (not leap year), Adar sheni is converted to Adar.
        If Cheshvan has 29 days, 30th Cheshvan is converted to 1st Kislev.
        If Kislev has 29 days, 30th Kislev is converted to 1st Teveth.
        If the month and date are still invalid, an exception is thrown."""

        try:
            month, date = super(HebrewYear, self).adjust_date(month, date)
        except MonthNotInRange:
            if month == HebrewMonth.ADAR_SHENI:
                # Substitute Adar Rishon in a non-leap year
                month, date = super(HebrewYear,
                                    self).adjust_date(HebrewMonth.ADAR_RISHON,
                                                      date)
            else:
                raise
        except DateNotInRange:
            if month in (HebrewMonth.CHESHVAN, HebrewMonth.KISLEV,
                         HebrewMonth.ADAR_RISHON) and date == self.LONG_MONTH:
                month = HebrewMonth.NISSAN \
                    if month == HebrewMonth.ADAR_RISHON else month + 1
                month, date = super(HebrewYear, self).adjust_date(month, 1)
            else:
                raise
        return month, date

    def format_date(self, month, date, fmt):
        month_name = format(month, fmt)
        if self.months_in_year() == self.MONTHS_IN_SIMPLE_YEAR:
            month_name = month_name.split(" ",
                                          1)[::-1 if fmt == "#R" else 1][0]
        date_fmt = u"{y} {m} {d}" if fmt == "#R" else u"{d} {m} {y}"
        return date_fmt.format(y=self.value, m=month_name, d=date)

    def molad(self, month=HebrewMonth.TISHRI):
        """Return the absolute time of the molad of the current month."""

        # Check validity
        month = self.adjust_date(month, 1)[0]
        months = month - HebrewMonth.TISHRI
        if months < 0:
            months += self.months_in_year()

        return months * LUNAR_CYCLE + self._start

    @property
    def start(self):
        """Returns the time at which the current year starts."""

        # If the molad for Tishri occurs at or after midday,
        # delay Rosh Hashanah by one day.
        # Rambam Hilchot Kiddush Hachodesh 7:2
        # The reason for the delay appears to be based on Rosh Hashonah 20b.
        rh_start = self._start + SIX_HOURS

        # Rosh Hashonah cannot fall on Sunday Wednesday or Friday
        # Rambam Hilchot Kiddush Hachodesh 7:1, 7:3
        if rh_start.days in (Weekday.SUNDAY, Weekday.WEDNESDAY,
                             Weekday.FRIDAY):
            rh_start += DAY

        rh_start = abs_time.AbsTime(absTime=rh_start, weeks=True, days=True)

        # At this point, if Rosh Hashanah has been postponed, there will be no
        # further postponements.
        if rh_start > self._start:
            return rh_start

        # If the year has 12 months and the molad for Tishri falls on Tuesday
        # after GaTRaD (see above for definition), Rosh Hashonah is delayed
        # until Thursday (Rambam Hilchot Kiddush 7:4). This is because the
        # molad for Tishri for the following year will fall on or after midday
        # on Saturday, and therefore Rosh Hashonah next year will be on Monday.
        # However, if Rosh Hashonah this year falls on Tuesday, Rosh Hashonah
        # next year can only fall on Saturday (ibid. 8:7 and 7:1).
        if (self._start.days == Weekday.TUESDAY and
                self.months_in_year() == self.MONTHS_IN_SIMPLE_YEAR and
                self._start > abs_time.AbsTime(absTime=self._start,
                                               weeks=True) + self.GaTRaD):
            rh_start += DAY * 2

        # If the previous year has 13 months and the molad for Tishri
        # (thisyear) falls on Monday after BTUTKPaT (see above for definition),
        # Rosh Hashonah is delayed until Tuesday (Rambam Hilchot Kiddush 7:5).
        # This is because the molad for Tishri for the previous year fell on or
        # after midday on Tuesday, and therefore Rosh Hashonah was delayed to
        # Thursday. Therefore, Rosh Hashonah this year can only fall on Tuesday
        # or Thursday (ibid. 8:8 and 7:1).
        if (self._start.days == Weekday.MONDAY and
                (self - 1).months_in_year() == self.MONTHS_IN_LEAP_YEAR and
                self._start > abs_time.AbsTime(absTime=self._start,
                                               weeks=True) + self.BTUTKPaT):
            rh_start += DAY

        return rh_start

    def days_in_year(self):
        """Return the number of days in the current year."""
        return ((self + 1).start - self.start).days

    def duration(self):
        """Return the time between Molad Tishri of the current and next year.
        """
        return self.months_in_year() * LUNAR_CYCLE

    # Not all years are the same length, but there is a cycle of 19 years
    # where the length of a cycle is fixed. This is only true of the Molad
    # used to calculate the start of the year (so cycles are not exactly the
    # same length).

    @classmethod
    def _years_per_cycle(cls):
        """Return number of years in a cycle."""
        return cls.YEARS_IN_CYCLE

    @classmethod
    def _cycle_duration(cls):
        """Return length of a cycle (RelTime)."""
        return ((cls.YEARS_IN_CYCLE - cls.LEAP_YEARS_IN_CYCLE) *
                cls.MONTHS_IN_SIMPLE_YEAR +
                cls.LEAP_YEARS_IN_CYCLE * cls.MONTHS_IN_LEAP_YEAR) *\
            LUNAR_CYCLE

    def sedrah(self, month, date, israel):
        """Returns the sedrah for the month and date in the current year.

        israel is a boolean (True for Israel, False for Diaspora."""

        month, date = self.adjust_date(month, date)

        rh_day = self.start.days
        if month == HebrewMonth.TISHRI and date <= self.SIMCHAT_TORAH[israel]:
            # Count the number of sabbaths from the sabbath on or after
            # Rosh Hashonah to the sabbath on or after today.
            week_count = (date + rh_day - 1) // DAYS_IN_WEEK
            # if rh_day == Weekday.SATURDAY:
            #     table = RH_SATURDAY_TABLE
            # elif rh_day == Weekday.THURSDAY:
            #     table = RH_THURSDAY_TABLE
            # else:
            #     table = RH_MONDAY_TUESDAY_TABLE
            return RH_TABLE[rh_day][week_count]
        else:
            pesach_day = (rh_day + self.days_in_year() - 2) % DAYS_IN_WEEK
            if self.months_in_year() == self.MONTHS_IN_SIMPLE_YEAR:
                if pesach_day == Weekday.SATURDAY:
                    table = SEDRAH_TABLE4 if israel else SEDRAH_TABLE5
                else:
                    if pesach_day == Weekday.THURSDAY and not israel:
                        table = SEDRAH_TABLE2
                    elif (pesach_day == Weekday.SUNDAY and
                          self.year_type() == YearType.FULL):
                        table = SEDRAH_TABLE3
                    else:
                        table = SEDRAH_TABLE1
            else:
                if pesach_day == Weekday.SATURDAY:
                    table = SEDRAH_TABLE6 if israel else SEDRAH_TABLE7
                else:
                    if pesach_day == Weekday.THURSDAY and not israel:
                        table = SEDRAH_TABLE9
                    elif ((pesach_day == Weekday.TUESDAY and
                           self.year_type() == YearType.FULL) or
                          pesach_day == Weekday.SUNDAY):
                        table = SEDRAH_TABLE10
                    else:
                        table = SEDRAH_TABLE8

            # Calculate the date of the next sabbath (or today if today
            # is the sabbath).
            next_shabbat = self.day_start(month, date)
            next_shabbat += abs_time.RelTime(0, 6 - next_shabbat.days, 0, 0)
            # Bereshith is the last sabbath in tishri.
            shabbat_bereshith = self.day_start(HebrewMonth.TISHRI,
                                               29 if rh_day == Weekday.SATURDAY
                                               else 28 - rh_day)

#           Calculate the number of sabbaths from Shabbat Bereshith to the
#           current or next sabbath.
            week_count = (next_shabbat - shabbat_bereshith).weeks
            return (tuple(Sedrah)[:int(Sedrah.KI_THISSA)] + table +
                    tuple(Sedrah)[int(Sedrah.DEVARIM) - 1:
                                  int(Sedrah.KI_THAVO)] +
                    ((Sedrah.NITZAVIM, Sedrah.VAYYELECH)
                     if pesach_day in (Weekday.SATURDAY, Weekday.SUNDAY) else
                     (Sedrah.NITZAVIM_VAYYELECH,)) +
                    (Sedrah.HAAZINU,))[week_count]

    def omer_day(self, month, date):
        """Return day of the omer (or None if outside the omer)."""
        month, date = self.adjust_date(month, date)
        if (HebrewMonth.NISSAN, 15) < (month, date) < (HebrewMonth.SIVAN, 6):
            return ((self.day_start(month, date) -
                     self.day_start(HebrewMonth.NISSAN, 15)) // DAY)
        return None
