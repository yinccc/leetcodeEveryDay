class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        mask = 1
        distance = 0
        for i in range(32):
            if ((xor & mask) == mask):
                distance += 1
            mask = mask << 1
        return distance
