list1 = [2, 3, 4]

list2 = [5, 6, 7]

list3 = list1 + list2

print(list3)

print(list3)

def is_palindrome(string):
    return string == string[:: -1]


list4 = [
    [1,2,3],
    [2,5,6],
    [7,8,9]
]

list5 = [
    [1,2,3],
    [2,5,6],
    [7,8,9]
]

list6 = []

for i in range(len(list4)):
    row =[]
    for j in range(len(list4[i])):
        row.append(list4[i][j] * list5[i][j])
    list6.append(row)

print (list6)


dictionary1 = {

("hamza", "khan") : 333333,
("John", "Doe") : 444444
}

first = input("Enter your first name: ")
last = input("Enter your last name: ")  

def find_phone_number(first, last):
    return dictionary1.get((first, last), "Phone number not found.")