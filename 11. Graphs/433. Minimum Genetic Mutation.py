from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        q = deque([(start, 0)])

        while q:
            gene, mut = q.popleft()
            if gene == end:
                return mut

            for i in range(len(gene)):
                for ch in "ACGT":
                    tmpgene = gene[:i] + ch + gene[i + 1 :]
                    if tmpgene in bank:
                        q.append((tmpgene, mut + 1))
                        bank.remove(tmpgene)
        return -1


testInputs = [
    ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],
    ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]],
]
for startGene, endGene, bank in testInputs:
    print(Solution().minMutation(startGene, endGene, bank))
