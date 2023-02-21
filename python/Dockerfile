# https://iotbytes.wordpress.com/create-your-first-docker-container-for-raspberry-pi-to-blink-an-led/
FROM arm64v8/python:3-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*conf ./
COPY ./*py ./
COPY ./meterly ./meterly
CMD ["python","hello-world-2.py"]