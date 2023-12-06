import random as r

# Range for data gathered from 2008, 2012 and 2016 olympic games
# 2016 - https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table
# 2012 - https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table
# 2008 - https://en.wikipedia.org/wiki/2008_Summer_Olympics_medal_table

"""
Ranges per country(gold, silver, bronze)
USA: 36-48, 22-37, 30-38
GB: 19-29, 13-23, 17-19
AUS: 8-14, 11-15, 10-17 
JP: 7-12, 8-14, 8-21
GER: 11-17, 10-20, 13-15
"""

def get_country_list():
    return ["Great Britain", "Australia", "Japan", "Germany"]


def get_year_list():
    return ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

def get_5_american_years():
    return [[r.randint(36, 48), r.randint(36, 48), r.randint(36, 48), r.randint(36, 48), r.randint(36, 48)],
            [r.randint(22, 37), r.randint(22, 37), r.randint(22, 37), r.randint(22, 37), r.randint(22, 37)],
            [r.randint(30, 38), r.randint(30, 38), r.randint(30, 38), r.randint(30, 38), r.randint(30, 38)]]

def get_gold_medal_data():
    return [ r.randint(13, 22), r.randint(8, 14), r.randint(7, 12), r.randint(11, 17)]

def get_silver_medal_data():
    return [ r.randint(13, 23), r.randint(11, 15), r.randint(8, 14), r.randint(10, 20)]

def get_bronze_medal_data():
    return [r.randint(12, 19), r.randint(10, 17), r.randint(8, 21), r.randint(13, 15)]

