def longestCommonPrefix(strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    print(ss)
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

if __name__ == '__main__':
    print(longestCommonPrefix(['abc', 'abd', 'abc']))