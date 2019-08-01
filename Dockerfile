FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip3 install -r /app/requirements.txt
RUN python3 setup.py install

CMD ["python3" "-m ""squash"]