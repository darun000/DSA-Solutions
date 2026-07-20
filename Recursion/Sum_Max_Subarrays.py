# Python implementation to find sum of max
# of subarrays by generating all subarrays

def sumOfMax(arr):
    n = len(arr)
    res = 0

    # Pick starting point of subarray
    for i in range(n):
        currMax = arr[i]

        # Pick ending point
        for j in range(i, n):
            # Max of subarray from i to j
            currMax = max(currMax, arr[j])

            res += currMax

    return res


if __name__ == "__main__":
    arr = [1, 3, 2]
    print(sumOfMax(arr))