class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        curr = []
        nex = []
        for i in range(len(paths)):
            curr.append(paths[i][0])
            nex.append(paths[i][1])
        c = paths[0][0]
        while(nex[curr.index(c)] in curr):
            c = nex[curr.index(c)]
        return nex[curr.index(c)]