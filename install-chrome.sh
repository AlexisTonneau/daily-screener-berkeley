apt-get -y update
apt-get -y install wget apt-utils gnupg

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt-get -y update
apt-get install -y google-chrome-stable
apt-get install -yqq unzip
wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
