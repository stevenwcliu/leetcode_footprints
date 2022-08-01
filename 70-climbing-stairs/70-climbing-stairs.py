class Solution:
    def climbStairs(self, n):
    # nc: bottom up dp
        one, two = 1, 1

        for i in range(n - 1):
            temp = one # store one in a temp var before updating it
            one = one + two # adding the two prev vals
            # update one before shifting two
            two = temp

        return one # return where one lands on
        