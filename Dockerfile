FROM ubuntu:14.04
ENV DEBIAN_FRONTEND=noninteractive

#Update server
RUN apt-get update

#Install vim for debugging
RUN apt-get install -y vim

#Install python and dependencies
RUN python3 --version
RUN apt-get install -y python3-pyqt5
RUN apt-get install -y python3-pip
RUN pip3 install pika

#Copy app source
RUN mkdir /var/client-app
COPY *.py /var/client-app/

CMD python3 /var/client-app/main.py
#CMD tail -f /dev/null