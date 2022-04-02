class Printer:
    def __init__(self, c, m, y, k):
        self.c = c
        self.m = m
        self.y = y
        self.k = k

class PrinterSet:
    def __init__(self, printer0, printer1, printer2):
        self.printers = []
        self.adjustment = { "c": 0, "m": 0, "y": 0, "k": 0 }
        self.highestValues = { "c": -1, "m": -1, "y": -1, "k": -1 }
        self.lastTotalCalculated = 0
        self.printers.append(printer0)
        self.printers.append(printer1)
        self.printers.append(printer2)

    def getHighestPossibleCyan(self):
        if self.highestValues['c'] == -1:
            HighestPossibleVal = self.printers[0].c
            for printer in self.printers:
                if printer.c < HighestPossibleVal:
                    HighestPossibleVal = printer.c
            
            self.highestValues['c'] = HighestPossibleVal
            return HighestPossibleVal
        else:
            return self.highestValues['c']
    
    def getHighestPossibleMagenta(self):
        if self.highestValues['m'] == -1:
            HighestPossibleVal = self.printers[0].m
            for printer in self.printers:
                if printer.m < HighestPossibleVal:
                    HighestPossibleVal = printer.m
            
            self.highestValues['m'] = HighestPossibleVal
            return HighestPossibleVal
        else:
            return self.highestValues['m']

    def getHighestPossibleYellow(self):
        if self.highestValues['y'] == -1:
            HighestPossibleVal = self.printers[0].y
            for printer in self.printers:
                if printer.y < HighestPossibleVal:
                    HighestPossibleVal = printer.y

            self.highestValues['y'] = HighestPossibleVal
            return HighestPossibleVal
        else:
            return self.highestValues['y']

    def getHighestPossibleBlack(self):
        if self.highestValues['k'] == -1:
            HighestPossibleVal = self.printers[0].k
            for printer in self.printers:
                if  printer.k < HighestPossibleVal:
                    HighestPossibleVal = printer.k

            self.highestValues['k'] = HighestPossibleVal
            return HighestPossibleVal
        else:
            return self.highestValues['k']

    def isPossibleCase(self):
        self.lastTotalCalculated = self.getHighestPossibleBlack() + self.getHighestPossibleYellow() + self.getHighestPossibleMagenta() + self.getHighestPossibleCyan()
        return self.lastTotalCalculated >= 1000000

    def printFinalColor(self):
        return (str(self.getHighestPossibleCyan()-self.adjustment['c']) + " " +
            str(self.getHighestPossibleMagenta()-self.adjustment['m']) + " " +
            str(self.getHighestPossibleYellow()-self.adjustment['y']) + " " +
            str(self.getHighestPossibleBlack()-self.adjustment['k'])
        )

def main():
    cases = int(input())
    for i in range(1, cases+1):
        printString = "Case #" + str(i) + ": "

        printer0data = input().split(" ")
        printer0 = Printer(
            int(printer0data[0]), 
            int(printer0data[1]), 
            int(printer0data[2]), 
            int(printer0data[3])
        )
        printer1data = input().split(" ")
        printer1 = Printer(
            int(printer1data[0]), 
            int(printer1data[1]), 
            int(printer1data[2]), 
            int(printer1data[3])
        )
        printer2data = input().split(" ")
        printer2 = Printer(
            int(printer2data[0]), 
            int(printer2data[1]), 
            int(printer2data[2]), 
            int(printer2data[3])
        )

        printerSet = PrinterSet(printer0, printer1, printer2)
        if not printerSet.isPossibleCase():
            printString += "IMPOSSIBLE"
            print(printString)
        else:
            difference = printerSet.lastTotalCalculated - 1000000
            
            actualAdjustment = getInkAdjustment(difference, printerSet.getHighestPossibleBlack())
            printerSet.adjustment['k'] = actualAdjustment['inkAdjustment']
            difference = actualAdjustment['differenceLeft']

            actualAdjustment = getInkAdjustment(difference, printerSet.getHighestPossibleYellow())
            printerSet.adjustment['y'] = actualAdjustment['inkAdjustment']
            difference = actualAdjustment['differenceLeft']

            actualAdjustment = getInkAdjustment(difference, printerSet.getHighestPossibleMagenta())
            printerSet.adjustment['m'] = actualAdjustment['inkAdjustment']
            difference = actualAdjustment['differenceLeft']

            actualAdjustment = getInkAdjustment(difference, printerSet.getHighestPossibleCyan())
            printerSet.adjustment['c'] = actualAdjustment['inkAdjustment']
            difference = actualAdjustment['differenceLeft']
            
            printString += printerSet.printFinalColor()
            print(printString)

def getInkAdjustment(difference, ink):
    amount = ink - difference
    if amount >= 0:
        return {
            "inkAdjustment": difference,
            "differenceLeft": 0
        };
    else:
        return {
            "inkAdjustment": ink,
            "differenceLeft": difference - ink
        };


main()