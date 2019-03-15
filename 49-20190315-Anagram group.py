def groupAnagrams(strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key,[]) + [w]
    return d.values()


a=['abc','bac','cba','edf']
b=groupAnagrams(a)
print(b)
