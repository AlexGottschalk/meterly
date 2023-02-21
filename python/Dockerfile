FROM python:3-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*conf ./
COPY ./*py ./
COPY ./meterly ./meterly
CMD ["python","main.py"]

# docker build -t python_hello_world .