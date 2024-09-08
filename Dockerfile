FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip curl wget 
COPY /dist/monisys-0.3-py3-none-any.whl /root/
WORKDIR /root
RUN wget https://pkg.osquery.io/deb/osquery_5.12.1-1.linux_amd64.deb
RUN dpkg -i osquery_5.12.1-1.linux_amd64.deb
RUN pip install monisys-0.3-py3-none-any.whl --break-system-packages
RUN rm -rf *

