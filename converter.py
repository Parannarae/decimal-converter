import argparse
from typing import List

def convert_from_dec(target_value: int, base_num: int) -> List[int]:
    """Convert decimal value target_value to n-ary number (represented by base_num).

    Result of the conversion will be a list of integer representing the value of each position in base_num number system
    where the most significant value to be the leftmost.

    e.g. converting 14 (decimal 14) to 112 (ternary 14) will result:
        [1, 1, 2]
    
    Args:
        target_value: a decimal value to convert
        base_num: radix of the number system target_value would convert to
    
    Returns:
        List of integer representing the value of each position in base_num number system
    """
    res = []
    cur_num = target_value
    while cur_num > base_num:
        remainder = cur_num % base_num
        quotient = cur_num // base_num

        res.append(remainder)
        cur_num = quotient

    # append last remainder
    res.append(cur_num)

    return reversed(res)


def get_nary_str_representation(nary_val_list: List[int]) -> str:
    """Return string which conncatnate the values in nary_val_list
    
    Args:
        nary_val_list: List of integer representing n-ary system value
    
    Returns:
        n-ary system value in string
    """
    return ''.join(str(val) for val in nary_val_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert decimal value to n-ary value")
    parser.add_argument(
        'target_value',
        type=int,
        help="A value to convert to the new number system."
    )
    parser.add_argument(
        '-b',
        dest='base',
        default=10,
        type=int,
        help="A base number (radix) for the converting number system. If not given, it will be 10 as the default."
    )
    args = parser.parse_args()
    print(f"Converting {args.target_value} to new number system with the base {args.base}...")
    res = convert_from_dec(args.target_value, args.base)
    print(f"The result is {get_nary_str_representation(res)}")