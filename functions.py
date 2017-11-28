def replace_letter(word,letter1,letter2):
    n = 0
    new_word = ""
    for count in range(0,len(word)):
        if word[n] == letter1:
            new_word = new_word + letter2
            n += 1
        else:
            new_word = new_word + word[n]
            n += 1
    return new_word
#////////////////////////////////////////////////////////////////////////////
def switch_letters(word,letter1,letter2):
    n = 0
    new_word = ""
    for count in range(0,len(word)):
        if word[n] == letter1:
            new_word = new_word + letter2
            n += 1
        elif word[n] == letter2:
            new_word = new_word + letter1
            n += 1
        else:
            new_word = new_word + word[n]
            n += 1
    return new_word
#////////////////////////////////////////////////////////////////////////////