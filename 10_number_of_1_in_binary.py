# coding: utf-8


def number_of_1_in_binary(num):
    res = 0
    
    while num:
        res += 1
        num &= (num - 1)
    
    return res


if __name__ == "__main__":
    print number_of_1_in_binary(123123123)