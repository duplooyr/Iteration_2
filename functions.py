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
def switch_words(sentence,word1,word2):
    n = 0
    new_sentence = ""
    for count in range(0,len(sentence)-len(word1 + word2)+2):

        if sentence[n:n+len(word1)] == word1:
            new_sentence = new_sentence + word2
            n += len(word1)

        elif sentence[n:n+len(word2)] == word2:
            new_sentence = new_sentence + word1
            n += len(word2)

        else:
            new_sentence = new_sentence + sentence[n]
            n +=1

    return  new_sentence
#////////////////////////////////////////////////////////////////////////////
def censor_words(sentence):
    n = 0
    new_sentence = ""
    bad_words = ["cat","orange","vegetable","yellow"]
    good_words = ["Dog", "Not Orange", "Fruit", "Not Yellow"]
    for count in range(0,len(sentence):
        if sentence[n] == bad_words[1,2,3,4]