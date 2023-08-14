import os


def write_to_file(facility_id, max_capacity, currently_used, timestamp):
    data_to_file = f"{facility_id},{max_capacity},{currently_used},{timestamp}"
    hour = timestamp[11:13]
    if not os.path.exists(f"./{facility_id}"):
        os.makedirs(f"./{facility_id}")
    with open(f"{facility_id}/parking_data_{hour}.csv", "a") as file:
        file.write(f"{data_to_file}\n")