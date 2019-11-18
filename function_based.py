from csv import reader
opened_file = open('data.csv')
read_file = reader(opened_file)
apps_data = list(read_file)


def extract(index):
    my_data = []
    for row in apps_data[1:]:
        value = row[index]
        my_data.append(value)
    return my_data


row = extract(1)
print(row)