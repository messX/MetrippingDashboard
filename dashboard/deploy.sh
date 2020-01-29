sudo apt-get update
sudo apt-get install curl -y
sudo apt-get install python-dev -y
sudo apt-get install python3-dev -y
sudo apt-get install libpq-dev -y
# Install base dependencies
sudo apt-get update && apt-get install -y -q --no-install-recommends \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        libssl-dev \
        supervisor \
        vim \
        wget \
    && rm -rf /var/lib/apt/lists/*

#Python setup
sudo apt-get update
sudo  apt-get install software-properties-common -y
sudo  apt-add-repository universe -y
sudo  apt-get update -y
sudo  apt-get install python-pip -y
sudo  pip install uwsgi
sudo  pip install virtualenv
sudo virtualenv -p /usr/bin/python3 /home/ubuntu/ver3.4
sudo  chown -R ubuntu /home/ubuntu/ver3.4
sudo /home/ubuntu/ver3.4/bin/pip install autoenv

