# Use the appropriate Docker Hub repository (https://hub.docker.com/_/python) for your CPU architecture.
FROM arm64v8/python:3-bullseye

# PYTHONUNBUFFERED with a non-zero value sends Python output
# directly to the terminal without buffering, allowing real-time
# monitoring of an application's output in a container log.
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Installation of all required libraries.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all required Python files.
COPY ./*conf ./
COPY ./*py ./
COPY ./meterly ./meterly
CMD ["python","main.py"]

# Further information:
# https://iotbytes.wordpress.com/create-your-first-docker-container-for-raspberry-pi-to-blink-an-led/