
# Development of an open source solution for reading analogue Ferraris electricity meters, including the creation of a dashboard to visualise consumption.

*How can a [Raspberry Pi](https://www.raspberrypi.com/) be used to read an analogue Ferraris electricity meter and store and visualise the consumption data?*

## Short (functional) description:



## Hardware used:

* [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-4gb) (4 GB) with power adapter
* Jumper cable
* TCRT5000 optical sensor

### Wiring:
![Connecting the sensor module to the Raspberry Pi](/images/circuit.png "San Juan Mountains")


## Software used:

* [**Docker**](https://www.docker.com/)
* [**InfluxDB**](https://www.influxdata.com/) as an [InfluxDB docker container](https://hub.docker.com/_/influxdb) (data storage and data visualisation)
* [**Python**](https://www.python.org/) as a [Python docker container](https://hub.docker.com/_/python) (data collection)


### Configuration:
The **[python.conf](https://github.com/AlexGottschalk/emit/blob/main/python/python.conf)** file is used to access the sensor module and the database. The pin to which the output of the sensor module is connected must be specified in the file. You must also specify the number of revolutions per kilowatt hour of the Ferraris electricity meter. The sampling rate can be left as it is. All other properties can be left as they are.

The **[.env](https://github.com/AlexGottschalk/emit/blob/main/.env)** file is used to initialise the InfluxDB instance (username, password, access token, port, ...). All properties can theoretically be left as they are. However, it is strongly recommended to change the username, password and access token.

Since I have not yet found a way to pass the environment variables from the [.env](https://github.com/AlexGottschalk/emit/blob/main/.env) file to the [python.conf](https://github.com/AlexGottschalk/emit/blob/main/python/python.conf) file, the configuration of overlapping properties has to be done twice. This affects the InfluxDB _organisation_, _url (port)_ and access _token_.

### Installation steps:

1. Install an [operating system](https://www.raspberrypi.com/software/operating-systems/).  
**Note**: The project was developed and tested under *Raspberry Pi OS Lite (64-bit)*.
2. Enable [remote access via SSH](https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh) on your Raspberry Pi.  
**Note**: When installing with the [Raspberry Pi Imager](https://www.raspberrypi.com/software/),
SSH remote access can already be enabled during the installation.
3. Connect to your Raspberry Pi via SSH
using [Linux, Mac OS](https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-linux-or-mac-os)
or [Windows](https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-windows-10).
4. Install [Docker on your Raspberry Pi](https://raspberrytips.com/docker-on-raspberry-pi/).



7. Go to the desired directory
8. Make the InfluxDB init script executable (to be on the safe side):  
```chmod +x ./influxdb/scripts/init.sh```
9. Start the container structure:  
```docker compose up --build```

***

### Save template changes:
To save changes to InfluxDB components, i.e. dashboards, tasks and so on, you need to export them as a template. When the container is reset, the template can be loaded initially with an [init script](https://github.com/AlexGottschalk/emit/blob/main/influxdb/scripts/init.sh).

1. Open the terminal of the InfluxDB docker container.
2. Create a configuration for CLI:  
```influx config create --config-name your_config --host-url http://localhost:8086 --org your_org --token your_token --active```
3. Export (Buckets, Tasks, Dashboards, …) as a new template:  
```influx export all -o your_org -t your_token -f ~/your_template.yml --filter=labelName=your_label```
4. Find out your InfluxDB docker container ID:
```docker container ls```
5. Retrieve the exported template file from the InfluxDB docker container:
```docker cp `your_container_id:/root/your_template.yml ./```


### Examples of extending the solution with additional components:
- [Running InfluxDB 2.0 and Telegraf Using Docker](https://www.influxdata.com/blog/running-influxdb-2-0-and-telegraf-using-docker/)
- [Install Grafana/InfluxDB/Telegraf using Docker Compose](https://dev.to/project42/install-grafana-influxdb-telegraf-using-docker-compose-56e9)
