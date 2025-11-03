# linear search
def linear(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return True

    return False


arrayHellow = ["a", "a", "a", "a", "a", "a", "h"]

print(linear("klsjalglkash", "h"))
print(linear(arrayHellow, "b"))

#binary search
def binarySearch(arr, lo, hi, n):
    while lo <= hi:
        m = lo + (hi - lo) // 2
        v = arr[m]

        if v == n:
            return m
        elif v < n:
            lo = m + 1
        else:
            hi = m - 1

    return -1  # not found


arr = [1, 3, 5, 7, 9, 11]
index = binarySearch(arr, 1, len(arr) - 1, 7)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

    
