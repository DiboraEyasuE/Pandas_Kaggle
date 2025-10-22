# This program checks whether a credit card is valid or not and further distinguishes between
# a master, American express and visa cards.
card = int(input("Number: "))
while not card:
    card = input("Number: ")
length = len(card)
index = length - 2
sum_doub = 0
later = 0
for i in range(index, -1, -2):
    double = int(card[i])
    un_doubled = int(card[i + 1])
    double *= 2
    if double > 9:
        tenths = int(double / 10)
        ones = double % 10
        double = tenths + ones
    sum_doub += double
    later += un_doubled
    if i == 1:
        if length % 2 != 0:
            later += int(card[0])
        else:
            sum_doub += int(card[0])
valid = int(sum_doub) + later
if valid % 10 == 0:
    if card[0] == '4' and length in [16, 13]:
        print("VISA")
    elif card[0] == '3' and card[1] in ['4', '7']:
        print("AMEX")
    elif card[0] == '5' and card[1] in ['1', '2', '3', '4', '5']:
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")
