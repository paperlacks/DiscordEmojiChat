import os

baseString = ":regional_indicator_{0}:"

numberDict = {
    "0": ":zero:",
    "1": ":one:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:"
}

def main():
    while True:
        word = str(input("Enter a word to emojify--> "))
        returnString = ""
        for letter in word:
            if letter == " ":
                returnString += "   "
                continue
            if letter in numberDict:
                letter = numberDict[letter]
                returnString += letter
                continue
            letter = letter.lower()
            returnString += baseString.format(letter)
            returnString += " "

        os.system('echo ' + returnString + ' | clip')
        print("Copied emojified '" + word + "' to clipboard.")


if __name__ == "__main__":
    main()
