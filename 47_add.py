# coding: utf-8


def add(self, num1, num2):
    while num2:
        result = (num1 ^ num2) & 0xffffffff
        carry = ((num1 & num2) << 1) & 0xffffffff
        num1 = result
        num2 = carry
        
    if num1 <= 0x7fffffff:
        result = num1
        
    else:
        result = ~(num1 ^ 0xffffffff)
        
    return result


if __name__ == '__main__':
    print add(5, 17)
    print add(142, 5312)
    print add(1421, -43)
