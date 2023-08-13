import os


def write_to_file(id, max_capacity, currently_used, timestamp):
    data_to_file = f"{id},{max_capacity},{currently_used},{timestamp}"
    hour = timestamp[11:13]
    if not os.path.exists(f"./{id}"):
        os.makedirs(f"./{id}")
    with open(f"{id}/parking_data_{hour}.csv", "a") as file:
        file.write(f"{data_to_file}\n")