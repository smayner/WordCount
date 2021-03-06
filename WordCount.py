# Beginning of file, imports go up here.
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
            print("File in incorrect format, please make sure the essay is a .txt file and that you add .txt to the name of the file.")

def safeDivision(dividend, divisor):
    if divisor == 0:
        divisor += 1
        print ("Division by zero occurred; answer may be unreliable.")
    return dividend / divisor

def fileWordCount(filename):
    with open(filename, 'r') as rawFile:
        rawString = rawFile.read()
    sentenceCount = 0
    wordCount = 0
    punctuation = [".","?",",",":",";","!"] # what counts as punctuation
    minWordLength = 4 # the minimum length of a word to count; declared as a variable for consistency
    splitString = str.split(rawString)
    for word in splitString:
        if word[-1] in punctuation:
            sentenceCount += 1 # word ends in punctuation, so we count a sentence
            if len(word)-1 >= minWordLength: # -1 to not count the punctuation
                wordCount += 1 # word is long enough, so we count it
            elif word[-1] == "." and word[0] in string.ascii_uppercase: # the word is less than minimum length (else) AND ends in a . AND begins with a capital letter
                sentenceCount -= 1 # the "sentence" is actually an abbreviation, so take the sentence out again
        elif len(word) >= minWordLength:
            wordCount += 1 # word does not end in punctuation and is long enough, so we count it
    return safeDivision(wordCount,sentenceCount)

def singleFile(filename):
    result = fileWordCount(filename)
    with open("WordCount.txt",'a') as outputFile:
        outputFile.write("The average words per sentence for {0} was {1}\n".format(filename,result))
    print("The average words per sentence of that file was:",result)
    return result # this return does nothing for single files, but allows integration with batchFile

def batchFile():
    finalSum = 0
    fileCount = 0
    currentInput = safeInput("Enter the name of the next text file you want to scan, or 'done' if you are done: ") 
    while currentInput != "done":
        currentAverage = singleFile(currentInput)
        finalSum += currentAverage
        fileCount += 1
        currentInput = safeInput("Enter the name of the next text file you want to scan, or 'done' if you are done: ")
    finalResult = safeDivision(finalSum,fileCount)
    with open("WordCount.txt",'a') as outputFile:
        outputFile.write("The average words per sentence for those files was {0}".format(finalResult))
    print ("The average words per sentence of those files was:",finalResult)
    print ("You can also see specific details in WordCount.txt")

# Main Process
def main():
    print("Hello, welcome to WordCount!")
    print("Please ensure the text document(s) you want to read are in the same folder as the WordCount program.")
    firstInput = safeInput("Then enter the name of the text file you want to scan, or 'batch' if you want to scan multiple: ")
    outputFile = open("WordCount.txt",'w').close() # wipes the output file clean because singleFile appends
    if firstInput == "done":
        print("No files were scanned. Please close and restart WordCount to try again.")    
    elif firstInput != "batch":
        singleFile(firstInput)
    else:
        batchFile()
    input("Press enter to finish and close the program.")

# End of File, only main() after this line
main()
# :3--<