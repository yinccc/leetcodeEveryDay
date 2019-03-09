def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # ----------------88ms-------------------
    max_len = 0
    cur = ''  # save the new substring
    for item in s:
        if item in cur:
            item_index = cur.index(item)
            cur = cur[item_index + 1:] + item
        else:
            cur += item
        max_len = max(max_len, len(cur))
    return max_len


a=lengthOfLongestSubstring('abcdabcdeabcdef')