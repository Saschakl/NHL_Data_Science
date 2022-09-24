from pip import main
import requests, urllib
from tqdm import tqdm
from datetime import datetime

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
login_url = "https://www.moneypuck.com"
requests_session = requests.Session() # create a requests Session
response = requests_session.post(login_url, headers=headers) # log in to the requests Session so that you can reuse it
download_url = "https://www.moneypuck.com/moneypuck/playerData/seasonSummary/2008/regular/goalies.csv"
response = requests_session.get(download_url, timeout=(15,15))

# function to download all files form this site
def download_file(url,file_name):
    # datetime object containing current date and time
    now = datetime.now()
    # convert to datetime dd/mm/YY H:M:S
    dt_string = now.strftime("%d%m%Y%H%M")
    filename = file_name + str(dt_string) + ".csv"
    print("Downloading %s ..." % filename)

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

    print("Download complete for %s!" % filename)

if __name__ == '__main__':
    
    # run function to download file
    download_file(response.url, "skaters_") 

