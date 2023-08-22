class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isalpha():
                letter_logs.append((identifier, content))
            else:
                digit_logs.append(log)
        letter_logs.sort(key=lambda x: (x[1], x[0]))

        result = []
        for id, content in letter_logs:
            result.append(id + " " + content)
        return result + digit_logs


# O(nlogn)

testInputs = [
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
    ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
]
for n in testInputs:
    print(Solution().reorderLogFiles(n))
