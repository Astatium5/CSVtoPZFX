from csv_processing import execute_csv
from pzfx_processing import initialize_file
from tkinter import *


# Function, which initializes the GUI window
def initialize_window():
    top = Tk()

    label = Label(top, text="Enter the directory of the file: ")
    label.pack(side=LEFT)

    entry = Entry(top, bd=5)
    entry.pack(side=RIGHT)
    filepath = entry.get()

    button = Button(top, text="Execute")
    button.pack()

    top.mainloop()
    return filepath


def main():
    # filename = initialize_window
    # filename = "gLuc_5943.csv"
    csv_filename = "gLuc timelapse_6019.csv".strip()
    matrices = execute_csv(csv_filename)

    # for i in range(len(matrices)):
    #     for j in range(len(matrices[i])):
    #         print(matrices[i][j], sep="\n")
    #     print("\n")

    initialize_file(csv_filename, matrices)


if __name__ == "__main__":
    main()
