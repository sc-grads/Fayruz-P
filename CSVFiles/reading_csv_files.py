#################################
## CSV Module
## Readind CSV Files
#################################

###CSV File - (airtravel.csv) - attached to this lecture
# "Month", "1958", "1959", "1960"
# "JAN",  340,  360,  417
# "FEB",  318,  342,  391
# "MAR",  362,  406,  419
# "APR",  348,  396,  461
# "MAY",  363,  420,  472
# "JUN",  435,  472,  535
# "JUL",  491,  548,  622
# "AUG",  505,  559,  606
# "SEP",  404,  463,  508
# "OCT",  359,  407,  461
# "NOV",  310,  362,  390
# "DEC",  337,  405,  432

## Importing the module
import csv

## Opening the file in read-only mode. airtravel.csv is in the same directory with the python script
with open('airtravel.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)  # using a csv.reader object

    next(reader)  # skipping the first line (header)
    for row in reader:
        print(row)  # row is a list, each field is list element