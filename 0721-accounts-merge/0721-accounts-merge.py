class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}

    def find(self, node):
        if node not in self.par:
            self.par[node] = node
            self.rank[node] = 0
            return node

        if self.par[node] == node:
            return node

        parent = self.par[node]
        self.par[node] = self.find(parent)
        return self.par[node]

    def union(self, n1, n2):
        par1, par2 = self.find(n1), self.find(n2)

        if self.rank[par1] > self.rank[par2]:
            self.rank[par1] += 1
            self.par[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.rank[par2] += 1
            self.par[par1] = par2
        else:
            self.rank[par1] += 1
            self.par[par2] = par1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # union find to union based on emails
        # how should we decide which the parent is?

        uf = UnionFind()
        email_to_name = {}
        for account in accounts:
            main_email = account[1]
            email_to_name[main_email] = account[0]
            for emails in account[2:]:
                uf.union(main_email, emails)
                email_to_name[emails] = account[0]

        res = []
        grouped_emails = defaultdict(list)
        for email in email_to_name:
            parent_email = uf.find(email)
            grouped_emails[parent_email].append(email)

        #print(uf.par)
        for parent_email in grouped_emails.keys():
            current = []
            #current.append(email_to_name[parent_email])
            current.append(parent_email)
            for email in grouped_emails[parent_email]:
                if email != parent_email:
                    current.append(email)
            res.append([email_to_name[parent_email]] + sorted(current))
        
        return res

        