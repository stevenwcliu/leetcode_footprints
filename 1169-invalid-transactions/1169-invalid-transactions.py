# class Solution:
#     def invalidTransactions(self, trans: List[str]) -> List[str]:
#         # ref: https://bhanga-manish.github.io/LeetCode-1169.-Invalid-Transactions/
        
#         # print("trans: ", trans)
#         records = []
#         res = []
        
#         # split the string into individual components
#         for t in trans:
#             # string manipulation
#             rec = t.split(',')
#             # convert the first two elements to int
#             rec[1] = int(rec[1])
#             rec[2] = int(rec[2])
#             records.append(rec)
        
#         # print("records: ", records)
        
#         for rec in records:
#             if rec[2] > 1000:
#                 # covert back to str before putting into res
#                 rec[1] = str(rec[1])
#                 rec[2] = str(rec[2])
#                 res.append(','.join(rec))
#                 continue
#             for x in records:
#                 if rec[0] == x[0] and abs(rec[1] - int(x[1])) <= 60 and rec[3] != x[3]:
#                     rec[1] = str(rec[1])
#                     rec[2] = str(rec[2])
#                     res.append(','.join(rec))
#                     break
        
#         return res

'''
ref: https://leetcode.cn/problems/invalid-transactions/solution/zhi-jie-ji-suan-liang-chong-qing-kuang-ji-ke-by-ti/

解题思路
遍历当前交易，如果和后面的交易冲突，记录，跳出（剪枝）
'''
# class Solution:
#     def invalidTransactions(self, transactions: List[str]) -> List[str]:
#         transactions=[i.split(",") for i in transactions]
#         print(transactions)
#         res=[]
#         for i,v in enumerate(transactions):
#             print("i: ", i, ", v: ", v)
#             if int(v[2])>1000:
#                 res.append(",".join(v))
#                 continue
#             for j,u in enumerate(transactions):
#                 if i==j:
#                     continue
#                 if v[0]==u[0] and v[3]!=u[3] and abs(int(v[1])-int(u[1]))<=60:
#                     res.append(",".join(v))
#                     break
#         return res 

class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions):
        transactions = [Transaction(*transaction.split(',')) for transaction in transactions]
        transactions.sort(key=lambda t: t.time) # O(nlogn) time

        trans_indexes = defaultdict(list)
        for i, t in enumerate(transactions): # O(n) time
            trans_indexes[t.name].append(i)

        res = []
        for name, indexes in trans_indexes.items(): # O(n) time
            left = right = 0
            for i, t_index in enumerate(indexes):
                t = transactions[t_index]
                if (t.amount > 1000):
                    res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                    continue
                while left <= len(indexes)-2 and transactions[indexes[left]].time < t.time - 60: # O(60) time
                    left += 1
                    
                print("left:", left)
                while right <= len(indexes)-2 and transactions[indexes[right+1]].time <= t.time + 60: # O(60) time
                    right += 1
                print("right:", right)
                for i in range(left,right+1): # O(120) time
                    if transactions[indexes[i]].city != t.city:
                        res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                        break

        return res