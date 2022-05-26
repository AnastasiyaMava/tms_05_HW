FROM python:3.8-slim


COPY . /opt/tms_05_HW

WORKDIR /opt/tms_05_HW

RUN pip install -r requirements.txt

WORKDIR /opt/tms_05_HW/google/

CMD pytest test_google.py

