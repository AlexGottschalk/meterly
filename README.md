
# Development of an open source solution for reading analogue Ferraris electricity meters, including the creation of a dashboard to visualise consumption.

*How can a [Raspberry Pi](https://www.raspberrypi.com/) be used to read an analogue Ferraris electricity meter and store and visualise the consumption data?*


## Hardware used:

* [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-4gb) (4 GB) with power adapter
* Jumper cable
* TCRT5000 optical sensor


## Installation steps:

1. Install an [operating system](https://www.raspberrypi.com/software/operating-systems/).  
**Note**: The project was developed and tested under *Raspberry Pi OS Lite (64-bit)*.
2. Enable [remote access via SSH](https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh) on your Raspberry Pi.  
**Note**: When installing with the [Raspberry Pi Imager](https://www.raspberrypi.com/software/),
SSH remote access can already be enabled during the installation.
3. Connect to your Raspberry Pi via SSH
using [Linux, Mac OS](https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-linux-or-mac-os)
or [Windows](https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-windows-10).
4. Install [Docker on your Raspberry Pi](https://raspberrytips.com/docker-on-raspberry-pi/).


