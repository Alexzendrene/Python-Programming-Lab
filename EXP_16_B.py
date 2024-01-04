import csv
def writein():
    file=open("new2.csv","w",newline ="")
    objwr=csv.writer(file)
    objwr.writerow(["name","marks","roll no"])
    while True:
        name = input("enter your name: ")
        marks = input("enter your marks: ")
        roll_no = input("enter your roll no.: ")
        list=[name,marks,roll_no]
        objwr.writerow(list)
        # for adding more enteries into the csv file.
        # any other letter for exiting.
        ch=input("enter Y OR y for more detail") 
        if ch not in "Yy":
          break
writein()
