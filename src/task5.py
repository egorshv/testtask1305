from typing import List, Optional


def join(s1: str, s2: str) -> Optional[str]:
    if s1 == s2:
        return

    if len(s1) >= len(s2):
        i = len(s1) - len(s2)
        j = len(s2) - 1
    else:
        i = 0
        j = len(s2) - len(s1) + 1

    while i < len(s1) and j >= 0:
        if s1[i:] == s2[:j + 1]:
            return s1 + s2[j + 1:]
        i += 1
        j -= 1


def handle_file(filename: str, word: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.readlines()

    result = []
    for i in range(len(words)):
        joined_word = join(word, words[i].strip())
        result.append(joined_word)

    return [word for word in result if word]


if __name__ == '__main__':
    words = handle_file('test.txt', 'ласты')
    words1 = handle_file('test.txt', 'кабала')
    words2 = handle_file('test.txt', 'стыковка')
    print(f'words 1: {words}')
    print()

    print(f'words 2: {words1}')
    print()

    print(f'words 3: {words2}')
    print()
