
def radix_sort(unSortedList):
    maxCipher = len(unSortedList)
    mod = 10
    div = 1

    while True:
        buckets = [[], [], [], [], [], [], [], [], [], []]

        for val in unSortedList:
            least_digit = val % mod
            least_digit //= div
            buckets[least_digit].append(val)
        mod = mod * 10
        div = div * 10

        if len(buckets[0]) == maxCipher:
            return buckets[0]
        unSortedList = []
        for b in buckets:
            for num in b:
                unSortedList.append(num)

data = [ 2, 10, 111, 565, 800 ]
print(radix_sort(data))

pass
