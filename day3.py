import re

with open('day3.in', 'r') as f:
    s = f.read().strip()

r = re.compile(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)')

ans = 0
enabled = True
for m in r.finditer(s):
    print(m.group())
    print(m.groups())
    if m.group(1):
        enabled = True
    elif m.group(2):
        enabled = False
    else:
        a = m.group(3)
        b = m.group(4)
        if enabled:
            ans += int(a) * int(b)
    # a = m.group(1)
    # b = m.group(2)
    # ans += int(a) * int(b)
print(ans)
