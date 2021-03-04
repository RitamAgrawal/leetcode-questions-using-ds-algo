class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_map = collections.Counter()
        for domain in cpdomains:
            count, dom = domain.split(" ")
            val = int(count)
            dom_array = dom.split(".")
            for i in range(len(dom_array)):
                hash_map[".".join(dom_array[i:])] += val
        return ["{} {}".format(ct,dom) for dom,ct in hash_map.items()]       
        