from ui.cinsole import filename,word,new_word
def replace(filename, word, new_word):
    f = open(filename, 'r')
    count = 0
    for line in f:
        words = line.split(' ')
        for i in range(len(words)):
            if word == words[i]:
                count += 1
                words[i] = words[i].replace(word, new_word)

    if count==0:
        print('das Wort wurde nicht ersätzt')

    f= open(filename,'w')
    f.write(' '.join(words))

    f.close()
    print(f"Ersetzt {word} durch {new_word} an {count} Stellen.")