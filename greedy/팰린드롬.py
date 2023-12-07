words = input()
words = sorted(words)
words_copy = sorted(words)

odd_word = []
result = []
for word in words_copy:
    if words_copy.count(word) % 2 == 1 and word not in odd_word:
        temp = word
        odd_word.append(temp)
        words.remove(word)
        words.append(temp)

if len(odd_word) > 1:
    print("I'm Sorry Hansoo")
else:
    if len(odd_word):
        for index in range(0, len(words), 2):
            result.append(words[index])
        result.extend(words[len(words) - 2: 0: -2])

    else:
        for index in range(0, len(words), 2):
            result.append(words[index])
        result.extend(words[len(words) - 1: 0: -2])

    print("".join(result))
