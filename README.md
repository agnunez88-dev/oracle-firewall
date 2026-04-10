# oracle-firewall
Log unauthorized access to the database

collect_data.py: is the python script to collect data from different databases

config.json: is the json where you can find the parameters to connect different databases or just one

firewall.py: is the pythin script that creates a simple html report 

options.json: is the json file where resides a few configurations to create the html report

table-firewall.txt: this table is to store the collected records

table-firewall_logon_log.txt: this table is where the trigger store the firewall violations

tnsnames.ora: string to connect to the database

trigger.txt: the trigger that fire the alarms
