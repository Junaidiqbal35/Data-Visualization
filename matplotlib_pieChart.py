import csv
from collections import Counter
from matplotlib import pyplot as plt


# function for pie_chart
def pie_chart_function():
    plt.style.use("fivethirtyeight")
    # with statement will automatically close the file after the nested block of code
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        """ Counter() Method
            A Counter() is a container that stores elements as dictionary keys, 
            and their counts are stored as dictionary values. 
        """
        language_counter = Counter()
        for row in csv_reader:
            language_counter.update(row['LanguagesWorkedWith'].split(';'))
    languages = []
    popularity = []
    # most_common() use to show data data of top 5 lang
    for item in language_counter.most_common(5):
        languages.append(item[0])
        popularity.append(item[1])
    # Specifies the fraction of the radius with which to offset each wedge.
    explode = [0, 0, 0, 0.1, 0]

    # Autopct parameter  used to label the wedges with their numeric value
    try:
        plt.pie(popularity, labels=languages, explode=explode, shadow=True,
                startangle=90, autopct='%1.1f%%',
                wedgeprops={'edgecolor': 'black'})
    except IOError:
        print(Exception)
    plt.title("Top 5 Programming Pie Chart")
    # tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area
    plt.tight_layout()
    plt.show()


# Calling the function
pie_chart_function()
