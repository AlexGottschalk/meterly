# https://iotbytes.wordpress.com/create-your-first-docker-container-for-raspberry-pi-to-blink-an-led/
FROM python:3-bullseye
#FROM arm64v8/python:3-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*conf ./
COPY ./*py ./
COPY ./meterly ./meterly
CMD ["python","write.py"]