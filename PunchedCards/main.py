import sys

def main():
    cases = int(input())
    for i in range(1, cases+1):
        line = input()
        print('Case #' + str(i) + ':')
        printAsciiTable(int(line.split(" ")[0]), int(line.split(" ")[1]))

def printAsciiTable(x, y):

    lineToPrint = "..+"
    for i in range(y-1):
        lineToPrint += "-+"
    print(lineToPrint)

    lineToPrint = "..|"
    for i in range(y-1):
        lineToPrint += ".|"
    print(lineToPrint)
    printSeparatorLine(y)
    rowsPrinted = 1

    while rowsPrinted < x:
        printContentLine(y)
        printSeparatorLine(y)
        rowsPrinted += 1

def printSeparatorLine(width):
    lineToPrint = "+-+"
    for i in range(width-1):
        lineToPrint += "-+"
    print(lineToPrint)

def printContentLine(width):
    lineToPrint = "|.|"
    for i in range(width-1):
        lineToPrint += ".|"
    print(lineToPrint)


main()