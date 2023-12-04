

def p1():

    total = 0
    with open("input.txt") as file:
        for line in file:
            sum = 0
            winnings = []
            line = line.strip().split(":")
            line  = line[1].strip().split("|")
            my_cards = line[1].strip().split(" ")
            winning_cards = line[0].strip().split(" ")
            winning_cards = [x for x in winning_cards if len(x) > 0]
            my_cards = [x for x in my_cards if len(x) > 0]
            
            for el in my_cards:
                if el in winning_cards:
                    winnings.append(el)
            for i in range(len(winnings)):
                if len(winnings) == 1:
                    sum += 1
                    break
                if len(winnings) > 0 and i == 1:
                    sum = sum + 1
                sum = sum * 2
                
            total += sum
            
    return total


def p2():
    
    total = 0
    scratchcards = []

    with open("input.txt") as file:
        for line in file:
            
            
            winnings = []
            line = line.strip().split(":")
            line  = line[1].strip().split("|")
            my_cards = line[1].strip().split(" ")
            winning_cards = line[0].strip().split(" ")
            winning_cards = [x for x in winning_cards if len(x) > 0]
            my_cards = [x for x in my_cards if len(x) > 0]
            


            for el in my_cards:
                if el in winning_cards:
                    winnings.append(el)
            
                
            total += sum
            
    return total


#print(p1())
print(p2())