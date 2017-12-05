import csv

def read(filename):
    """read a given csv file but don't include the header row in result"""
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader][1:]

def retrieve_statistics(data, column_index, column_name):
    required_stats = sorted_data(data, column_index)
    return formatted_statistics(required_stats, column_name, column_index)

def sorted_data(data, sorting_column_index):
    """retrieve the first 3 rows of sorted data"""
    return sorted(
        data,
        key=lambda data: float(data[sorting_column_index]),
        reverse=True)[:3]

def formatted_statistics(stats, required_stats_column_name, required_stats_column):
    """Format retrieved stats for pretty printing"""
    result = []
    for row in stats:
        result.append("Player: {}, Team: {}, {}:{}".format(
            row[0],
            row[1],
            required_stats_column_name,
            row[required_stats_column]))
    return "{}\n{}\n{}".format("-"*30, "\n".join(result), "-"*30)

def read_menu_options(file):
    options_file = open(file, "r")
    menu_option_array = []

    for line in options_file:
        menu_option_array.append(line.replace("\n", ""))

    return menu_option_array

def menu_options_dict():
    options = dict();

    options["main"] = read_menu_options("data_files/Build-Main.txt")
    options["qb"] = read_menu_options("data_files/Option01Menu.txt")
    options["rb"] = read_menu_options("data_files/Option02Menu.txt")
    options["recv"] = read_menu_options("data_files/Option03Menu.txt")
    options["tackles_sacks"] = read_menu_options("data_files/Option04Menu.txt")
    options["interceptions"] = read_menu_options("data_files/Option05Menu.txt")

    return options
