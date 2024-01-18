""" O(n * log n) with two pointers"""

arr = [1, 2, 3, 5, 11]
arr1 = [3, 4, 7, 12, 33, 45]

n = len(arr)
m = len(arr1)
res = []

i = j = 0

while i < n and j < m:
    if arr[i] < arr1[j]:
        res.append(arr[i])
        i += 1
    else:
        res.append(arr1[j])
        j += 1

if n > i:
    res.extend(arr[i:])

if m > j:
    res.extend(arr1[j:])

if __name__ == "__main__":
    print(res)
