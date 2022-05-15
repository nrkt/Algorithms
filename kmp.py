"""
ref: https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/kmp_algorithm
ref: https://tjkendev.github.io/procon-library/python/string/kmp.html
"""
class KMP():
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.table = self.create_table()
        self.indices = self.search()
    
    def create_table(self):
        table = [0] * len(self.pattern)
        i = 0
        for j in range(1, len(self.pattern)):
            if self.pattern[j] == self.pattern[i]:
                i += 1
                table[j] = i
            else:
                table[j] = i
                i = 0
        return table
    
    def search(self):
        matched_indices = []
        i = j = 0
        while i < len(self.text):
            if self.text[i] == self.pattern[j]:
                i += 1
                j += 1
                if j == len(self.pattern):
                    matched_indices.append(i-j)
                    j = self.table[j-1]
            else:
                j = self.table[j]
        return matched_indices

kmp = KMP("aaaabcaaaa", "abc")
print(kmp.indices) # [3]
