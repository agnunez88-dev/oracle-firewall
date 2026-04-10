# oracle-firewall
Log unauthorized access to the database

collect_data.py: This is the Python script used to collect data from various databases.

config.json: This is the JSON file containing the settings for connecting to one or more databases.

firewall.py: This is the Python script that generates a simple HTML report.

options.json: This is the JSON file containing configuration settings for generating the HTML report.

table-firewall.txt: this table is used to store the collected records

table-firewall_logon_log.txt: this table is where the trigger stores firewall violations

tnsnames.ora: string for connecting to the database

trigger.txt: the trigger that activates the alarms
