def print_upper_words(words,letters):
    """ print words in uppercase in words that starts any letter in letters 

       # for example:
       print_upper_words(["hello","happy","hey","funny","sunny"],["h","s"])

       this should print "HELLO","HAPPY","HEY","SUNNY"

    """

    # CODE STARTS HERE:

    upper_words =[]
    upper_letters = []
    for word in words:
        upper_words.append(word.upper())
    for letter in letters:
        upper_letters.append(letter.upper())

    for word in upper_words:
        for letter in upper_letters:
            if word.startswith(letter):
                print(word)


print_upper_words(["hello","happy","hey","funny","sunny"],["h","f"])