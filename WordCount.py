# Beginning of file for my sake, imports go up here.
import string

# Function Definitions
def safeInput(promptText):
    systemCommands = ["done","batch","options"] # non-filename input to be accepted
    while True:
        try:
            inputText = input(promptText)
            if inputText in systemCommands:
                return inputText            
            inputFile = open(inputText)
            return inputText
        except FileNotFoundError:
            print("File not found or command entered incorrectly.")
            print("Please ensure the text document(s) are in the same folder as the WordCount program.")

def fileWordCount(filename):
    rawFile = open(filename)
    rawString = rawFile.read()
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
            elif word[-1] == "." and word[0] in string.ascii_uppercase: # the word is less than minimum length (else) and ends in a . AND begins with a capital letter
                sentenceCount -= 1 # the "sentence" is actually an abbreviation, so take the sentence out again
        elif len(word) >= minWordLength:
            wordCount += 1 # word does not end in punctuation and is long enough, so we count it
    return wordCount / sentenceCount

# Main Process
def main():
    print("Hello, welcome to WordCount!")
    print("Please ensure the text document(s) you want to read are in the same folder as the WordCount program.")
    firstInput = safeInput("Then enter the name of the text file you want to scan, or 'batch' if you want to scan multiple: ")

    averageWordcount = 0
    unprocessedText = []

    if firstInput != "batch":
        finalResult = fileWordCount(firstInput)
        print("The average words per sentence of that file was: " + str(finalResult))

        finalSum = 0
        fileCount = 0
        while firstInput == "batch":
            currentInput = safeInput("Enter the name of the next text file you want to scan, or 'done' if you are done: ")
            if currentInput == "done":
                break
            finalSum += fileWordCount(currentInput)
            fileCount += 1
    finalResult = finalSum / finalCount

    if firstInput == "done":
        print "The average of the average words per sentence of those files was: " + str(finalResult))

        print("Yay words!")

# End of File for my sake
main()