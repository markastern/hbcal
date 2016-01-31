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
from hbcal.hebrew_calendar.date import MonthNotInRange

from hbcal.hebrew_calendar.hebrew_year import HebrewYear, HebrewMonth, Sedrah
logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestPesachSundayRegularIsrael(unittest.TestCase):
    """Tests a regular year where the first day of Pesach is Sunday, in Israel.

    Also tests Rosh Hashonah on Monday."""
    test_year = HebrewYear(5734)
    israel = True

    def test_invalid_month(self):
        with self.assertRaises(MonthNotInRange):
            self.test_year.sedrah(14, 6, self.israel)

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 2,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 3,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 4,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 10,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 17,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 30,
                                               self.israel),
                         Sedrah.NOACH)

    def test_cheshvan_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 1,
                                               self.israel),
                         Sedrah.NOACH)

    def test_cheshvan_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 8,
                                               self.israel),
                         Sedrah.LECH_LECHA)

    def test_cheshvan_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 15,
                                               self.israel),
                         Sedrah.VAYYERA)

    def test_cheshvan_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 22,
                                               self.israel),
                         Sedrah.CHAYYE_SARAH)

    def test_cheshvan_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 29,
                                               self.israel),
                         Sedrah.TOLEDOTH)

    def test_kislev_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 6,
                                               self.israel),
                         Sedrah.VAYYETZE)

    def test_kislev_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 13,
                                               self.israel),
                         Sedrah.VAYYISHLACH)

    def test_kislev_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 20,
                                               self.israel),
                         Sedrah.VAYYESHEV)

    def test_kislev_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 27,
                                               self.israel),
                         Sedrah.MIKKETZ)

    def test_tevet_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 4,
                                               self.israel),
                         Sedrah.VAYYIGASH)

    def test_teveth_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 11,
                                               self.israel),
                         Sedrah.VAYYECHI)

    def test_teveth_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 18,
                                               self.israel),
                         Sedrah.SHEMOTH)

    def test_teveth_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 25,
                                               self.israel),
                         Sedrah.VAAYRA)

    def test_shevat_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 3,
                                               self.israel),
                         Sedrah.BO)

    def test_shevat_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 10,
                                               self.israel),
                         Sedrah.BESHALLACH)

    def test_shevat_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 17,
                                               self.israel),
                         Sedrah.YITHRO)

    def test_shevat_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 24,
                                               self.israel),
                         Sedrah.MISHPATIM)

    def test_adar_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 1,
                                               self.israel),
                         Sedrah.TERUMAH)

    def test_adar_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 8,
                                               self.israel),
                         Sedrah.TETZAVEH)

    def test_adar_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 15,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 22,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 29,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_nissan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 7,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 14,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 21,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 28,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 5,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 12,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 19,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 26,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_sivan_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 4,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 11,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 18,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 25,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 2,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 9,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 16,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 23,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_av_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 1,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 8,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 15,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_av_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 22,
                                               self.israel),
                         Sedrah.EKEV)

    def test_av_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 29,
                                               self.israel),
                         Sedrah.REEH)

    def test_ellul_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 6,
                                               self.israel),
                         Sedrah.SHOFETIM)

    def test_ellul_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 13,
                                               self.israel),
                         Sedrah.KI_THETZE)

    def test_ellul_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 20,
                                               self.israel),
                         Sedrah.KI_THAVO)

    def test_ellul_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 27,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachSundayRegularDiaspora(unittest.TestCase):
    """Tests a regular year where the first day of Pesach is Sunday, not in Israel.

    Also tests Rosh Hashonah on Monday."""
    test_year = HebrewYear(5734)
    israel = False

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 2,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 3,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 4,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 10,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 17,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 30,
                                               self.israel),
                         Sedrah.NOACH)

    def test_cheshvan_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 1,
                                               self.israel),
                         Sedrah.NOACH)

    def test_cheshvan_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 8,
                                               self.israel),
                         Sedrah.LECH_LECHA)

    def test_cheshvan_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 15,
                                               self.israel),
                         Sedrah.VAYYERA)

    def test_cheshvan_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 22,
                                               self.israel),
                         Sedrah.CHAYYE_SARAH)

    def test_cheshvan_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.CHESHVAN, 29,
                                               self.israel),
                         Sedrah.TOLEDOTH)

    def test_kislev_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 6,
                                               self.israel),
                         Sedrah.VAYYETZE)

    def test_kislev_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 13,
                                               self.israel),
                         Sedrah.VAYYISHLACH)

    def test_kislev_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 20,
                                               self.israel),
                         Sedrah.VAYYESHEV)

    def test_kislev_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.KISLEV, 27,
                                               self.israel),
                         Sedrah.MIKKETZ)

    def test_tevet_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 4,
                                               self.israel),
                         Sedrah.VAYYIGASH)

    def test_teveth_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 11,
                                               self.israel),
                         Sedrah.VAYYECHI)

    def test_teveth_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 18,
                                               self.israel),
                         Sedrah.SHEMOTH)

    def test_teveth_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TEVETH, 25,
                                               self.israel),
                         Sedrah.VAAYRA)

    def test_shevat_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 3,
                                               self.israel),
                         Sedrah.BO)

    def test_shevat_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 10,
                                               self.israel),
                         Sedrah.BESHALLACH)

    def test_shevat_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 17,
                                               self.israel),
                         Sedrah.YITHRO)

    def test_shevat_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SHEVAT, 24,
                                               self.israel),
                         Sedrah.MISHPATIM)

    def test_adar_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 1,
                                               self.israel),
                         Sedrah.TERUMAH)

    def test_adar_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 8,
                                               self.israel),
                         Sedrah.TETZAVEH)

    def test_adar_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 15,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 22,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 29,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_nissan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 7,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 14,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 21,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 28,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 5,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 12,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 19,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 26,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_sivan_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 4,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 11,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 18,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 25,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 2,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 9,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 16,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 23,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_av_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 1,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 8,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 15,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_av_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 22,
                                               self.israel),
                         Sedrah.EKEV)

    def test_av_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 29,
                                               self.israel),
                         Sedrah.REEH)

    def test_ellul_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 6,
                                               self.israel),
                         Sedrah.SHOFETIM)

    def test_ellul_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 13,
                                               self.israel),
                         Sedrah.KI_THETZE)

    def test_ellul_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 20,
                                               self.israel),
                         Sedrah.KI_THAVO)

    def test_ellul_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 27,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachSaturdayLeapIsrael(unittest.TestCase):

    test_year = HebrewYear(5725)
    israel = True

    def test_adar1_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 18,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 25,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar2_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 2,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 9,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 16,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 23,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 1,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 8,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 15,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 22,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 29,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 6,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 13,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 20,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 27,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 5,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 12,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 19,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 26,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 3,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 10,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 17,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 24,
                                               self.israel),
                         Sedrah.MATTOS)

    def test_av_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 2,
                                               self.israel),
                         Sedrah.MASSEY)

    def test_av_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 9,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 16,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 28,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachSaturdayLeapDiaspora(unittest.TestCase):

    test_year = HebrewYear(5725)
    israel = False

    def test_adar1_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 18,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 25,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar2_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 2,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 9,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 16,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 23,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 1,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 8,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 15,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 22,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 29,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_iyar_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 6,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 13,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 20,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 27,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_sivan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 5,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 12,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 19,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 26,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 3,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 10,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 17,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 24,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_av_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 2,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 9,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 16,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 28,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachSaturdayRegularIsrael(unittest.TestCase):
    """This also tests Rosh Hashonah on a Thursday"""

    test_year = HebrewYear(5701)
    israel = True

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 3,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 10,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 17,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_adar1_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 16,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 23,
                                               self.israel),
                         Sedrah.VAYYAKHEL_PEKUDEY)

    def test_nissan_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 1,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 8,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 15,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 22,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 29,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 6,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 13,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 20,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 27,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_sivan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 5,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 12,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 19,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 26,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 3,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 10,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 17,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 24,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_av_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 2,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 9,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 16,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 28,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachSaturdayRegularDiaspora(unittest.TestCase):
    """This also tests Rosh Hashonah on a Thursday"""

    test_year = HebrewYear(5701)
    israel = False

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 3,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 10,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 17,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_adar1_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 16,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 23,
                                               self.israel),
                         Sedrah.VAYYAKHEL_PEKUDEY)

    def test_nissan_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 1,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 8,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 15,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 22,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 29,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 6,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 13,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 20,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 27,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_sivan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 5,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 12,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 19,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 26,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 3,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 10,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 17,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 24,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_av_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 2,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 9,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 16,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 28,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachThurdayRegularIsrael(unittest.TestCase):
    test_year = HebrewYear(5702)
    israel = True

    def test_adar1_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 18,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 25,
                                               self.israel),
                         Sedrah.VAYYAKHEL_PEKUDEY)

    def test_nissan_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 3,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 10,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 15,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 22,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 1,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 8,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 15,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 22,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_iyar_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 29,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 7,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 14,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 21,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 28,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 5,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 12,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 19,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 26,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 4,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 11,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 23,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestPesachThursdayRegularDiaspora(unittest.TestCase):
    test_year = HebrewYear(5702)
    israel = False

    def test_adar1_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 18,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 25,
                                               self.israel),
                         Sedrah.VAYYAKHEL_PEKUDEY)

    def test_nissan_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 3,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 10,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 15,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 22,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 1,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 8,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 15,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 22,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_iyar_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 29,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 7,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 14,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 21,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 28,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 5,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 12,
                                               self.israel),
                         Sedrah.CHUKKAS_BALAK)

    def test_tammuz_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 19,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 26,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 4,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 11,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 23,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestPesachTuesdayLeapIsrael(unittest.TestCase):
    test_year = HebrewYear(5700)
    israel = True

    def test_adar1_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 15,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 22,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar1_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 29,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_6_(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 6,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 13,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 20,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_adar2_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 27,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 5,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 12,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 19,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_nissan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 26,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 3,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 10,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 17,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 24,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 2,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 9,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 16,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 23,
                                               self.israel),
                         Sedrah.KORACH)

    def test_sivan_30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 30,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 7,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 14,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 21,
                                               self.israel),
                         Sedrah.MATTOS)

    def test_tammuz_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 28,
                                               self.israel),
                         Sedrah.MASSEY)

    def test_av_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 6,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 13,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 25,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestPesachTuesdayLeapDiaspora(unittest.TestCase):
    test_year = HebrewYear(5700)
    israel = False

    def test_adar1_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 15,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 22,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar1_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 29,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_6_(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 6,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 13,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 20,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_adar2_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 27,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 5,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 12,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 19,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_nissan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 26,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 3,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 10,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 17,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 24,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 2,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 9,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 16,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 23,
                                               self.israel),
                         Sedrah.KORACH)

    def test_sivan_30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 30,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 7,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 14,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 21,
                                               self.israel),
                         Sedrah.MATTOS)

    def test_tammuz_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 28,
                                               self.israel),
                         Sedrah.MASSEY)

    def test_av_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 6,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 13,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 25,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestRoshHashonahTuesdayIsrael(unittest.TestCase):

    test_year = HebrewYear(5715)
    israel = True

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.VAYYELECH)

    def test_tishri5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 5,
                                               self.israel),
                         Sedrah.VAYYELECH)

    def test_tishri12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 12,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 19,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 26,
                                               self.israel),
                         Sedrah.BERESHITH)


class TestRoshHashonahTuesdayDiaspora(unittest.TestCase):

    test_year = HebrewYear(5715)
    israel = False

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.VAYYELECH)

    def test_tishri5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 5,
                                               self.israel),
                         Sedrah.VAYYELECH)

    def test_tishri12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 12,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 19,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 26,
                                               self.israel),
                         Sedrah.BERESHITH)


class TestPesachSundayLeapIsrael(unittest.TestCase):
    test_year = HebrewYear(5714)
    israel = True

    def test_adar1_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 17,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 24,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar2_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 1,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 8,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 15,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 22,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_adar2_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 29,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 7,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 14,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 21,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_nissan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 28,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 5,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 12,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 19,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 26,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 4,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 11,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 18,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 25,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 2,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 9,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 16,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 23,
                                               self.israel),
                         Sedrah.MATTOS)

    def test_av_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 1,
                                               self.israel),
                         Sedrah.MASSEY)

    def test_av_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 8,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 15,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 27,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachSundayLeapDiaspora(unittest.TestCase):
    test_year = HebrewYear(5714)
    israel = False

    def test_adar1_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 17,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 24,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar2_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 1,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 8,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 15,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 22,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_adar2_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 29,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 7,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 14,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 21,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_nissan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 28,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 5,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 12,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 19,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 26,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 4,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 11,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 18,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 25,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 2,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 9,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 16,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 23,
                                               self.israel),
                         Sedrah.MATTOS)

    def test_av_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 1,
                                               self.israel),
                         Sedrah.MASSEY)

    def test_av_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 8,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 15,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 27,
                                               self.israel),
                         Sedrah.NITZAVIM)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.VAYYELECH)


class TestPesachThursdayLeapIsrael(unittest.TestCase):
    test_year = HebrewYear(5719)
    israel = True

    def test_adar1_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 20,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 27,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar2_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 4,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 11,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 18,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 25,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 3,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 10,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 17,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 24,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_iyar_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 1,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 8,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 15,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 22,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 29,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 7,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 14,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 21,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 28,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 5,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 12,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 19,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 26,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 4,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 11,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 23,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestPesachThursdayLeapDiaspora(unittest.TestCase):
    test_year = HebrewYear(5719)
    israel = False

    def test_adar1_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 20,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar1_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 27,
                                               self.israel),
                         Sedrah.VAYYAKHEL)

    def test_adar2_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 4,
                                               self.israel),
                         Sedrah.PEKUDEY)

    def test_adar2_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 11,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_adar2_18(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 18,
                                               self.israel),
                         Sedrah.TZAV)

    def test_adar2_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_SHENI, 25,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 3,
                                               self.israel),
                         Sedrah.THAZRIA)

    def test_nissan_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 10,
                                               self.israel),
                         Sedrah.METZORA)

    def test_nissan_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 17,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_nissan_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 24,
                                               self.israel),
                         Sedrah.ACHAREY_MOS)

    def test_iyar_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 1,
                                               self.israel),
                         Sedrah.KEDOSHIM)

    def test_iyar_8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 8,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 15,
                                               self.israel),
                         Sedrah.BEHAR)

    def test_iyar_22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 22,
                                               self.israel),
                         Sedrah.BECHUKOSAI)

    def test_iyar_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 29,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 7,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 14,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 21,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_28(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 28,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_tammuz_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 5,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 12,
                                               self.israel),
                         Sedrah.CHUKKAS_BALAK)

    def test_tammuz_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 19,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 26,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_4(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 4,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_11(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 11,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 23,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestPesachTuesdayRegularIsrael(unittest.TestCase):
    """Tests a regular year where the first day of Pesach is Tuesday, in Israel.

    Also tests Rosh Hashonah on Saturday."""
    test_year = HebrewYear(5713)
    israel = True

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 2,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 7,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 8,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 9,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 15,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 29,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 30,
                                               self.israel),
                         Sedrah.NOACH)

    def test_adar_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 20,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 27,
                                               self.israel),
                         Sedrah.VAYYAKHEL_PEKUDEY)

    def test_nissan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 5,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 12,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 19,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 26,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 3,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 10,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 17,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 24,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_sivan_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 2,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 9,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 16,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 23,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 30,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 7,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 14,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 21,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_28_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 28,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 6,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 13,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 25,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)


class TestPesachTuesdayRegularDiaspora(unittest.TestCase):
    """Tests a regular year, first day of Pesach Tuesday, not Israel.

    Also tests Rosh Hashonah on Saturday."""
    test_year = HebrewYear(5713)
    israel = False

    def test_tishri1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 1,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 2,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 7,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri8(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 8,
                                               self.israel),
                         Sedrah.HAAZINU)

    def test_tishri9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 9,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri15(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 15,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri22(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 22,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 23,
                                               self.israel),
                         Sedrah.VZOTH_HABERACHAH)

    def test_tishri24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 24,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 29,
                                               self.israel),
                         Sedrah.BERESHITH)

    def test_tishri30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TISHRI, 30,
                                               self.israel),
                         Sedrah.NOACH)

    def test_adar_20(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 20,
                                               self.israel),
                         Sedrah.KI_THISSA)

    def test_adar_27(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ADAR_RISHON, 27,
                                               self.israel),
                         Sedrah.VAYYAKHEL_PEKUDEY)

    def test_nissan_5(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 5,
                                               self.israel),
                         Sedrah.VAYYIKRA)

    def test_nissan_12(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 12,
                                               self.israel),
                         Sedrah.TZAV)

    def test_nissan_19(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 19,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_nissan_26(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.NISSAN, 26,
                                               self.israel),
                         Sedrah.SHEMINI)

    def test_iyar_3(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 3,
                                               self.israel),
                         Sedrah.THAZRIA_METZORA)

    def test_iyar_10(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 10,
                                               self.israel),
                         Sedrah.ACHAREY_KEDOSHIM)

    def test_iyar_17(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 17,
                                               self.israel),
                         Sedrah.EMOR)

    def test_iyar_24(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.IYAR, 24,
                                               self.israel),
                         Sedrah.BEHAR_BECHUKOSAI)

    def test_sivan_2(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 2,
                                               self.israel),
                         Sedrah.BEMIDBAR)

    def test_sivan_9(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 9,
                                               self.israel),
                         Sedrah.NASO)

    def test_sivan_16(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 16,
                                               self.israel),
                         Sedrah.BEHAALOSECHA)

    def test_sivan_23(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 23,
                                               self.israel),
                         Sedrah.SHELACH_LECHA)

    def test_sivan_30(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.SIVAN, 30,
                                               self.israel),
                         Sedrah.KORACH)

    def test_tammuz_7(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 7,
                                               self.israel),
                         Sedrah.CHUKKAS)

    def test_tammuz_14(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 14,
                                               self.israel),
                         Sedrah.BALAK)

    def test_tammuz_21(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 21,
                                               self.israel),
                         Sedrah.PINCHAS)

    def test_tammuz_28_1(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.TAMMUZ, 28,
                                               self.israel),
                         Sedrah.MATTOS_MASSEY)

    def test_av_6(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 6,
                                               self.israel),
                         Sedrah.DEVARIM)

    def test_av_13(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.AV, 13,
                                               self.israel),
                         Sedrah.VAETHCHANAN)

    def test_ellul_25(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 25,
                                               self.israel),
                         Sedrah.NITZAVIM_VAYYELECH)

    def test_ellul_29(self):
        self.assertEqual(self.test_year.sedrah(HebrewMonth.ELLUL, 29,
                                               self.israel),
                         Sedrah.HAAZINU)
