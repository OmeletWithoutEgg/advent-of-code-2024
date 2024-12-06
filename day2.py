def good(l, tolerance = 1):
    if tolerance < 0:
        return False
    for i in range(1, len(l)):
        diff = l[i] - l[i - 1]
        if diff <= 0 or diff > 3:
            l1 = l[:i] + l[i+1:]
            l2 = l[:i-1] + l[i:]
            return good(l1, tolerance - 1) or good(l2, tolerance - 1)
    return True

with open('day2.in', 'r') as f:
    ans = 0
    for line in f.readlines():
        l = list(map(int, line.split()))
        if good(l) or good(l[::-1]):
            ans += 1
    print(ans)
