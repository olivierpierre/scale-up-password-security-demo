FROM ubuntu:24.04

RUN apt-get update && apt-get install -y hashcat

COPY demo/02-rockyou/rockyou_md5.txt /root/rockyou_md5.txt
COPY README.md /root/README.md

WORKDIR /root
CMD ["bash"]