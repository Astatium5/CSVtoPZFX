from csv_processing import execute_csv
from pzfx_processing import initialize_file
from tkinter import messagebox, filedialog
from tkinter import *
from os import path


# Function, which initializes the GUI window
def initialize_window():
    while True:
        top = Tk()
        top.title("Kean's Biology Lab. CSV to PZFX")
        top.geometry("1280x720")

        label = Label(top, text="Enter the directory of the input file: ")
        label.pack(side="left")

        # filepath = StringVar(top)
        # entry = Entry(top, bd=5, textvariable=filepath)
        # entry.pack(side="right")

        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))

        button = Button(top, text="Execute", command=top.destroy)
        button.pack(side="bottom")

        top.mainloop()

        if not path.exists(filename):
            top.withdraw()
            messagebox.showerror("Error!", "The specified input file does not exist.")
            continue

        if not filename:
            top.withdraw()
            messagebox.showerror("Error!", "Enter the name of the input file.")
            continue

        # top.mainloop()

        break

    return filename


def main():
    # filename = initialize_window()
    # filename = "gLuc_5943.csv"
    filename = "gLuc timelapse_6019.csv"
    # filename = "/home/dmitrii/PycharmProjects/CSVtoPZFX/gLuc timelapse_6019.csv"
    csv_filename = filename.strip()
    print(csv_filename)
    matrices = execute_csv(csv_filename)

    for i in range(len(matrices)):
        for j in range(len(matrices[i])):
            print(matrices[i][j], sep="\n")
        print("\n")

    initialize_file(csv_filename, matrices)


if __name__ == "__main__":
    main()
