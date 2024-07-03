import requests
import json
import time
import logging
import argparse
import threading


logging.basicConfig(filename='monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def sendHealthStatus():
    while True:
        logging.info(f"Health OK")
        time.sleep(2)

def check_website(url, content):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if content in response.text:
            logging.info(f"SUCCESS: {url} - Response time: {end_time - start_time:.2f}s")
        else:
            logging.warning(f"CONTENT MISMATCH: {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"CONNECTION ERROR: {url} - {str(e)}")

def main(config_file, interval):
    config = load_config(config_file)

    healthThread = threading.Thread(target=sendHealthStatus)
    healthThread.start()
    
    while True:
        for site in config['sites']:
            check_website(site['url'], site['content'])
        
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Monitoring Tool')
    parser.add_argument('-c', '--config', type=str, required=True, help='Configuration file path')
    parser.add_argument('-i', '--interval', type=int, default=60, help='Interval between checks in seconds')
    args = parser.parse_args()
    
    main(args.config, args.interval)

