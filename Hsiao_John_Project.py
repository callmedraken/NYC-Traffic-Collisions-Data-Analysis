### John Hsiao
### Data Mining Project

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def readFila(file):
    data = pd.read_csv(file, low_memory=False)
    data.columns = data.columns.str.replace('\s+', '_')
    return data

# determine how many accidents occurred in a certain month
def analyzeMonth(data):
    months = {
        "jan":0,
        "feb":0,
        "mar":0,
        "apr":0,
        "may":0,
        "june":0,
        "jul":0,
        "aug":0,
        "sep":0,
        "oct":0,
        "nov":0,
        "dec":0,
    }
    # find number of accidents in each month of the year
    for col in data.DATE:
        if col[:2] == "01":
            months["jan"] += 1
        elif col[:2] == "02":
            months["feb"] += 1
        elif col[:2] == "03":
            months["mar"] += 1
        elif col[:2] == "04":
            months["apr"] += 1
        elif col[:2] == "05":
            months["may"] += 1
        elif col[:2] == "06":
            months["june"] += 1
        elif col[:2] == "07":
            months["jul"] += 1
        elif col[:2] == "08":
            months["aug"] += 1
        elif col[:2] == "09":
            months["sep"] += 1
        elif col[:2] == "10":
            months["oct"] += 1
        elif col[:2] == "11":
            months["nov"] += 1
        elif col[:2] == "12":
            months["dec"] += 1
    # graph it
    plt.bar(range(len(months)), list(months.values()), align='center')
    plt.xticks(range(len(months)), list(months.keys()))
    plt.title("Accidents in a month")
    plt.xlabel("Month")
    plt.ylabel("Number of accidents")
    plt.show()
    # store in a text document
    fout = "months.txt"
    fo = open(fout, "w")
    for k, v in months.items():
        fo.write(str(k) + ' >>> ' + str(v) + '\n\n')
    fo.close()

def analyzeTime(data):
    time = {
        "am":0,
        "pm":0,
    }
    for col in data.TIME:
        if len(col) == 4:
            time["am"] += 1
        else:
            if int(col[:2]) < 12:
                time["am"] += 1
            else:
                time["pm"] += 1
    plt.bar(range(len(time)), list(time.values()), align='center')
    plt.xticks(range(len(time)), list(time.keys()))
    plt.title("Time Accidents occur")
    plt.xlabel("AM vs PM")
    plt.ylabel("Number of accidents")
    plt.show()
    fout = "time.txt"
    fo = open(fout, "w")
    for k, v in time.items():
        fo.write(str(k) + ' >>> ' + str(v) + '\n\n')
    fo.close()

def analyzeBoroughs(data):
    borough = {
        "Queens":0,
        "Manhattan":0,
        "Brooklyn":0,
        "StatenIsland":0,
        "Bronx":0,
        "NA":0,
    }
    for col in data.BOROUGH:
        if col == "QUEENS":
            borough["Queens"] += 1
        elif col == "BRONX":
            borough["Bronx"] += 1
        elif col == "MANHATTAN":
            borough["Manhattan"] += 1
        elif col == "STATEN ISLAND":
            borough["StatenIsland"] += 1
        elif col == "BROOKLYN":
            borough["Brooklyn"] += 1
        else:
            borough["NA"] += 1
    labels = 'Queens', 'Manhattan', 'Brooklyn', 'StatenIsland', 'Bronx', 'NA'
    sizes = list(borough.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')
    plt.title("Percent of accidents that occur in each borough")
    plt.show()
    fout = "boroughs.txt"
    fo = open(fout, "w")
    for k, v in borough.items():
        fo.write(str(k) + ' >>> ' + str(v) + '\n\n')
    fo.close()

def boroughYears(data):
    yr2012 = {
        "Queens":0,
        "Manhattan":0,
        "Brooklyn":0,
        "StatenIsland":0,
        "Bronx":0,
        "NA":0,
    }
    yr2013 = {
        "Queens": 0,
        "Manhattan": 0,
        "Brooklyn": 0,
        "StatenIsland": 0,
        "Bronx": 0,
        "NA": 0,
    }
    yr2014 = {
        "Queens": 0,
        "Manhattan": 0,
        "Brooklyn": 0,
        "StatenIsland": 0,
        "Bronx": 0,
        "NA": 0,
    }
    yr2015 = {
        "Queens": 0,
        "Manhattan": 0,
        "Brooklyn": 0,
        "StatenIsland": 0,
        "Bronx": 0,
        "NA": 0,
    }
    yr2016 = {
        "Queens": 0,
        "Manhattan": 0,
        "Brooklyn": 0,
        "StatenIsland": 0,
        "Bronx": 0,
        "NA": 0,
    }
    yr2017 = {
        "Queens": 0,
        "Manhattan": 0,
        "Brooklyn": 0,
        "StatenIsland": 0,
        "Bronx": 0,
        "NA": 0,
    }
    yr2018 = {
        "Queens": 0,
        "Manhattan": 0,
        "Brooklyn": 0,
        "StatenIsland": 0,
        "Bronx": 0,
        "NA": 0,
    }
    df = data[['DATE', 'BOROUGH']]
    for row in df.itertuples():
        yr = getattr(row, "DATE")
        br = getattr(row, "BOROUGH")
        if yr[-2:] == "12":
            byLoop(br, yr2012)
        elif yr[-2:] == "13":
            byLoop(br, yr2013)
        elif yr[-2:] == "14":
            byLoop(br, yr2014)
        elif yr[-2:] == "15":
            byLoop(br, yr2015)
        elif yr[-2:] == "16":
            byLoop(br, yr2016)
        elif yr[-2:] == "17":
            byLoop(br, yr2017)
        else:
            byLoop(br, yr2018)
    ind = np.arange(len(yr2012))
    plt.bar(ind, list(yr2012.values()), .1, color='r', label='2012')
    plt.bar(ind + .1, list(yr2013.values()), .1, color='g', label='2013')
    plt.bar(ind + .2, list(yr2014.values()), .1, color='b', label='2014')
    plt.bar(ind + .3, list(yr2015.values()), .1, color='y', label='2015')
    plt.bar(ind + .4, list(yr2016.values()), .1, color='m', label='2016')
    plt.bar(ind + .5, list(yr2017.values()), .1, color='c', label='2017')
    plt.bar(ind + .6, list(yr2018.values()), .1, color='k', label='2018')
    plt.xticks(range(len(yr2012)), list(yr2012.keys()))
    plt.title("Accidents in a year in each borough")
    plt.xlabel("Borough")
    plt.ylabel("Number of accidents")
    plt.legend()
    print(yr2012, yr2013, yr2014, yr2015, yr2016, yr2017, yr2018)
    plt.show()


def byLoop(br, dict):
    if br == "QUEENS":
        dict["Queens"] += 1
    elif br == "MANHATTAN":
        dict["Manhattan"] += 1
    elif br == "BROOKLYN":
        dict["Brooklyn"] += 1
    elif br == "STATEN ISLAND":
        dict["StatenIsland"] += 1
    elif br == "BRONX":
        dict["Bronx"] += 1
    else:
        dict["NA"] += 1


def analyzeContributingFactors(data):
    factors = {
    }
    for col in data.CONTRIBUTING_FACTOR_VEHICLE_1:
        if col in factors:
            factors[col] += 1
        else:
            factors[col] = 1
    for col in data.CONTRIBUTING_FACTOR_VEHICLE_2:
        if col in factors:
            factors[col] += 1
        else:
            factors[col] = 1
    for col in data.CONTRIBUTING_FACTOR_VEHICLE_3:
        if col in factors:
            factors[col] += 1
        else:
            factors[col] = 1
    for col in data.CONTRIBUTING_FACTOR_VEHICLE_4:
        if col in factors:
            factors[col] += 1
        else:
            factors[col] = 1
    for col in data.CONTRIBUTING_FACTOR_VEHICLE_5:
        if col in factors:
            factors[col] += 1
        else:
            factors[col] = 1
    x = pd.DataFrame(data=factors, index=list('#'))
    tot = sum(factors.values())
    for key, val in factors.items():
        if (val/tot) > .0005:
            print('{}\t{}'.format(key, val))

def analyzeVehicle(data):
    vehicle = {
    }
    for col in data.VEHICLE_TYPE_CODE_1:
        if col in vehicle:
            vehicle[col] += 1
        else:
            vehicle[col] = 1
    for col in data.VEHICLE_TYPE_CODE_2:
        if col in vehicle:
            vehicle[col] += 1
        else:
            vehicle[col] = 1
    for col in data.VEHICLE_TYPE_CODE_3:
        if col in vehicle:
            vehicle[col] += 1
        else:
            vehicle[col] = 1
    for col in data.VEHICLE_TYPE_CODE_4:
        if col in vehicle:
            vehicle[col] += 1
        else:
            vehicle[col] = 1
    for col in data.VEHICLE_TYPE_CODE_5:
        if col in vehicle:
            vehicle[col] += 1
        else:
            vehicle[col] = 1
    while len(vehicle) > 20:
        kmin = min(vehicle.keys(), key=lambda k: vehicle[k])
        del vehicle[kmin]
    plt.barh(range(len(vehicle)), list(vehicle.values()), align='center')
    plt.yticks(range(len(vehicle)), list(vehicle.keys()))
    plt.title("Accidents by vehicle type")
    plt.xlabel("Number of accidents")
    plt.ylabel("Vehicle")
    plt.rc('ytick', labelsize=4)
    plt.show()

def main():
    file = "NYPD_Motor_Vehicle_Collisions.csv"
    data = readFila(file)
    analyzeVehicle(data)

main()