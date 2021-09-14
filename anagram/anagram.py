def find_anagrams(word, candidates):
    letters = list(word)
    for candidate in candidates:
        can_letters = list(candidate)
        correct = 1
        for can_letter in can_letters:
            if can_letter not in letters:
                correct = 0
        for letter in letters:
            if letter not in can_letter:
                correct == 0
        if correct == 1:
            return candidate

