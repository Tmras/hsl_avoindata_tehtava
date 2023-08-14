import matplotlib.pyplot as plt
import csv


def get_data(area_id):
    hours = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
             "17", "18", "19", "20", "21", "22", "23")
    usage_percentage_list = []

    # calculate average amount of available parking spaces in the given facility by hour
    for hour in hours:
        try:
            with open(f"..//ParkAndRideMonitor/{area_id}/parking_data_{hour}.csv", "r") as data_file:
                lines = csv.reader(data_file, delimiter=',')
                line_count = 0
                percentage_counter = 0
                for row in lines:
                    line_count += 1
                    percentage = (int(row[2])/int(row[1])) * 100
                    percentage_counter += percentage
                usage_percentage_list.append(percentage_counter/line_count)
        except FileNotFoundError as e:
            print(f"File for the hour {hour} does not exist. Availability percentage will be listed as 0.")
            usage_percentage_list.append(0)

    plt.bar(hours, usage_percentage_list, color='b', label="Availability percentage")
    plt.xlabel('Hour')
    plt.ylabel('Availability percentage')
    plt.title('Availability percentage by hour')
    plt.legend()
    plt.show()

