# csv library to work with csv files
import csv
# Collections in Python are containers that are used to store collections of data e.g dict.
from collections import Counter
# python library used to work with data visualization
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
try:
    with open('data.csv') as csv_file:

        # DictReader class basically creates a CSV object that behaves like a Python OrderedDict
        csv_reader = csv.DictReader(csv_file)
        """ Counter() method
            A Counter() is a container that stores elements as dictionary keys, 
            and their counts are stored as dictionary values.
         """
        language_counter = Counter()

        for row in csv_reader:
            """
             An  language_counter populated via the update() method of Counter().
             The split() method splits a string into a list here were are using semi-colon as a separator. 
            """
            try:
                language_counter.update(row['LanguagesWorkedWith'].split(';'))
            except Exception:
                print(" Handling null value in the file ")

    # using languages and popularity list to separate the data, that save in language_counter.
    languages = []
    popularity = []
    # most_common() use to show data data of top 15 lang
    for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])

    languages.reverse()  # reverse() the list most popular lang on top
    popularity.reverse()

    # barh method showing data in horizontal bars
    plt.barh(languages, popularity)

    plt.title("Most Popular Languages Survey May 2019")
    # x-axis
    plt.xlabel("Number of People Who Use")

    # tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area
    plt.tight_layout()

    # open interactive windows that display your figure
    plt.show()

except FileNotFoundError:
    print(" Error While Opening the File or file not found ")
