
def task1(nums):
    return sum(x ** 2 for x in nums)


def task2(nums):
    avg = sum(nums) / len(nums)
    return sum(x for x in nums if x >= avg)


def task3(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return sorted(nums, key=lambda x: (-frequency[x], x))


def task4(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)


def task5(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


def task6(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


def task8(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def task10(points, k):
    points.sort(key=lambda point: point[0]**2 + point[1]**2)
    return points[:k]