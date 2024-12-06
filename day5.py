def check(rules, v):
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if (v[j], v[i]) in rules:
                return False
    return True

def sort_by(rules, v):
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if (v[j], v[i]) in rules:
                v[j], v[i] = v[i], v[j]

ans = 0
rules = set()
while s := input():
    if '|' in s:
        a, b = map(int, s.split('|'))
        rules.add((a, b))

while s := input():
    v = list(map(int, s.split(',')))
    if not check(rules, v):
        sort_by(rules, v)
        ans += v[len(v)//2]

print(ans)
