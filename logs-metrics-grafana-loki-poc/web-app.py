import requests
import json
import time
import logging
import argparse
import threading

def load_config(config_file):
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def sendHealthStatus():
    """Send periodic health status logs."""
    while True:
        logging.info("Health status: OK")
        time.sleep(2)

def check_website(url, content, env):
    """Check the website and log the result with environment information."""
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if content in response.text:
            logging.info(f"url: {url} - status: SUCCESS - response_time: {end_time - start_time:.2f}s - env: {env}")
        else:
            logging.warning(f"url: {url} - status: CONTENT MISMATCH - env: {env}")
    except requests.exceptions.RequestException as e:
        logging.error(f"url: {url} - status: CONNECTION ERROR - error: {str(e)} - env: {env}")

def main(config_file, interval):
    """Main function to read config and start monitoring."""
    config = load_config(config_file)

    # Set up logging configuration with key-value pair format and no milliseconds
    logging.basicConfig(
        filename='monitor.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Start health status thread
    healthThread = threading.Thread(target=sendHealthStatus)
    healthThread.start()
    
    # Main monitoring loop
    while True:
        for site in config['sites']:
            # Pass the environment value from the config to the check_website function
            check_website(site['url'], site['content'], site['env'])
        
        time.sleep(interval)

if __name__ == "__main__":
    # Argument parsing for config file and interval
    parser = argparse.ArgumentParser(description='Web Monitoring Tool')
    parser.add_argument('-c', '--config', type=str, required=True, help='Configuration file path')
    parser.add_argument('-i', '--interval', type=int, default=60, help='Interval between checks in seconds')
    args = parser.parse_args()
    
    main(args.config, args.interval)
