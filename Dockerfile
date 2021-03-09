FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN mkdir /var/tmp/src
RUN chmod 777 /var/tmp/src
COPY src/modulos /var/tmp/src/modulos
RUN pip3 install -r /var/tmp/src/modulos
COPY src/main.py /var/tmp/src/main.py
COPY src/testSheets-3547a5e53a01.json /var/tmp/src/testSheets-3547a5e53a01.json
RUN python3 /var/tmp/src/main.py
RUN rm -rf /var/tmp/src/main.py /var/tmp/testSheets-3547a5e53a01.json
