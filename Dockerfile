FROM centos:7

ENV PYTHON_VERSION "3.6.0"



RUN yum -y install epel-release \
&& yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
&& yum -y install python36u python36-setuptools \
&& easy_install-3.6 pip

RUN echo $'[mongodb-org-3.4] \n\
name=MongoDB Repository \n\
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/ \n\
gpgcheck=1 \n\
enabled=1 \n\
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc' >> etc/yum.repos.d/mongodb-org.repo

RUN yum repolist
RUN yum -y install mongodb-org
RUN yum clean all

WORKDIR /pottery

COPY . .

RUN pip install -r requirements.txt
RUN pip install -e .

EXPOSE 5000

RUN mkdir -p /data/db


CMD ["python3.6", "/pottery/pottery/__init__.py"]







