def solve(arr):
    arr = sorted(int(m[:2]) * 60 + int(m[3:]) for m in set(arr))
    print(arr)
    arr += [arr[0] + 1440]
    o = []
    print(arr)
    for i in range(len(arr)-1):
        print(arr[5])
        o.append(arr[i+1] - arr[i])
    print (o)
    h, m = divmod(max(arr[i + 1] - arr[i] - 1 for i in range(len(arr) - 1)), 60)
    print(h,m)
    return "{:03}:{:03}".format(h, m)
print(solve(["21:14", "15:34", "14:51", "06:25", "15:30"]))
