from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

my_dict = {
    'rose': {'r': 0, 'o': 0, 's': 0, 'e': 0},
    'tulip': {'t': 0, 'u': 0, 'l': 0, 'i': 0, 'p': 0},
    'lotus': {'l': 0, 'o': 0, 't': 0, 'u': 0, 's': 0},
    'daffodil': {'d': 0, 'a': 0, 'f': 0, 'f': 0, 'o': 0, 'd': 0, 'i': 0, 'l': 0}
}

while len(vowels) > 0 and len(consonants) > 0:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for k, v in my_dict.items():
        for ch in v:
            if ch == vowel or ch == consonant:
                v[ch] = 1

    for k, v in my_dict.items():
        ready = True
        for ch in v:
            if v[ch] == 0:
                ready = False
                break

        if ready:
            print(f"Word found: {k}")
            if len(vowels) > 0:
                print(f"Vowels left: {' '.join(vowels)}")
            if len(consonants) > 0:
                print(f"Consonants left: {' '.join(consonants)}")
            break

    if ready:
        break

if not ready:
    print("Cannot find any word!")
    if len(vowels) > 0:
        print(f"Vowels left: {' '.join(vowels)}")
    if len(consonants) > 0:
        print(f"Consonants left: {' '.join(consonants)}")


# o e a o e a i
# p r s x r

# a a a
# x r l t p p

# u a o i u y o e
# p m t l

