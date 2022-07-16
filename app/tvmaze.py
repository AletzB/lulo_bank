from request_api import Request
from sqllite_db import sqllite_db
import logging
import pandas as pd
import os
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class publicaciones(object):

    def run(self):
        logger.info("Starting the process to download the data from http://api.tvmaze.com ----------------------------------------------------------------------------")
        s_d= Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-01"}, timeout=4)
        response = s_d.parallelize_request()
        logger.info("Starting the process to load the data to the database -------------------------------------------------------------------------------------------")
        dataset = pd.read_parquet("app/data.parquet").reset_index().drop(['index'], axis=1)
        #dataset = pd.read_parquet("data.parquet").reset_index().drop(['index'], axis=1)
        self.__load_data(dataset)
       

    def __load_data(self, data):
        db = sqllite_db('SHOWS')
        db.init_table()
        logger.info("Bulk loading to the database: tvshows.sqlite")
        db.bulk_data(data)
        logger.info(" {c} records were downloaded from http://api.tvmaze.com and loaded to the database {d}".format(c= db.validate(), d = 'tvshows.sqlite'))


if __name__ == '__main__':

    logger.info(" Getting data from http://api.tvmaze.com")
    publicaciones().run()
    logger.info(" End of program")

