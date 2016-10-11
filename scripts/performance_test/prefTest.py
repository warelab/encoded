import boto3
import getpass
import re
import subprocess
import sys
import datetime
import json
import urllib

def get_status(url):
    url = url+"/_indexer"
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    return data["status"]

def index_timer(url): 
    status = get_status(url)
        if status == "waiting":
            print("Instance is in the wating state: cannot time the indexing")
        else: # might want to push to a log eventually
            print("Indexing Start Time: %s " % datetime.datetime.now())
            while status == "indexing":
                status = get_status(url)
            print("Indexing End Time: %s " % datetime.datetime.now())

def releseanator(url, accession):
    process = subprocess.call('time python3 py_encoded_tools/ENCODE_patch_set.py --key test --accession '+accession+' --field aliases:encode --data "test:Preformance" --update', shell=True)

def python_get(url):
     process = subprocess.call('python3 get.py '+url,shell=True)

def run(index_time, url, locust, accession):
    if index_time:
        index_timer(url)
    releseanator(url, accession)
    python_get(url)
        
def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Test instance with automation",
    )
    parser.add_argument('-t', '--index-time', default='store_true', help="Yes or No to recored indexing time")
    parser.add_argument('--url', default='https://test.encodedcc.org')
    parser.add_argument('--locust', action='store_true', help="locust file")
    parser.add_argument('--accession', default='ENCFF445ANP', help="accession code")
    
    args = parser.parse_args()

    return run(**vars(args))


if __name__ == '__main__':
    main()
