############################################################
# Dockerfile to build the Feature Request App with Python / Flask
# Based on CentOS 7 (latest)
############################################################

# Set the base image to Ubuntu
FROM centos:7

# File Author / Maintainer
MAINTAINER Sam Mohamed

# Update the sources list
RUN yum -y update
RUN yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs gcc g++ make wget

# Install Python 2.7.8
RUN curl -o /root/Python-2.7.9.tar.xz https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
RUN tar -xf /root/Python-2.7.9.tar.xz -C /root
RUN cd /root/Python-2.7.9 && ./configure --prefix=/usr/local && make && make altinstall

# Copy the application folder inside the container
ADD . /opt/iws_project

# Download Setuptools and install pip and virtualenv
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | /usr/local/bin/python2.7
RUN /usr/local/bin/easy_install-2.7 pip
RUN /usr/local/bin/pip2.7 install virtualenv

# Create virtualenv and install requirements:
RUN /usr/local/bin/virtualenv /opt/iws_project/venv && source /opt/iws_project/venv/bin/activate && pip install -r /opt/iws_project/requirements.txt

# Expose ports
EXPOSE 8000

# Set the default directory where CMD will execute
WORKDIR /opt/iws_project
 
RUN source /opt/iws_project/venv/bin/activate && /opt/iws_project/manage.py syncdb --noinput

