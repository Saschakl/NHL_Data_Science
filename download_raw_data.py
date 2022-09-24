import time
import requests
from datetime import datetime
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor


# function to download all files form this site
def download_file(url,file_name):
    # add header to prevent error 403
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    # add login url for all requests
    login_url = "https://www.moneypuck.com"
    # create a requests Session
    requests_session = requests.Session()
    # log in to the requests Session so that you can reuse it
    response = requests_session.post(login_url, headers=headers)
    # the endpoint to the csv file
    download_url = url
    response = requests_session.get(download_url, timeout=(15,15))
    # datetime object containing current date and time
    now = datetime.now()
    # convert to datetime dd/mm/YY H:M:S
    dt_string = now.strftime("%d%m%Y%H%M")
    destination_path = "./raw_data"
    filename = file_name + str(dt_string) + ".csv"
    full_file_path = destination_path + "/" + filename
    print("Downloading %s ..." % full_file_path)

    with open(full_file_path, "wb") as handle:
        for data in response.iter_content():
            handle.write(data)

    print("Download complete for %s!" % full_file_path)
    
def download_period_files(position, start_year, end_year):
    # run function to download files for skaters in certain time period 
    start_year = start_year 
    end_year = end_year
    while start_year <= end_year:
        download_file("https://www.moneypuck.com/moneypuck/playerData/seasonSummary/{}/regular/{}.csv".format(start_year, position), "{}_{}_".format(position, start_year))
        start_year += 1
    

def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()


if __name__ == '__main__':
        
    run_cpu_tasks_in_parallel([
    download_period_files("skaters", 2009, 2019),
    download_period_files("goalies", 2008, 2012),
    download_period_files("lines", 2010, 2013),
    download_period_files("teams", 2016, 2021),
    ])
    
    
    
    