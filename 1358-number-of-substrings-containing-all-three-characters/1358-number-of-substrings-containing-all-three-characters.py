# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         l = res = 0
#         char_freq = {}
#         # hm = {x:0 for x in "abc"}
#         # print(hm)
        
#         # abc 
#         # bca
#         # cab
#         # abc
#         for r in range(len(s)):
#             char = s[r]
#             if char not in char_freq:
#                 char_freq[char] = 0
#             char_freq[char] += 1
            
#             # while all(char_freq.values()):
             
#             print(char_freq)
#             if len(char_freq) == 3:
#                 res += 1
#                 print("res: ", res)
#             # when to shrink? when r reach the end?
        
#         return res
    

# ref: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/2526889/Python-sliding-window-solution-with-Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # count = collections.Counter()
        # print(count)
        char_freq = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] not in char_freq:
                char_freq[s[r]] = 0
            
            char_freq[s[r]] += 1

            while len(char_freq) == 3 and min(char_freq.values()) >= 1:
                res += len(s) - r
                char_freq[s[l]] -= 1
                if char_freq[s[l]] == 0:
                    del char_freq[s[l]]
                l += 1
            r += 1
        return res


# ref: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/1732848/Python-Sliding-Window-approach-with-explanation
# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         string = "abc"
#         char_count = {}
#         window_start = 0
#         matched = 0
#         total = 0
        
#         for char in string:
#             # keep a count of all characters in a hashmap
#             if char not in char_count:
#                 char_count[char] = 0
#             char_count[char] += 1
#         print(char_count)
			
#         # When we find a character that matahes the one in the dictionary, we reduce the count in the dictionary 
# 		# by moving the right pointer forward. We increase count of matched when the count of character is 0
		
#         for window_end in range(len(s)):
#             char_right = s[window_end]
#             char_count[char_right] -= 1
#             if char_count[char_right] == 0:
#                 matched += 1
                
#            # the left moves the window forward and puts back the character in the dictionary. We keep a count 
# 		   # of all substrings in total.
		   
#             while matched == len(string):
#                 if matched == len(char_count):
#                      total += len(s) - window_end
#                 char_left = s[window_start]
#                 if char_count[char_left] == 0:
#                     matched -= 1
#                 char_count[char_left] += 1
#                 window_start += 1
                
#         return total