FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip3 install -r /app/requirements.txt
RUN python3 setup.py install

ENV SQUASH_PORT 8899
EXPOSE $SQUASH_PORT

CMD ["python3", "-m", "squash"]