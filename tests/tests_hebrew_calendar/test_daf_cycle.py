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

import unittest
import logging

from hbcal.hebrew_calendar import date
from hbcal.hebrew_calendar.daf_yomi import DafYomiCycle, Tractate, DateBeforeDafYomi
from hbcal.hebrew_calendar.abs_time import AbsTime

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestYearStart(unittest.TestCase):
    def test_first_cycle(self):
        self.assertEqual(AbsTime(296475, 2, 6, 0), DafYomiCycle(1).start)

    def test_second_cycle(self):
        self.assertEqual(AbsTime(296861, 2, 6, 0), DafYomiCycle(2).start)

    def test_eighth_cycle(self):
        self.assertEqual(AbsTime(299177, 2, 6, 0), DafYomiCycle(8).start)

    def test_ninth_cycle(self):
        self.assertEqual(AbsTime(299564, 4, 6, 0), DafYomiCycle(9).start)


class TestValidate(unittest.TestCase):

    def test_zeroth_cycle(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(0), Tractate.NIDAH, 20)

    def test_start_first_cycle(self):
        test_date = date.Date(DafYomiCycle(1), Tractate.BERACHOS, 2)
        self.assertEqual((1, 1, 2),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus1_tractate(self):
        """ Tests a month value of -1

        This is now valid. It is the last month of the year.
        """
        test_date = date.Date(DafYomiCycle(10), -1, 23)
        self.assertEqual((10, Tractate.NIDAH, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus37_tractate(self):
        """ Tests a month value of -12

        This is now valid. For negative months we count back from the end of
        the year.
        """
        test_date = date.Date(DafYomiCycle(10), -37, 23)
        self.assertEqual((10, Tractate.BERACHOS, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_tractate(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), -38, 23)

    def test_zero_tractate(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), 0, 23)

    def test_month_too_big(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), 41, 23)

    def test_minus1_daf(self):
        """ Tests a date value of -1.

        This is now valid. It is the last date of the month.
        """
        test_date = date.Date(DafYomiCycle(10), Tractate.SUCCAH, -1)
        self.assertEqual((10, Tractate.SUCCAH, 56),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_small_negative_date(self):
        """ Tests a small negative value for date.

        This is now valid. For negative dates we count back from the end of
        the month.
        """
        test_date = date.Date(DafYomiCycle(10), Tractate.SUCCAH, -7)
        self.assertEqual((10, Tractate.SUCCAH, 50),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_date(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SUCCAH, -56)

    def test_zero_daf(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SUCCAH, 0)

    def test_daf_alef(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SUCCAH, 1)

    def test_berachos_64(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.BERACHOS, 64)
        self.assertEqual((10, Tractate.BERACHOS, 64),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_berachos_65(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.BERACHOS, 65)

    def test_shabbos_157(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.SHABBOS, 157)
        self.assertEqual((10, 2, 157),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_shabbos_158(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SHABBOS, 158)

    def test_eruvin_105(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.ERUVIN, 105)
        self.assertEqual((10, 3, 105),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_eruvin_106(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.ERUVIN, 106)

    def test_pesachim_121(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.PESACHIM, 121)
        self.assertEqual((10, 4, 121),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_pesachim_122(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.PESACHIM, 122)

    def test_shekalim_13(self):
        test_date = date.Date(DafYomiCycle(7), Tractate.SHEKALIM, 13)
        self.assertEqual((7, Tractate.SHEKALIM, 13),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_shekalim_14_original(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(7), Tractate.SHEKALIM, 14)

    def test_shekalim_14_adjusted(self):
        test_date = date.Date(DafYomiCycle(8), Tractate.SHEKALIM, 14)
        self.assertEqual((8, Tractate.SHEKALIM, 14),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_shekalim_22_adjusted(self):
        test_date = date.Date(DafYomiCycle(8), Tractate.SHEKALIM, 22)
        self.assertEqual((8, Tractate.SHEKALIM, 22),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_shekalim_23_adjusted(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(8), Tractate.SHEKALIM, 23)

    def test_yoma_88(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.YOMA, 88)
        self.assertEqual((10, Tractate.YOMA, 88),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_yoma_89(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.YOMA, 89)

    def test_succah_56(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.SUCCAH, 56)
        self.assertEqual((10, Tractate.SUCCAH, 56),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_succah_57(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SUCCAH, 57)

    def test_beitzah_40(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.BEITZAH, 40)
        self.assertEqual((10, Tractate.BEITZAH, 40),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_beitzah_41(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.BEITZAH, 41)

    def test_rosh_hashanah_35(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.ROSH_HASHANAH, 35)
        self.assertEqual((10, Tractate.ROSH_HASHANAH, 35),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_rosh_hashanah_36(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.ROSH_HASHANAH, 36)

    def test_taanis_31(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.TAANIS, 31)
        self.assertEqual((10, Tractate.TAANIS, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_taanis_32(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.TAANIS, 32)

    def test_megilah_32(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.MEGILAH, 32)
        self.assertEqual((10, Tractate.MEGILAH, 32),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_megilah_33(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.MEGILAH, 33)

    def test_moed_katan_29(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.MOED_KATAN, 29)
        self.assertEqual((10, Tractate.MOED_KATAN, 29),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_moed_katan_30(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.MOED_KATAN, 30)

    def test_chagigah_27(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.CHAGIGAH, 27)
        self.assertEqual((10, Tractate.CHAGIGAH, 27),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_chagigah_28(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.CHAGIGAH, 28)

    def test_yevamos_122(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.YEVAMOS, 122)
        self.assertEqual((10, Tractate.YEVAMOS, 122),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_yevamos_123(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.YEVAMOS, 123)

    def test_kesuvos_112(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.KESUVOS, 112)
        self.assertEqual((10, Tractate.KESUVOS, 112),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_kesuvos_113(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.KESUVOS, 113)

    def test_nedarim_91(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.NEDARIM, 91)
        self.assertEqual((10, Tractate.NEDARIM, 91),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_nedarim_92(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.NEDARIM, 92)

    def test_nazir_66(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.NAZIR, 66)
        self.assertEqual((10, Tractate.NAZIR, 66),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_nazir_67(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.NAZIR, 67)

    def test_sotah_49(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.SOTAH, 49)
        self.assertEqual((10, Tractate.SOTAH, 49),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_sotah_50(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SOTAH, 50)

    def test_gitin_90(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.GITIN, 90)
        self.assertEqual((10, Tractate.GITIN, 90),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_gitin_91(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.GITIN, 91)

    def test_kiddushin_82(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.KIDDUSHIN, 82)
        self.assertEqual((10, Tractate.KIDDUSHIN, 82),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_kiddushin_83(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.KIDDUSHIN, 83)

    def test_bava_kama_119(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.BAVA_KAMA, 119)
        self.assertEqual((10, Tractate.BAVA_KAMA, 119),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_bava_kama_120(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.BAVA_KAMA, 120)

    def test_bava_metzia_119(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.BAVA_METZIA, 119)
        self.assertEqual((10, Tractate.BAVA_METZIA, 119),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_bava_metzia_120(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.BAVA_METZIA, 120)

    def test_bava_basra_176(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.BAVA_BASRA, 176)
        self.assertEqual((10, Tractate.BAVA_BASRA, 176),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_bava_basra_177(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.BAVA_BASRA, 177)

    def test_sanhedrin_113(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.SANHEDRIN, 113)
        self.assertEqual((10, Tractate.SANHEDRIN, 113),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_sanhedrin_114(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SANHEDRIN, 114)

    def test_makkos_24(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.MAKKOS, 24)
        self.assertEqual((10, Tractate.MAKKOS, 24),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_makkos_25(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.MAKKOS, 25)

    def test_shevuos_49(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.SHEVUOS, 49)
        self.assertEqual((10, Tractate.SHEVUOS, 49),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_shevuos_50(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.SHEVUOS, 50)

    def test_avoda_zarah_76(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.AVODA_ZARAH, 76)
        self.assertEqual((10, Tractate.AVODA_ZARAH, 76),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_avoda_zarah_77(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.AVODA_ZARAH, 77)

    def test_horayos_14(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.HORAYOS, 14)
        self.assertEqual((10, Tractate.HORAYOS, 14),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_horayos_15(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.HORAYOS, 15)

    def test_zevachim_120(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.ZEVACHIM, 120)
        self.assertEqual((10, Tractate.ZEVACHIM, 120),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_zevachim_121(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.ZEVACHIM, 121)

    def test_menachos_110(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.MENACHOS, 110)
        self.assertEqual((10, Tractate.MENACHOS, 110),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_menachos_111(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.MENACHOS, 111)

    def test_chulin_142(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.CHULIN, 142)
        self.assertEqual((10, Tractate.CHULIN, 142),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_chulin_143(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.CHULIN, 143)

    def test_bechoros_61(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.BECHOROS, 61)
        self.assertEqual((10, Tractate.BECHOROS, 61),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_bechoros_62(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.BECHOROS, 62)

    def test_erchin_34(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.ERCHIN, 34)
        self.assertEqual((10, Tractate.ERCHIN, 34),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_erchin_35(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.ERCHIN, 35)

    def test_temurah_34(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.TEMURAH, 34)
        self.assertEqual((10, Tractate.TEMURAH, 34),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_temurah_35(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.TEMURAH, 35)

    def test_kerisus_28(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.KERISUS, 28)
        self.assertEqual((10, Tractate.KERISUS, 28),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_kerisus_29(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.KERISUS, 29)

    def test_meilah_37(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.MEILAH, 37)
        self.assertEqual((10, Tractate.MEILAH, 37),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_meilah_38(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.MEILAH, 38)

    def test_nidah_73(self):
        test_date = date.Date(DafYomiCycle(10), Tractate.NIDAH, 73)
        self.assertEqual((10, Tractate.NIDAH, 73),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_nidah_74(self):
        with self.assertRaises(ValueError):
            date.Date(DafYomiCycle(10), Tractate.NIDAH, 74)


class TestCurrentDate(unittest.TestCase):
    def test_before_first_cycle(self):
        with self.assertRaises(DateBeforeDafYomi):
            date.Date(DafYomiCycle, AbsTime(296475, 2, 5, 1079))

    def test_start_of_first_cycle(self):
        self.assertEqual(date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 2),
                         date.Date(DafYomiCycle, AbsTime(296475, 2, 6, 0)))

    def test_end_first_day(self):
        self.assertEqual(date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 2),
                         date.Date(DafYomiCycle, AbsTime(296475, 3, 5, 1079)))

    def test_start_second_day(self):
        self.assertEqual(date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 3),
                         date.Date(DafYomiCycle, AbsTime(296475, 3, 6, 0)))

    def test_last_day_berachos(self):
        self.assertEqual(date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 64),
                         date.Date(DafYomiCycle, AbsTime(296484, 1, 6, 0)))

    def test_first_day_shabbos(self):
        self.assertEqual(date.Date(DafYomiCycle(1),
                                   Tractate.SHABBOS, 2),
                         date.Date(DafYomiCycle, AbsTime(296484, 2, 6, 0)))

    def test_last_day_nidah(self):
        self.assertEqual(date.Date(DafYomiCycle(1),
                                   Tractate.NIDAH, 73),
                         date.Date(DafYomiCycle, AbsTime(296861, 1, 6, 0)))

    def test_first_day_second_cycle(self):
        self.assertEqual(date.Date(DafYomiCycle(2),
                                   Tractate.BERACHOS, 2),
                         date.Date(DafYomiCycle, AbsTime(296861, 2, 6, 0)))

    def test_first_day_recent_cycle(self):
        self.assertEqual(date.Date(DafYomiCycle(14),
                                   Tractate.BERACHOS, 2),
                         date.Date(DafYomiCycle, AbsTime(301501, 0, 6, 0)))

    # Check that we still get the right answers even if we use a ridiculously
    # low (or high) heuristic for the number of weeks in a year.
    def test_first_day_recent_year_low_heuristic(self):

        class DafYomiLowDays(DafYomiCycle):
            @classmethod
            def estimate_current_year(cls, atime):
                return int(((atime - cls.start_first_year()).days) / 1500 + 0.5) +\
                    cls.first_year()

        self.assertEqual(date.Date(DafYomiLowDays(14),
                                   Tractate.BERACHOS, 2),
                         date.Date(DafYomiLowDays, AbsTime(301501, 0, 6, 0)))

    def test_first_day_recent_year_high_heuristic(self):

        class DafYomiHighDays(DafYomiCycle):
            @classmethod
            def estimate_current_year(cls, atime):
                return int(((atime - cls.start_first_year()).days) / 4000 + 0.5) +\
                    cls.first_year()

        self.assertEqual(date.Date(DafYomiHighDays(14),
                                   Tractate.BERACHOS, 2),
                         date.Date(DafYomiHighDays, AbsTime(301501, 0, 6, 0)))


class TestDayStart(unittest.TestCase):

    def test_start_of_first_year(self):
        self.assertEqual(AbsTime(296475, 2, 6, 0),
                         date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 2).day_start())

    def test_second_day(self):
        self.assertEqual(AbsTime(296475, 3, 6, 0),
                         date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 3).day_start())

    def test_last_day_berachos(self):
        self.assertEqual(AbsTime(296484, 1, 6, 0),
                         date.Date(DafYomiCycle(1),
                                   Tractate.BERACHOS, 64).day_start())

    def test_first_day_shabbos(self):
        self.assertEqual(AbsTime(296484, 2, 6, 0),
                         date.Date(DafYomiCycle(1),
                                   Tractate.SHABBOS, 2).day_start())

    def test_last_day_nidah(self):
        self.assertEqual(AbsTime(296861, 1, 6, 0),
                         date.Date(DafYomiCycle(1),
                                   Tractate.NIDAH, 73).day_start())

    def test_first_day_second_cycle(self):
        self.assertEqual(AbsTime(296861, 2, 6, 0),
                         date.Date(DafYomiCycle(2),
                                   Tractate.BERACHOS, 2).day_start())

    def test_first_day_recent_cycle(self):
        self.assertEqual(AbsTime(301501, 0, 6, 0),
                         date.Date(DafYomiCycle(14),
                                   Tractate.BERACHOS, 2).day_start())


if __name__ == '__main__':
    unittest.main()
