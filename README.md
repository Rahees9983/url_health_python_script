# Check URL health using a Python script and Monitor Python script using DataDog
## Create virtual environment and activate it 
* apt update
* apt install python3.8-venv
* python3 -m venv url_health_check_venv
* source url_health_check_venv/bin/activate

## Install required Modules
pip install -r requirements.txt

## Usage 
```
python webMonitor.py [-h] -c CONFIG [-i INTERVAL]

options:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Configuration file path
  -i INTERVAL, --interval INTERVAL
                        Interval between checks in seconds
```

## Run
### You can run the script with below command:
```
python webMonitor.py -c config.json -i 3
```
### DataDog
#### I have used DataDog for monitoring the python script itself
I have created a Virtual Machine on Azure Cloud to execute the script and used a DataDog free trial account for monitoring the health of script.
Steps followed for Integration Azure Virtual machine with DataDog are below.

1. Installed the DataDog agent on the Virtual Machine name (fluent-docker)
2. Confured the DataDog agent configurations using /etc/datadog-agent/datadog.yaml
  #### changes made are below
  Created a python.d/ folder in the conf.d/ Agent configuration directory.
  Created a file conf.yaml in the conf.d/python.d/ directory with the following content
  ```
 (myvenv) root@fluent-docker:/home/raheeskhan9983/testcrew/url_health_python_script# cat /etc/datadog-agent/conf.d/python.d/conf.yaml 
  ##Log section
  logs:
    - type: file
      path: "/home/raheeskhan9983/testcrew/monitor.log"
      service: "rahees_url_check"
      source: python
      sourcecategory: sourcecode
  ```
3. Add below configration to the /etc/datadog-agent/datadog.yaml file
    ```
    logs_enabled: true
    process_config:
      process_collection:
      enabled: true
    ```    
5.  `sudo service datadog-agent restart`
6.  `sudo systemctl status datadog-agent`

## DataDog Monitor and Alert
1. I am monitoring the process running the webMonitor.py script

  <img width="1425" alt="image" src="https://github.com/Rahees9983/url_health_python_script/assets/38326225/992b7292-1705-485e-87f2-c3a7e122017e">


2. Logs are also available at the DataDog console

  <img width="1433" alt="image" src="https://github.com/Rahees9983/url_health_python_script/assets/38326225/30d847b2-fa64-4d46-a2c3-035b7483c695">



3. ```
   I have created a monitor to check the health status of my webMonitor.py script if script is down or in failed state.
   Monitor will raise and alert at khanrahees333@gmail.com
   Monitor name:- webMonitor heatlh check
   ```
  <img width="1432" alt="image" src="https://github.com/Rahees9983/url_health_python_script/assets/38326225/413d1598-457a-4792-af4c-68c493823935">


4. Now I will stop the execution of the webMonitor.py script and I will get an alert on my email khanrahees333@gmail.com

  <img width="884" alt="image" src="https://github.com/Rahees9983/url_health_python_script/assets/38326225/b2470b26-85e4-4b24-a3d4-a43cfb7e8465">

