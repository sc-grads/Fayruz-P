# Challenge #1
#
# Consider the following Python list:
#
people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]
#
# Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv
#
# After writing to the file, read and print out the file contents.
#
# Use the default , (comma) as the delimiter.
import csv
with open('people1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for item in people:
        writer.writerow(item)



# reading a csv file
with open('people1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
#
#
# Challenge #2
#
# Change the solution from the previous challenge and use : (colon) as the delimiter.
#
# writing into a csv file
with open('people2.csv', 'w') as f:
    writer = csv.writer(f, delimiter=':')
    for item in people:
        writer.writerow(item)


# reading a csv file
with open('people2.csv') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)