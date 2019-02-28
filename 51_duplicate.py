# coding: utf-8


def duplicate(nums):
    length = len(nums)

    for i in xrange(length):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]:
                return nums[i]
            a, b = i, nums[i]
            nums[a], nums[b] = nums[b], nums[a]

    return -1


if __name__ == '__main__':
    print duplicate([2, 3, 1, 0, 2, 5, 3])