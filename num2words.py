import math

within20 = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

orders = {
    3: "thousand",
    6: "million",
    9: "billion",
    12: "trillion",
    15: "quadrillion",
    18: "quintillion",
}

def num2words(num: int) -> str:
    """ Handles everything else """
    if num < 0:
        return f"negative {num2word(-num)}"

    if num <= 999:
        return _num2word(num)
    
    order = math.floor(math.floor(math.log10(num))/3) * 3

    first3 = num // (10 ** order)
    rest = num - first3 * 10 ** order

    postfix = orders[order]

    if rest == 0:
        return f"{num2word(first3)} {postfix}" 
    else:
        return f"{num2word(first3)} {postfix} {num2word(rest)}"

def _num2words(num: int) -> str:
    """ Handles 0-999 """
    assert num >= 0

    if num <= 19:
        return within20[num - 1]

    elif num <= 99:
        ten, rest = divmod(num, 10)
        if rest == 0:
            return f"{tens[ten]}"
        else:
            return f"{tens[ten]} {_num2word(rest)}"

    elif num <= 999:
        hundreds, rest = divmod(num, 100)
        if rest == 0:
            return f"{_num2word(hundreds)} hundred"
        else:
            return f"{_num2word(hundreds)} hundred {_num2word(rest)}"
