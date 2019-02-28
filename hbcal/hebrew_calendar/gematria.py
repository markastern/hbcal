from .hebrew_letters import HEBREW_LETTERS

HUNDREDS = ['', HEBREW_LETTERS['QOF'], HEBREW_LETTERS['RESH'],
            HEBREW_LETTERS['SHIN']]

TENS = ['', HEBREW_LETTERS['YOD'], HEBREW_LETTERS['KAF'],
        HEBREW_LETTERS['LAMED'], HEBREW_LETTERS['MEM'], HEBREW_LETTERS['NUN'],
        HEBREW_LETTERS['SAMECH'], HEBREW_LETTERS['AYIN'],
        HEBREW_LETTERS['PE'], HEBREW_LETTERS['TZADE']]

UNITS = ['', HEBREW_LETTERS['ALEF'], HEBREW_LETTERS['BET'],
         HEBREW_LETTERS['GIMEL'], HEBREW_LETTERS['DALET'],
         HEBREW_LETTERS['HE'], HEBREW_LETTERS['VAV'], HEBREW_LETTERS['ZAYIN'],
         HEBREW_LETTERS['CHET'], HEBREW_LETTERS['TET']]


def to_letters(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(
            "invalid positive integer: {value}".format(value=value))
    quotient, value = divmod(value, 400)
    result = HEBREW_LETTERS['TAV'] * quotient

    quotient, value = divmod(value, 100)
    result += HUNDREDS[quotient]

    quotient, value = divmod(value, 10)
    if quotient == 1 and value in (5, 6):
        result += HEBREW_LETTERS['TET']
        value += 1
    else:
        result += TENS[quotient]
    result += UNITS[value]
    if len(result) == 1:
        return result + HEBREW_LETTERS['GERESH']
    else:
        return result[:-1] + HEBREW_LETTERS['GERSHAYIM'] + result[-1]
