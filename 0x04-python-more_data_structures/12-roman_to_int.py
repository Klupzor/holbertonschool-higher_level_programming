#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = list(roman_string)
        nums = list(map(lambda key: rom[key], n))
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i] = nums[i] * - 1
        return sum(nums)
