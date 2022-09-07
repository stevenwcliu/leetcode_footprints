class Solution:
    def invalidTransactions(self, trans: List[str]) -> List[str]:
        # ref: https://bhanga-manish.github.io/LeetCode-1169.-Invalid-Transactions/
        
        # print("trans: ", trans)
        records = []
        res = []
        
        # split the string into individual components
        for t in trans:
            # string manipulation
            rec = t.split(',')
            # convert the first two elements to int
            rec[1] = int(rec[1])
            rec[2] = int(rec[2])
            records.append(rec)
        
        # print("records: ", records)
        
        for rec in records:
            if rec[2] > 1000:
                # covert back to str before putting into res
                rec[1] = str(rec[1])
                rec[2] = str(rec[2])
                res.append(','.join(rec))
                continue
            for x in records:
                if rec[0] == x[0] and abs(rec[1] - int(x[1])) <= 60 and rec[3] != x[3]:
                    rec[1] = str(rec[1])
                    rec[2] = str(rec[2])
                    res.append(','.join(rec))
                    break
        
        return res
        