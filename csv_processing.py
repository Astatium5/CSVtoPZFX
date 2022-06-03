import csv


def check_empty_row(row):
    for string in row:
        if string != "":
            return False

    return True


def check_title_row(row):
    counter = 1
    marker = False

    for string in row:
        if string.isnumeric():
            if int(string) == counter and not marker:
                counter += 1
                marker = True
            elif int(string) != counter and counter != 12:
                return False

    return True


# Function for reading the data from the csv file
def read_the_file(filepath):
    rows = []

    with open(filepath, "r", encoding="iso-8859-1") as csvfile:
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
            if "Plate information" in string:
                marker = False
            if "Results for" in string or "Calculated results:" in string:
                marker = True
            if marker:
                table.append(row)
                break

    return table


# Function, which deletes unneeded rows from the list of strings from the file
def delete_rows(file):
    counter = 0

    while counter < len(file):
        if len(file[counter][0]) == 0:
            file.remove(file[counter])

        counter += 1

    for row in file:
        if row[0] == "" or "Results for" in row[0] or "Calculated results:" in row[0]:
            file.remove(row)


# Function for deleting unnecessary matrices
def delete_matrices(matrices):
    # delete unneccesary matrices at the end
    for i in reversed(range(len(matrices))):
        if matrices[i][0][0] == -1 or matrices[i][0][0] == 0:
            del matrices[i]

    # delete duplicate matrices
    return [v for i, v in enumerate(matrices) if i % 2 == 0]


# Function, which creates a matrix from a list of strings
def create_matrix(data):
    matrix = [[0 for x in range(11)] for y in range(8)]

    for i in range(len(data)):
        for j in range(1, 12):
            if data[i][j].isdecimal():
                matrix[i][j - 1] = int(data[i][j])
            if len(data[i][j]) == 0:
                matrix[i][j - 1] = -1

    return matrix


# Function, which translates the strings from the file into a list of matrices
def strings_to_matrices(data):
    arr = []
    i = 0

    while i < len(data):
        arr.append(create_matrix(data[i : i + 8]))
        i += 8

    return arr


# Function, which uses all the function defined in this file in order to obtain
# a list of matrices from a csv file
def execute_csv(filename):
    file = read_the_file(filename)
    data = extract_info(file)
    delete_rows(data)

    # needed in case data is duplicated
    matrices = strings_to_matrices(data)
    matrices = delete_matrices(matrices)

    return matrices
