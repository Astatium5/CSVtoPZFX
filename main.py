from csv_processing import execute_csv
from pzfx_processing import initialize_file


def main():
    # filename = "gLuc_5943.csv"
    filename = "AL_05.24.22_GLuc_RLuc.csv"
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
