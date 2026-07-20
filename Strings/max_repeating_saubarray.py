# Python program to find the maximum consecutive
# repeating character in given string

# Function to find out the maximum repeating
# character in given string
def maxRepeating(s):
    n = len(s)
    maxCnt = 0
    res = s[0]

    # Find the maximum repeating character
    # starting from s[i]
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if s[i] != s[j]:
                break
            cnt += 1

        # Update result if required
        if cnt > maxCnt:
            maxCnt = cnt
            res = s[i]

    return res

if __name__ == "__main__":
    s = "aaaabbaaccde"
    print(maxRepeating(s))