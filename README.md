# Fast-Port-Scanner

This is my fast port scanner which scans ports from 0-6555 in 1second.

It stores open port of each ip scanned from a list from a database. (more info in usage how to set up your database) and then with a discord webhook with bot it sends your open ports to a linked discord channel.

It is made to scan every ten minutes.

### Usage

It works with a database connected to the port scanner. In the database there should be a database with a table inside it that has variables ip and ports.

You can setup your mysql database with runing setup_db.py first then setup_table.py.


In the menu you can choose the option 2 where you can insert a domain in you table which is going to be scanned. It can be ip or a host domain.

It is using a webhook to send the open ports status to you desired discord channel.

### Requirements
Install python pyfiglet libary. Manually or using `pip install pyfiglet`

Install python mysql libary. Manyally from mysql website or using `pip install mysql-connector-python`

