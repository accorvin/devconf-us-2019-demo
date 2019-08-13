FROM registry.access.redhat.com/ubi8/ubi
LABEL maintainer "Alex Corvin <acorvin@redhat.com>"

RUN dnf -y install vim python3-pip \
    && dnf clean all
RUN mkdir /flask-app
WORKDIR /flask-app
COPY requirements.txt /flask-app
RUN pip-3 install --no-cache-dir -r requirements.txt
COPY . /flask-app

EXPOSE 5000

CMD ["bash", "/flask-app/run.sh"]
