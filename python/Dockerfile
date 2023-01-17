FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*ini ./
COPY ./*py ./
CMD ["python","hello-world.py"]
# CMD ["python","write.py"]

# docker build -t python_hello_world .