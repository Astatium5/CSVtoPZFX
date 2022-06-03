from xml.dom import minidom
from datetime import datetime


def change_file_extension(filename):
    filename.replace(".csv", ".pzfx")


def create_info(root, info, name):
    const = root.createElement("Constant")
    info.appendChild(const)

    name_tag = root.createElement("Name")
    const.appendChild(name_tag)

    name_text = root.createTextNode(name)
    name_tag.appendChild(name_text)

    value = root.createElement("Value")
    const.appendChild(value)


def create_entry(root, subcolumn, value):
    entry = root.createElement("d")
    subcolumn.appendChild(entry)

    number = root.createTextNode(str(value))
    entry.appendChild(number)


def create_title(root, table, i, j):
    title = root.createElement("Title")
    table.appendChild(title)

    pos = root.createTextNode("Row " + str(i) + ", Column " + str(j))
    title.appendChild(pos)


def create_ycolumn(root):
    ycolumn = root.createElement("YColumn")
    ycolumn.setAttribute("Width", "300")
    ycolumn.setAttribute("Decimals", "0")
    ycolumn.setAttribute("Subcolumns", "3")

    return ycolumn


def create_counter_columns(root, table, length):
    xColumn = root.createElement("XColumn")
    xColumn.setAttribute("Width", "50")
    xColumn.setAttribute("Subcolumns", "1")
    xColumn.setAttribute("Decimals", "0")
    table.appendChild(xColumn)

    title = root.createElement("Title")
    xColumn.appendChild(title)

    subcolumn = root.createElement("Subcolumn")
    xColumn.appendChild(subcolumn)

    for i in range(length):
        entry = root.createElement("d")
        subcolumn.appendChild(entry)

        number = root.createTextNode(str(i))
        entry.appendChild(number)

    xAdvancedColumn = root.createElement("XAdvancedColumn")
    xAdvancedColumn.setAttribute("Version", "1")
    xAdvancedColumn.setAttribute("Width", "51")
    xAdvancedColumn.setAttribute("Decimals", "0")
    xAdvancedColumn.setAttribute("Subcolumns", "1")
    table.appendChild(xAdvancedColumn)

    title = root.createElement("Title")
    xAdvancedColumn.appendChild(title)

    subcolumn = root.createElement("Subcolumn")
    xAdvancedColumn.appendChild(subcolumn)

    for i in range(length):
        create_entry(root, subcolumn, i)


def print_matrices(root, table, matrices):
    for i in range(len(matrices[0])):  # in one table by rows
        for j in range(11):  # in one row of a table by entries
            if matrices[0][i][j] != -1:
                if j == 0 or j == 4 or j == 8:
                    ycolumn = create_ycolumn(root)
                    create_title(root, ycolumn, i, j)

                subcolumn = root.createElement("Subcolumn")
                ycolumn.appendChild(subcolumn)

                for k in range(len(matrices)):
                    create_entry(root, subcolumn, matrices[k][i][j])

                if j == 2 or j == 6 or j == 10:
                    table.appendChild(ycolumn)


# Function, which initializes the pzfx file
def initialize_file(csv_filename, matrices):
    root = minidom.Document()

    prism_file = root.createElement("GraphPadPrismFile")
    prism_file.setAttribute("PrismXMLVersion", "5.00")
    root.appendChild(prism_file)

    created = root.createElement("Created")
    prism_file.appendChild(created)

    original_version = root.createElement("OriginalVersion")
    original_version.setAttribute(
        "CreatedByProgram", "CSV to PZFX by Dmitrii Golubenko"
    )
    # Prints the time
    time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    original_version.setAttribute("DateTime", time)
    created.appendChild(original_version)

    info_sequence = root.createElement("InfoSequence")
    prism_file.appendChild(info_sequence)

    ref = root.createElement("Ref")
    ref.setAttribute("ID", "Info0")
    ref.setAttribute("Selected", "1")
    info_sequence.appendChild(ref)

    info = root.createElement("Info")
    info.setAttribute("ID", "Info0")
    prism_file.appendChild(info)

    title_info = root.createElement("Title")
    info.appendChild(title_info)

    title_project_text = root.createTextNode("Project Info 1")
    title_info.appendChild(title_project_text)

    notes_info = root.createElement("Notes")
    info.appendChild(notes_info)

    create_info(root, info, "Experiment Date")
    create_info(root, info, "Experiment ID")
    create_info(root, info, "Notebook ID")
    create_info(root, info, "Project")
    create_info(root, info, "Experimenter")
    create_info(root, info, "Protocol")

    table_sequence = root.createElement("TableSequence")
    table_sequence.setAttribute("Selected", "1")

    ref_table_sequence = root.createElement("Ref")
    ref_table_sequence.setAttribute("ID", "Table0")
    ref_table_sequence.setAttribute("Selected", "1")
    table_sequence.appendChild(ref_table_sequence)

    table = root.createElement("Table")
    table.setAttribute("ID", "Table0")
    table.setAttribute("XFormat", "numbers")
    table.setAttribute("YFormat", "replicates")
    table.setAttribute("Replicates", "3")
    table.setAttribute("TableType", "XY")
    table.setAttribute("EVFormat", "AsteriskAfterNumber")
    prism_file.appendChild(table)

    table_title = root.createElement("Title")
    table.appendChild(table_title)

    row_titles_column = root.createElement("RowTitlesColumn")
    row_titles_column.setAttribute("Width", "100")
    table.appendChild(row_titles_column)

    subcolumn = root.createElement("Subcolumn")
    row_titles_column.appendChild(subcolumn)

    create_counter_columns(root, table, len(matrices))
    print_matrices(root, table, matrices)

    xml = root.toprettyxml(indent="\t")

    pzfx_filename = csv_filename.replace(".csv", ".pzfx")
    with open(pzfx_filename, "w") as file:
        file.write(xml)
