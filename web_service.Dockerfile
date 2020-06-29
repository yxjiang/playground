FROM ubuntu:18.04

EXPOSE 5000

RUN apt-get update && apt-get install -y python3 python3-pip

# WORKDIR bazel-bin

RUN mkdir -p /web_service

COPY bazel-bin-cp/web_service ./web_service
COPY ./web_service/requirements.txt ./web_service

RUN pip3 install -r web_service/requirements.txt

CMD python3 web_service/web_service