import random
string = ""

def generate(textlength):

    #Open seed text file
    with open ("sherlock.txt", "r", encoding='utf8') as myfile:
        string=myfile.read().replace('\n', ' ')


    string = string.split()
    triples = []
    sentenceLen = 25
    possibleWords = {}
    possibleStarts = []
    w1, w2, w3 = "","",""


    #Get each word + the following two words
    for i in range(len(string) - 2):
        triples.append(string[i] + " " + string[i+1] + " " + string[i+2])

    #add two words as key, with the third as definition
    for each in triples:
        each = each.split(" ")
        w1, w2 = each[0], each[1]
        w3 = each[2]
        key = (w1 + " " + w2)
        value = w3
        #If key exists, add it. If not, create the key (w1+w2)
        if key in possibleWords:
            possibleWords[key].append(w3)
        else:
            possibleWords[key] = [w3]


    #Populate possibleStarts with only words that come after periods
    for i in range(1,len(string)):
        if string[i-1].endswith("."):
            possibleStarts.append(string[i] + " " + string[i+1])
    start = random.choice(possibleStarts)
    start = start.split(" ")

    #Add two start words to the sentence
    startWord = start[0]
    nextWord = start[1]
    w1, w2 = startWord,nextWord
    words = [startWord,nextWord]

    #Choose the next word based on the existing dict.
    for i in range(0,textlength):
        choices = possibleWords[w1 + " " + w2]
        nextWord = random.choice(possibleWords[w1 + " " + w2])
        w1 = w2
        w2 = nextWord
        words.append(nextWord)
    textfull = " ".join(words)

    ##Just cleaning up the text; making sure it doesn't cut off the end of a sentence.
    textfull = textfull.split(".")
    textfull = textfull[:-1]
    textfull = ".".join(textfull) + "."
    return textfull
print(generate(int((input("Length?")))))








