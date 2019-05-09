import math
import sys

def read_file(filename):
    try:
        f=open(filename, 'r')
        return f.read()
    except:
        print("Error opening file")
        sys.exit()

def get_words_from_line_list(L):
    wordList=[]
    for line in L:
        wordsInLine=getWordsFromString(line)
        wordList.extend(wordsInLine)
    return wordList

def getWordsFromString(line):
    wordList=[]
    characterList=[]

    for c in line:
        if c.isalnum():
            characterList.append(c)
        elif len(characterList):
            word="".join(characterList)
            word=word.lower()
            wordList.append(word)
            characterList=[]
            #Empty the character list once a word is created
    if len(characterList):
        word="".join(characterList)
        word=word.lower()
        wordList.append(word)
    return wordList
def countFrequency(wordList):
    D={}
    for newWord in wordList:
        if newWord in D:
            D[newWord]+=1
        else:
            D[newWord]=1
    return D
def wordFreqForFile(filename):
    text=read_file(filename)
    wordList=getWordsFromString(text)
    freqMapping=countFrequency(wordList)
    return freqMapping

def innerProduct(D1, D2):
    sum=0.0
    for key in D1:
        if key in D2:
            sum+=D1[key]*D2[key]
    return sum

def vectorAngle(D1, D2):
    numerator=innerProduct(D1,D2)
    denominator=math.sqrt(innerProduct(D1, D1) * innerProduct(D2, D2))
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv)!=3:
        print("Error")
    else:
        filename1=sys.argv[1]
        filename2=sys.argv[2]
        sorted_word_list_1=wordFreqForFile(filename1)
        sorted_word_list_2=wordFreqForFile(filename2)
        distance =vectorAngle(sorted_word_list_1, sorted_word_list_2)
        print(f"Distance: {distance}")

if __name__=="__main__":
    main()
