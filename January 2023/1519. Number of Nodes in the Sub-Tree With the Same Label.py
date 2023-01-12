class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        tree = defaultdict(list)

        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        output = [0]*n
        seen = set()

        def dfs(node):
            count = Counter(labels[node])
            for i in tree[node]:
                if i in seen:
                    continue
                seen.add(node)
                count += dfs(i)
            output[node] = count[labels[node]]
            return count
        dfs(0)

        return output
