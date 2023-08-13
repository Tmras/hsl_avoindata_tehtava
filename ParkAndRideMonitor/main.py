import os

import DataFetcher
from config import Configuration

if __name__ == '__main__':
    # Change the working direcotry to the current directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    print(dname)
    os.chdir(dname)

    config = Configuration()
    DataFetcher.poll_data(config.polling_time(), config.facility_ids())


