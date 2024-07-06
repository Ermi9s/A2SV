class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        visits = {}

        for cp in cpdomains:
            num , domain = cp.split()
            num = int(num)
       

            visits[domain] = visits.get(domain , 0) + num
            
            for i in range(len(domain)):
                if domain[i] == ".":
                    visits[domain[i+1:]] = visits.get(domain[i+1:] , 0) + num

            
            
        
        for i in visits.keys():
            ans.append(f"{visits[i]} {i}")


        return ans
        