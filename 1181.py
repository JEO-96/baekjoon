import sys

N = int(sys.stdin.readline())
words = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_len = len(word)
    words.append((word, word_len))

words = list(set(words))
words.sort(key=lambda x: (x[1], x[0]))
for i in words:
    print(i[0])
