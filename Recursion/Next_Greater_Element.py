def nextLargerElement(arr):
    n = len(arr)
    res = [-1] * n

    # Iterate through each element in the array
    for i in range(n):

        # Check for the next greater element
        # in the rest of the array
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break

    return res

if __name__ == "__main__":
    arr = [6, 8, 0, 1, 3]

    res = nextLargerElement(arr)
    print(" ".join(map(str, res)))