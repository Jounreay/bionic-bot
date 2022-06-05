spec = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
    " ",
]

BOLD = {
    "ANSI": {"BOLD": "\033[1m", "END": "\033[0m"},
    "RTF": {"BOLD": r"\b ", "END": r"\b0 "},
}


def tokenizeString(aString, separators):

    separators.sort(key=len)
    listToReturn = []
    i = 0
    while i < len(aString):
        theSeparator = ""
        for current in separators:
            if current == aString[i : i + len(current)]:
                theSeparator = current
        if theSeparator != "":
            listToReturn += [theSeparator]
            i = i + len(theSeparator)
        else:
            if listToReturn == []:
                listToReturn = [""]
            if listToReturn[-1] in separators:
                listToReturn += [""]
            listToReturn[-1] += aString[i]
            i += 1
    return listToReturn


def modify_word(sentence: list, type: str):

    for index, word in enumerate(sentence):
        pos = ""
        wordlen = len(word)
        isword = lambda x: False if x in spec else True
        if isword(word):
            if wordlen < 2:
                pos = None
            elif wordlen in range(1, 4):
                pos = 1
            elif wordlen in range(3, 7):
                pos = 2
            elif wordlen in range(6, 11):
                pos = 3
            elif wordlen in range(10, 14):
                pos = 4

            newword = (
                BOLD[type]["BOLD"] + word[:pos] + BOLD[type]["END"] + word[pos:]
                if pos
                else word
            )
            print(newword)
            sentence[index] = newword
    return sentence


def join_sentence(bionicline: list):
    return "".join(bionicline)


with open("/home/jreid/Projects/bionic-bot/text.rtf", "w") as testrtf:
    testrtf.write("{\\rtf1\\ansi \n")

with open("/home/jreid/Projects/bionic-bot/text.txt", "r") as test:
    lines = test.readlines()
    for line in lines:
        line = tokenizeString(line, spec)
        bionicline = modify_word(line, "RTF")
        bionicsentence = join_sentence(bionicline)
        with open("/home/jreid/Projects/bionic-bot/text.rtf", "a") as testrtf:
            testrtf.write(bionicsentence)

with open("/home/jreid/Projects/bionic-bot/text.rtf", "a") as testrtf:
    testrtf.write("}")
