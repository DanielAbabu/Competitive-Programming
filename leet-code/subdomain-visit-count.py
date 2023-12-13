class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_pair = {}

        for i in cpdomains:
            num,domain = map(str,i.split(" "))
            num = int(num)
            domains = domain.split(".")
            
            count_pair [domain] = count_pair.get(domain,0) + num
            if len(domains) >= 2:
                count_pair [".".join(domains[1:])] = count_pair.get(".".join(domains[1:]),0) + num
            if len(domains) == 3:
                count_pair [domains[-1]] = count_pair.get(domains[-1],0) + num
        answer = []

        for key,value in count_pair.items():
            answer.append(str(value)+ " " + key)

        return answer

     