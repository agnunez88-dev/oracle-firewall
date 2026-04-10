import oracledb
import json
import urllib3

from datetime import date, timedelta

with open('/home/rundeck/PycharmProjects/oraclefirewall/options.json','r') as file:
    load_option = json.load(file)

fileout = open("/var/www/html/diatipo/firewall.html", "w")


fileout.write('<html>')
fileout.write('<head>')
fileout.write('<title> Firewall </title>')
fileout.write('</head>')
fileout.write('<body>')
fileout.write('<h1> Firewall Oracle Database </h1>')

current_date = date.today().strftime('%d-%m-%Y')

fileout.write('<h2> Fecha: ' + str(current_date) + '</h2>')

header = False

connDiatipo = oracledb.connect(user='diatipo', password='1qazxsw2', dsn='127.0.0.1/freepdb1')

cursorDiatipo = connDiatipo.cursor()

try:

    # Details for database status
    if load_option['option'] == 'firewall':
        header = False
        fileout.write('<h2>Firewall violations</h2>')
        table = "<table border=1 style=margin-bottom:30px>\n"
        cursorDiatipo.execute(
            'select db as database, user_session, ip_address, module, trunc(id_fecha) as fecha, count(id) from '
            'firewall where trunc(id_fecha) = trunc(sysdate) group by database,user_session, ip_address, '
            'module,trunc(id_fecha) order by COUNT (id) desc')

        # Create the table's column headers
        if not header:
            table += "  <tr>\n"
            for column in cursorDiatipo.description:
                table += "    <th>" + column[0] + "</th>\n"
            table += "  </tr>\n"

            header = True

        # Create the table's row data
        for fila in cursorDiatipo:
            table += "  <tr>\n"
            for column in fila:
                table += "    <td>" + str(column) + "</td>\n"
            table += "  </tr>\n"
        table += "</table>"
        fileout.writelines(table)

except Exception as error:
    print(error)

fileout.write('</body>')
fileout.write('</html>')

fileout.close()

connDiatipo.close()

