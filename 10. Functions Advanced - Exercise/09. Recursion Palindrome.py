def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    # правим проверка дали първия индекс е равен на последния и после дали втория е равен на предпоследния и т.н.
    first, last = word[idx], word[-1 -idx]
    if first != last:
        return f"{word} is not a palindrome"

    idx += 1
    return palindrome(word, idx)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
