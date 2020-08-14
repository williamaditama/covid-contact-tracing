FROM ubuntu:18.04
COPY . /app
RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install -r /app/requirements.txt
CMD python /app/app.py