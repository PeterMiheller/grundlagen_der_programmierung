from ui.cinsole import filename,word,new_word
def replace(filename, word, new_word):
    with open(filename, 'r') as f:
        lines = f.readlines()

    count = 0
    modified_lines = []
    for line in lines:
        words = line.split(' ')
        for i in range(len(words)):
            if word== words[i].strip() :
                count += 1
                words[i] = words[i].replace(word, new_word)
        modified_lines.append(' '.join(words))

    if count == 0:
        print('Das Wort wurde nicht ersetzt.')
        return

    with open(filename, 'w') as f:
        f.write(' '.join(modified_lines))

    print(f"Ersetzt {word} durch {new_word}")