# Beginning of file for my sake, imports go up here.
import string

# Function Definitions
def safeInput(promptText):
    systemCommands = ["done","batch"] # non-filename input to be accepted
    while True:
        try:
            inputText = input(promptText)
            if inputText in systemCommands:
                return inputText
            elif inputText[-4:] != ".txt":
                raise ValueError
            inputFile = open(inputText)
            return inputText
        except FileNotFoundError:
            print("File not found, please ensure the text document(s) are in the same folder as the WordCount program.")
        except ValueError:
            print("File in incorrect format, please make sure the essay is a .txt file.")

def fileWordCount(filename):
    rawFile = open(filename)
    rawString = rawFile.read()
    rawFile.close()
    sentenceCount = 0
    wordCount = 0
    punctuation = [".","?",",",":",";"] # what counts as punctuation
    minWordLength = 4 # the minimum length of a word to count; declared as a variable for consistency
    splitString = str.split(rawString)
    for word in splitString:
        if word[-1] in punctuation:
            sentenceCount += 1
            if len(word)-1 >= minWordLength: # -1 to not count the punctuation
                wordCount += 1
            elif word[-1] == "." and word[0] in string.ascii_uppercase: # the word is less than minimum length (else) AND ends in a . AND begins with a capital letter
                sentenceCount -= 1 # the "sentence" is actually an abbreviation, so take the sentence out again
        elif len(word) >= minWordLength:
            wordCount += 1 # word does not end in punctuation and is long enough, so we count it
    return wordCount / sentenceCount

def singleFile(filename):
    result = fileWordCount(filename)
    print("The average words per sentence of that file was:",result)

def batchFile():
    outputFile = open("WordCount.txt",'w')
    outputFile.write("")
    finalSum = 0
    fileCount = 0
    currentInput = safeInput("Enter the name of the next text file you want to scan, or 'done' if you are done: ")
    outputFile = open("WordCount.txt",'a')   
    while currentInput != "done":
        currentAverage = fileWordCount(currentInput)
        finalSum += currentAverage
        fileCount += 1
        outputFile.write("The average words per sentence for {0} was {1}.\n".format(currentInput,currentAverage))
        currentInput = safeInput("Enter the name of the next text file you want to scan, or 'done' if you are done: ")
    finalResult = finalSum / fileCount
    outputFile.write("The average words per sentence for those files was {0}.".format(finalResult))
    outputFile.close()
    print ("The average words per sentence of those files was:",finalResult)
    print ("You can also see specific details in WordCount.txt")

# Main Process
def main():
    print("Hello, welcome to WordCount!")
    print("Please ensure the text document(s) you want to read are in the same folder as the WordCount program.")
    firstInput = safeInput("Then enter the name of the text file you want to scan, or 'batch' if you want to scan multiple: ")
    if firstInput != "batch":
        singleFile(firstInput)
    else:
        batchFile()
    print("Yay words!")

# End of File, only main() after this line
main()
# :3--<