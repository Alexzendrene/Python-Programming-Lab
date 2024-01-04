import csv

def read_csv():
    try:
        with open("new2.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(f"Name: {row[0]}, Marks: {row[1]}, Roll No: {row[2]}")
    except FileNotFoundError:
        print("The file 'new2.csv' does not exist.")
if __name__ == "__main__":
    read_csv()