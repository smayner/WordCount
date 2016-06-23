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
            inputFile = open(inputText)
            return inputText
        except FileNotFoundError:
            print("File not found or command entered incorrectly. Please try again.")

def fileProcessor(filename):
    processedText = ""
    rawFile = open(filename)
    rawString = rawFile.read()
    punctuation = [".","?",",",":",";"] # what counts as punctuation
    splitString = str.split(rawString)
    
    
    return processedText

def wordsPerSentence(inputText):
    wordCount = 0
    wordMinimum = 4 # the minimum number of letters a word has to contain to count
    return wordCount

# Main Process
print("Hello, welcome to WordCount!")
print("Please ensure the text document(s) you want to read are in the same folder as the WordCount program.")
firstInput = safeInput("Then enter the name of the text file you want to scan, or 'batch' if you want to scan multiple: ")

averageWordcount = 0
unprocessedText = []

if firstInput != "batch":
    firstText = fileProcessor(firstInput)
    finalResult = wordsPerSentence(firstText)

while firstInput == "batch":
    finalSum = 0
    fileCount = 0
    currentInput = safeInput("Enter the name of the next text file you want to scan, or 'done' if you are done: ")
    if currentInput == "done":
        break
    currentText = fileProcessor(currentInput)
    fileCount += 1
    finalResult = wordsPerSentence(currentText)
    
print("Yay words!")

# End of File for my sake
