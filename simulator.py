import json
from datetime import timedelta
import datetime
import csv
import argparse
import time


time_start = datetime.datetime.now()
time_end = datetime.datetime(2018, 12, 1)
current_time = time_start
csv_name = ''
total = 0
quiet = False
gui = False
timestamp = 60
consumption = 0.00
signal = ""
start_time = time.time()

def signal_received(signal_rec):
    global signal
    signal = signal_rec


def consumption_changed(consumption_received):
    #consumption per hour
    global consumption
    consumption = (consumption_received / 1000)/60


def get_price(list_time, time_t):
    for hour in list_time:
        for key in hour.keys():
            key = key
        if key == str(time_t):
            key = key
            break
    for hour in list_time:
        if key in hour:
            return hour[key]


def current_timepricing(list_time_converted, current_t):
    time_t = list_time_converted[-1]
    for i in range(len(list_time_converted)):
        if i + 1 < len(list_time_converted):
            if list_time_converted[i] <= current_t < list_time_converted[i + 1]:
                time_t = list_time_converted[i]
    return time_t


def create_list_of_time(list_time):
    list_time_converted = []
    for hour in list_time:
        for key in hour.keys():
            key = key
        hour = key.split(":")
        new_time = datetime.time(int(hour[0]), int(hour[1]), int(hour[2]))
        list_time_converted.append(new_time)
    return list_time_converted


def create_datetime(string_date):
    string_date = string_date.split(".")
    new_date = datetime.datetime(int(string_date[2]), int(string_date[1]), int(string_date[0]))
    return new_date


def generate_timestamp(timestamp):
    global current_time
    list_of_datetimes = []
    while current_time < time_end:
        current_time = current_time + timedelta(seconds=timestamp)
        list_of_datetimes.append(current_time)
    return list_of_datetimes


def generate_profile(current_date, timeline):
    profile = timeline[-1]['profile']
    for i in range(len(timeline)):
        if timeline[i]['date']:
            date = timeline[i]['date']
            if i+1 < len(timeline):
                this_date = create_datetime(date).date()
                next_date = create_datetime(timeline[i+1]['date']).date()
                if this_date < current_date < next_date:
                    profile = timeline[i]['profile']
    return profile


def write_to_csv(current_time_csv, price, consumption, total, passed_time):
    with open(csv_name, 'a') as consumption_csv:
        filewriter = csv.writer(consumption_csv, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([current_time_csv, passed_time,  price, consumption,  price*consumption, total])
    consumption_csv.close()


def total_price():
    total = 0
    with open('csv_name', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row):
                if row[-2] != 'current consumption price':
                    total += float(row[-2])
    return total


def calculation(json_data, pricing, current_time_calculation):
    # current_time_calculation = current_time_calculation + timedelta(seconds=timestamp)
    time_t = current_time_calculation.time()
    profile = generate_profile(current_time_calculation.date(), json_data['timeline'])
    list_time_converted = create_list_of_time(pricing[profile])
    time_t = current_timepricing(list_time_converted, time_t)
    price = get_price(pricing[profile], time_t)
    global total
    total += consumption * price
    # total = total_price()
    if not quiet:
        passed_time = time.time() - start_time
        if csv_name:
            write_to_csv(current_time_calculation, price, consumption, total, passed_time)
        else:
            print(current_time_calculation, passed_time, price, consumption, price*consumption, total)

# wait parametar
# read only from json
def start_2(gui_command):
    global time_end
    with open('v2/dvotarifno.json') as type:
        json_data = json.load(type)
        pricing = json_data['pricing']

    if csv_name:
        with open(csv_name, 'w') as consumption_csv:
            filewriter = csv.writer(consumption_csv, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['date', 'timestamp',  'current price', 'consumption', 'current consumption price', 'total'])
        consumption_csv.close()
    global current_time
    if gui_command:
        for date in json_data['timeline']:
            current_time = create_datetime(date['date'])
            time_end = current_time + datetime.timedelta(days=1)
            while current_time < time_end:
                if signal == "stop":
                    break
                elif signal == "pause":
                    while signal == "pause":
                        continue
                else:
                    calculation(json_data, pricing, current_time)
                    time.sleep(1)
                    current_time = current_time + datetime.timedelta(seconds=timestamp)
    else:
        for date in json_data['timeline']:
            current_time = create_datetime(date['date'])
            time_end = current_time + datetime.timedelta(days=1)
            while current_time < time_end:
                calculation(json_data, pricing, current_time)
                time.sleep(1)
                current_time = current_time + datetime.timedelta(seconds=timestamp)


# start from current date
def start(gui_command):
    with open('v2/dvotarifno.json') as type:
        json_data = json.load(type)
        pricing = json_data['pricing']

    if csv_name:
        with open(csv_name, 'w') as consumption_csv:
            filewriter = csv.writer(consumption_csv, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['date', 'timestamp', 'current price', 'consumption', 'current consumption price', 'total'])
        consumption_csv.close()
    global current_time
    if gui_command:
        current_time = datetime.datetime.now()
        calculation(json_data, pricing, current_time)
    else:
        while current_time < time_end:
            calculation(json_data, pricing, current_time)
            for i in range(timestamp):
                time.sleep(1)
            current_time = datetime.datetime.now()


def main(timestamp_m, csv_name_m, quiet_m, gui_command):
    global timestamp, consumption, csv_name, quiet, start_time
    start_time = time.time()
    timestamp = timestamp_m
    csv_name = csv_name_m
    quiet = quiet_m

    parser = argparse.ArgumentParser()
    parser.add_argument("--res", help="resolution")
    parser.add_argument("--o", help="output file name")
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()
    if args.res:
        timestamp = int(args.res)
    if args.o:
        csv_name = args.o
    if args.quiet:
        quiet = True
    start_2(gui_command)


if __name__ == "__main__":
    main(timestamp, "", False, False)
