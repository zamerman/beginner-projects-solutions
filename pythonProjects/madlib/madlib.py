sentence = '''EXCLAMATION! He said ADVERB as he jumped into his convertible
NOUN and drove off with his ADJECTIVE wife.'''
categories = ['EXCLAMATION', 'ADVERB', 'NOUN', 'ADJECTIVE']

def fillSentence(sentence):
    for category in categories:
        while sentence.find(category) != -1:
            replacement = input(category.lower() + ": ")
            sentence = sentence.replace(category, replacement, 1)
    return sentence

def main():
    try:
        print("Mad Libs Story Maker")
        print(fillSentence(sentence))
    except KeyboardInterrupt:
        quit()

main()
