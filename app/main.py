
import math
import requests
import os
import logging
import json
import multiprocessing as mp
from timer import timer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def request_json(id_archivo, position_start, position_end):
    
    url="http://api.tvmaze.com/schedule/web"
    logger.info(" Requesting json from {}".format(id_archivo))

    try:
        for i in range (position_start, position_end):
                args={"date":f"2020-12-0{i+1}"} if i+1 < 10 else {"date":f"2020-12-{i+1}"}
                response = requests.get(url, params=args)
                if response.status_code == 200:
                    response_json = response.json()
                    jsonString = json.dumps(response_json)
                    with open(f'api/json_response/{args["date"]}.json', 'w') as f:
                        f.write(jsonString)
                    logger.info(" Download success for " + args["date"])
                else:
                    logger.error("Error: " + response.status_code)

    except Exception as e:
        logger.error(e)
        
    
@timer('function:main', unit='s')
def main():

    logger.info(' Starting...')

    if not os.path.exists("api/json_response"):
        try:
            os.makedirs("api/json_response")
        except OSError:
            logger.error("Error: Creating directory. " + os.path.dirname("json_response"))
        
    cores = mp.cpu_count() 
    days = 31
    pool = mp.Pool(cores)
    jobs = []

    logger.info(f'Runinng on {cores} CPU')

    id_archivo = 0
    position_start = 0
    position_end = 0
    count = math.ceil(days/cores)
  
    for i in range(cores):     
        try:
            id_archivo +=1
            position_end+=count
            logger.info(f'Request {id_archivo} in position {position_end}')
            jobs.append(pool.apply_async(request_json, args=(id_archivo, position_start, position_end)))
            position_start = position_end
            
        except Exception as e:
            logger.error (e)

    cont = 0
    for job in jobs:
        cont += 1
        job.get() 
    pool.close()

    logger.info(' Ending...')


if __name__ == '__main__':
    main()
