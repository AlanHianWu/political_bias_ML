import sys
import csv
import pandas as pd
from operator import itemgetter

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

def remove_dups(file):
    output_rows = []
    with open(file, encoding="utf8", errors="ignore") as f:
        #reader = csv.reader(f, dialect='excel-tab')
        #reader = csv.reader(f, encoding='latin1')
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row in output_rows:
                pass
            elif row[0] == "":
                pass
            else:
                output_rows.append(row)

    with open('cleaned_text.tsv', 'wt', newline='') as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        for row in output_rows:
            tsv_writer.writerow(row)

def split_five(file):
    split_file = []
    with open(file, encoding="utf8", errors="ignore") as f:
        #reader = csv.reader(f, dialect='excel-tab')
        #reader = csv.reader(f, encoding='latin1')
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            split_file.append(row)
    print(len(split_file))

    sorted(split_file, key=itemgetter(1))
    containers = len(split_file) // 5
    five = [containers, containers*2, containers*3, containers*4]
    res = [split_file[i : j] for i, j in zip([0] + five, five + [None])]
    fixed_five = []
    for i in range(len(res)):
        for row in res[i]:
            fixed_five.append([row[0], i])

    with open('split_text.tsv', 'wt', newline="") as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        for row in fixed_five:
            tsv_writer.writerow(row)

def truncate(file):
    output_rows = []
    with open(file, encoding="utf8", errors="ignore") as f:
        #reader = csv.reader(f, dialect='excel-tab')
        #reader = csv.reader(f, encoding='latin1')
        reader = csv.reader(f, delimiter="\t")

        for row in reader:
            res = split_all(row)
            for rows in res:
                output_rows.append(rows)
    
    with open('truncate_text.tsv', 'wt', newline="") as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        for row in output_rows:
            tsv_writer.writerow(row)

def split_all(row):
    res = []
    truncated = row[0].split()
    word_max = 400
    new = []
    for word in truncated:
        if word_max > 0:
            word_max = word_max - len(word)
            new.append(word)
        else:
            res.append([" ".join(new), row[1]])
            word_max = 400
            new = []

    return res
            
        


if __name__ == "__main__":
    # clean_file(sys.argv[1])
    # remove_dups(sys.argv[1])
    # split_five(sys.argv[1])
    truncate(sys.argv[1])
    with open("truncate_text.TSV", encoding="utf8", errors="ignore") as f:
            #reader = csv.reader(f, dialect='excel-tab')
            #reader = csv.reader(f, encoding='latin1')
            reader = csv.reader(f, delimiter="\t")
            lens = []
            for row in reader:
                lens.append(len(row[0]))
    print(max(lens))