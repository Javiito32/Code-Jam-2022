def main():
    cases = int(input())

    for i in range(1, cases+1):
        dices = input()
        dicesValues = input().split()
        dicesValues = [int(i) for i in dicesValues]
        dicesValues.sort()
        
        counter = 0
        for value in dicesValues:
            if value > counter:
                counter += 1
                continue
            else:
                continue
        
        print("Case #" + str(i) + ": " + str(counter))

main()