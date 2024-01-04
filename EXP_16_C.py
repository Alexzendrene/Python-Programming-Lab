import csv

def writein_append():

    file = open("new2.csv", "a", newline='')

    objwr = csv.writer(file)

    while True:
        name = input("enter your name:")
        marks = input("enter your marks:")
        rollno = input("enter your roll no:")
        data = [name, marks, rollno]
        objwr.writerow(data)

        ch = input("enter Y or y for more details")
        if ch not in "Yy":
            break


    file.close()


writein_append()