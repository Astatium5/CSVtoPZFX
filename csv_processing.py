import csv


# Function for reading the data from the csv file
def read_the_file(filepath):
    rows = []

    with open(filepath, 'r', encoding="iso-8859-1") as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            rows.append(row)

    return rows


# Function for getting the table out of the csv file
def extract_info(file):
    table = []
    marker = False

    for row in file:
        for string in row:
            if "H" in string:
                marker = False
            if "Results for" in string:
                marker = True
            if marker:
                table.append(row)
                break

    return table


# Function, which deletes unneeded rows from the list of strings from the file
def delete_rows(file):
    counter = 0

    for row in file:
        for string in row:
            if "Results for" in string or "H" in string or "A" in string:
                file.remove(row)
                break

    while counter < len(file):
        if len(file[counter][0]) == 0:
            file.remove(file[counter])

        counter += 1


# Function, which creates a matrix from a list of strings
def create_matrix(data):
    matrix = [[0 for x in range(9)] for y in range(6)]

    for i in range(len(data)):
        for j in range(2, 11):
            if data[i][j].isdecimal():
                matrix[i][j-2] = int(data[i][j])
            if len(data[i][j]) == 0:
                matrix[i][j-2] = -1

    return matrix


# Function, which translates the strings from the file into a list of matrices
def strings_to_matrices(data):
    arr = []
    i = 0

    while i < len(data):
        arr.append(create_matrix(data[i:i+6]))
        i += 6

    return arr


# Function, which uses all the function defined in this file in order to obtain
# a list of matrices from a csv file
def execute_csv(filename):
    file = read_the_file(filename)
    data = extract_info(file)
    delete_rows(data)
    matrices = strings_to_matrices(data)

    return matrices
