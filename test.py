def countPairs(arr, n):
    mp = dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    ans = 0
    for it in mp:
        count = mp[it]
        ans += (count * (count - 1))
    return ans

N = int(input())
arr = list(map(int, input().split()))

leng = len(arr)
for idx, x in enumerate(arr):
    temp = x
    arr[idx] = 0
    print(countPairs(arr, leng))
    arr[idx] = temp