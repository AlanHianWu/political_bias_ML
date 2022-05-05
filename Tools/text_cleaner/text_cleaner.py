import sys
import csv
import pandas as pd

#tsv_file = open("articles_data.tsv")
#read_tsv = csv.reader(tsv_file, encoding="cp1252", delimiter="\t")

#read_tsv = pd.read_csv("articles_data.tsv", encoding="cp1252")
#read_tsv = pd.read_csv("articles_data.tsv")

#for row in read_tsv:
    #print(row)


def clean_file(file):
    output_rows = []
    with open('articles_data.tsv', encoding="utf8", errors="ignore") as f:
        #reader = csv.reader(f, dialect='excel-tab')
        #reader = csv.reader(f, encoding='latin1')
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            output_rows.append(row)

    with open('cleaned_text.tsv', 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        for row in output_rows:
            tsv_writer.writerow(row)



if __name__ == "__main__":
    clean_file(sys.argv[1])


