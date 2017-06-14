import csv
A=1
B=2
C=4
cursor = []
cursor.append(A)
cursor.append(B)
cursor.append(C)
print cursor
with open("sample.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(cursor)