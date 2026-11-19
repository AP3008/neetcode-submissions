class UnionFind:
    def __init__(self, n):
        # Each index corresponds to the account index, and the value at the index in the union find is the parent. 
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        # While the parent of x is not itself, i.e we are looking for the root parent of x, we want to search for the parent. 
        while x != self.par[x]:
            # Path compression, to get rid of redundant work we set the parent as the parent of the parent. This works because once we reach the root, the roots parent will be itself, so we won't get any errors or skip anything. 
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x 
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True 
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # We need to implement a union find 
        # We can use a hashmap of emails that are mapped to an accounts index, If we see an email that

        uf = UnionFind(len(accounts)) 
        emailToAcc = {} # email -> index of acc
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        emailGroup = defaultdict(list)
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res 
        