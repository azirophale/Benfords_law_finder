import csv

# Declaring Variabels for numver counts
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

line_count = 0
# benfords list for storing data 
benndord_list = []

#  This function will return first digit of Integer
def firstDigit(num):
    while (num >= 10):
        num = num // 10
    return num


try:
    # opens Csv file for processing
    with open('Insert_your_data_inside_this.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            try:
                number = int(row[0])
            except:
                # print("error")
                continue
            # By calling function we will get first digit of integer   
            num = firstDigit(number)
            # if Number is zero then it will not count
            if num != 0 or num !="":
                line_count = line_count+1
            if num == 1:
                one = one+1
            elif num == 2:
                two = two+1
            elif num == 3:
                three = three+1
            elif num == 4:
                four = four+1
            elif num == 5:
                five = five + 1
            elif num == 6:
                six = six+1
            elif num == 7:
                seven = seven+1
            elif num == 8:
                eight = eight+1
            elif num == 9:
                nine = nine+1
except:
    print("There Is Some ERROR.......!")

# Will print repetation of numbers
print("one", one)
print("two", two)
print("three", three)
print("four", four)
print("five", five)
print("six", six)
print("seven", seven)
print("eight", eight)
print("Nine", nine)

# Total line by wich average is counted
print("Total Values",line_count)

benndord_list.append(int(one/line_count*100))
benndord_list.append(int(two/line_count*100))
benndord_list.append(int(three/line_count*100))
benndord_list.append(int(four/line_count*100))
benndord_list.append(int(five/line_count*100))
benndord_list.append(int(six/line_count*100))
benndord_list.append(int(seven/line_count*100))
benndord_list.append(int(eight/line_count*100))
benndord_list.append(int(nine/line_count*100))

# Percentage of Data 
# print(benndord_list)
print("Graph :-")
# will print Simple Graph (You sould read it in sidways)
for i in benndord_list:
    print("-"*i,i,"%")
