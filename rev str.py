def revStr(s):
    l = 0
    h = len(s) - 1
    global flag
    flag = 1
    rev = ["0"] * len(s)
    while l <= h:
        if not (ord(s[l]) >= 97 and ord(s[l]) <= 122) or (
            ord(s[l]) >= 65 and ord(s[l]) <= 90
        ):
            rev[l] = s[l]
            l += 1
        if not (ord(s[h]) >= 97 and ord(s[h]) <= 122) or (
            ord(s[h]) >= 65 and ord(s[h]) <= 90
        ):
            rev[h] = s[h]
            h -= 1
        rev[l], rev[h] = s[h], s[l]
        l += 1
        h -= 1
    print("".join(rev))


s = "h@e$llo"
revStr(s)
