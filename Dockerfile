1 FROM ubuntu
  2 RUN apt-get update
  3 RUN apt-get install -y python3
  4 RUN apt-get install -y python3-pip
  5 RUN mkdir /var/tmp/src
  6 RUN chmod 777 /var/tmp/src
  7 COPY src/modulos /var/tmp/src/modulos
  8 RUN pip3 install -r /var/tmp/src/modulos
  9 RUN rm -rf /var/tmp/src
 10 COPY src/main.py /var/tmp/main.py
 11 COPY src/testSheets-3547a5e53a01.json /var/tmp/testSheets-3547a5e53a01.json
 12 RUN python3 main.py
 13 RUN rm -rf /var/tmp/main.py /var/tmp/testSheets-3547a5e53a01.json