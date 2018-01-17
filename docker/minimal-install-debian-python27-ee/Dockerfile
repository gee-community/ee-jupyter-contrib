FROM debian:stable

LABEL maintainer="tylere@google.com"

RUN apt-get update && apt-get install -y \
    python-pip

RUN pip install google-api-python-client
RUN pip install google-auth-oauthlib
RUN pip install earthengine-api

ENTRYPOINT ["/bin/bash"]
