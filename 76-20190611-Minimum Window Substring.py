import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        dict_t = collections.Counter(t)

        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0
        formed = 0
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1
            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.Counter(t)
        window = {}
        l, r = 0, 0
        res = float('inf'), 0, 0
        form, require = 0, len(dic)
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in dic and window[char] == dic[char]:
                form += 1
            while l <= r and form == require:
                char = s[l]
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                window[char] -= 1
                if char in dic and window[char] < dic[char]:
                    form -= 1
                l += 1
            r += 1
        return '' if res[0] == float('inf') else s[res[1]:res[2] + 1]