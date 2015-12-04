"""test"""
import csv
def main():
    """test"""
    with open('t1.csv',newline='') as csvfile:
    aaa = csv.reader(csvfile)
    for row in aaa:
    print(row)
main()
