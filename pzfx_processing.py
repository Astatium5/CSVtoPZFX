from xml.dom import minidom


def change_file_extension(filename):
    filename.replace(".csv", ".pzfx")


def create_info(root, empty_string, info, name):
    const = root.createElement("Constant")
    info.appendChild(const)

    name_tag = root.createElement("Name")
    const.appendChild(name_tag)

    name_text = root.createTextNode(name)
    name_tag.appendChild(name_text)

    value = root.createElement("Value")
    # value.appendChild(empty_string)
    const.appendChild(value)


def create_counter_columns(root, table, length):
    xColumn = root.createElement("XColumn")
    xColumn.setAttribute("Width", "50")
    xColumn.setAttribute("Subcolumns", '1')
    xColumn.setAttribute("Decimals", '0')
    table.appendChild(xColumn)

    title = root.createElement("Title")
    xColumn.appendChild(title)

    subcolumn = root.createElement("Subcolumn")
    xColumn.appendChild(subcolumn)

    for i in range(length):
        entry = root.createElement('d')
        subcolumn.appendChild(entry)

        number = root.createTextNode(str(i))
        entry.appendChild(number)

    xAdvancedColumn = root.createElement("XAdvancedColumn")
    xAdvancedColumn.setAttribute("Version", '1')
    xAdvancedColumn.setAttribute("Width", "51")
    xAdvancedColumn.setAttribute("Decimals", '0')
    xAdvancedColumn.setAttribute("Subcolumns", '1')
    table.appendChild(xAdvancedColumn)

    title = root.createElement("Title")
    xAdvancedColumn.appendChild(title)

    subcolumn = root.createElement("Subcolumn")
    xAdvancedColumn.appendChild(subcolumn)

    for i in range(length):
        entry = root.createElement('d')
        subcolumn.appendChild(entry)

        number = root.createTextNode(str(i))
        entry.appendChild(number)


def print_matrices(root, table, matrices):
    yColumn = root.createElement("YColumn")
    yColumn.setAttribute("Width", "300")
    yColumn.setAttribute("Decimals", '0')
    yColumn.setAttribute("Subcolumns", '3')

    for i in range(len(matrices)):





# Function, which initializes the pzfx file
def initialize_file(csv_filename, matrices):
    # FIXME Add Encoding
    root = minidom.Document()
    empty_string = root.createTextNode("")

    prism_file = root.createElement("GraphPadPrismFile")
    prism_file.setAttribute("PrismXMLVersion", "5.00")
    root.appendChild(prism_file)

    created = root.createElement("Created")
    prism_file.appendChild(created)

    original_version = root.createElement("OriginalVersion")
    original_version.setAttribute("CreatedByProgram", "CSV to PZFX by Dmitrii Golubenko")
    # FIXME
    original_version.setAttribute("DateTime", "2 november")
    created.appendChild(original_version)

    info_sequence = root.createElement("InfoSequence")
    prism_file.appendChild(info_sequence)

    ref = root.createElement("Ref")
    ref.setAttribute("ID", "Info0")
    ref.setAttribute("Selected", '1')
    # ref.appendChild(empty_string)
    info_sequence.appendChild(ref)

    info = root.createElement("Info")
    info.setAttribute("ID", "Info0")
    prism_file.appendChild(info)

    title_info = root.createElement("Title")
    info.appendChild(title_info)

    # May be "Project info 1" (with a lower-case letter)
    title_project_text = root.createTextNode("Project Info 1")
    title_info.appendChild(title_project_text)

    notes_info = root.createElement("Notes")
    # notes_info.appendChild(empty_string)
    info.appendChild(notes_info)

    create_info(root, empty_string, info, "Experiment Date")
    create_info(root, empty_string, info, "Experiment ID")
    create_info(root, empty_string, info, "Notebook ID")
    create_info(root, empty_string, info, "Project")
    create_info(root, empty_string, info, "Experimenter")
    create_info(root, empty_string, info, "Protocol")

    table_sequence = root.createElement("TableSequence")
    table_sequence.setAttribute("Selected", '1')

    ref_table_sequence = root.createElement("Ref")
    ref_table_sequence.setAttribute("ID", "Table0")
    ref_table_sequence.setAttribute("Selected", '1')
    # ref_table_sequence.appendChild(empty_string)
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


    xml = root.toprettyxml(indent = '\t')

    pzfx_filename = csv_filename.replace(".csv", ".pzfx")
    with open(pzfx_filename, "w") as file:
        file.write(xml)
