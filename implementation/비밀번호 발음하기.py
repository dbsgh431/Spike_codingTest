import sys

vowels = ['a', 'e', 'i', 'o', 'u']


def print_acceptable(flag: bool):
    if flag:
        print("<" + words + ">", "is acceptable.")
    else:
        print("<" + words + ">", "is not acceptable.")


while True:
    words = sys.stdin.readline().rstrip()
    is_acceptable = False

    continuous_words = []
    if words == "end":
        exit()

    for v in vowels:
        if v in words:
            is_acceptable = True
            break

    for i in range(1, len(words)):
        if i >= 2:
            if (words[i] in vowels and words[i - 1] in vowels and words[i - 2] in vowels) or (
                    words[i] not in vowels and words[i - 1] not in vowels and words[i - 2] not in vowels):
                is_acceptable = False
                break

        if words[i] != 'e' and words[i] != 'o':
            if words[i] == words[i - 1]:
                is_acceptable = False
                break

    if is_acceptable:
        print_acceptable(is_acceptable)
    else:
        print_acceptable(is_acceptable)