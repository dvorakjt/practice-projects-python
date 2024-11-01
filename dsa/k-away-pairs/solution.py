def count_pairs(nums, k):
    """Counts pairs of numbers that are k apart in a list of unique integers"""
    seen_nums = set()
    pair_count = 0

    for num in nums:
        if num - k in seen_nums:
            pair_count += 1
        if num + k in seen_nums:
            pair_count += 1
        seen_nums.add(num)

    return pair_count

pairs = [1, 7, 5, 9, 2, 12, 3]

print(count_pairs(pairs, 2))