# flask-app
A website made with Flask

<h1>Running the app</h1>
python app.py
Then open 127.0.0.1:5000

<h1>Setting up the dev environment</h1><br>
Using OSX
brew install pyenv
pyenv install 3.6.4
pyenv global 3.6.4

sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install awscli
pip3 install flask

<h2>Setting up the database</h2>
brew install mysql
sudo chown -R _mysql:mysql /usr/local/var/mysql
sudo mysql.server start
mysql -uroot
In SQL:
CREATE DATABASE BucketList;
CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));


