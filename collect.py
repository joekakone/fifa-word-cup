#!/usr/bin/env python
# coding: utf-8

"""
    Récupération des données sur le FIFA World Cup
    Source: https://www.foxsports.com/soccer/fifa-world-cup/history
"""

import csv
import requests
from bs4 import BeautifulSoup


# PARAMS
BASE_URL = "https://www.foxsports.com/soccer/fifa-world-cup/history"

SOURCE_DIR = "sources/"

MOTHER_BALISE = "table"
MOTHER_CLASS = "wisbb_heStandard"

HEADER_BALISE = "thead"
COLUMN_BALISE = "th"

LINES_BALISE = "tbody"
LINE_BALISE = "tr"
LINE_COL_BALISE = "td"


def get_source(url=None):
    code = requests.get(url)
    return BeautifulSoup(code.text, "html.parser")

def retreive_data(url):
    # html code
    source = get_source(url)
    # table
    table = source.find(MOTHER_BALISE)
    # header
    header = table.find(HEADER_BALISE)
    colnames = [col.text for col in header.find_all(COLUMN_BALISE)]
    # lines
    lines = table.find(LINES_BALISE)
    with open("data/fifa-word-cup-data.csv","w", newline="\n") as f:
        # write header
        f.write(";".join(colnames))
        for line in lines.find_all(LINE_BALISE):
            # parse line
            values = [col.text.replace("\n","") for col in line.find_all(LINE_COL_BALISE)]
            # write line
            f.write("\n"+";".join(values))

if __name__ == "__main__":
    print("Start...")
    retreive_data(BASE_URL)
    print("End...")
