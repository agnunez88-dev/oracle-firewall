import oracledb
import json

connDiatipo = oracledb.connect(user='diatipo', password='1qazxsw2', dsn='127.0.0.1/freepdb1')

cursorDiatipo = connDiatipo.cursor()

with open('/home/rundeck/PycharmProjects/oraclefirewall/config.json','r') as file:
    connection = json.load(file)

with open('/home/rundeck/PycharmProjects/oraclefirewall/options.json','r') as file1:
    load_option = json.load(file1)

for con in connection:
    for database in connection[con]:
        db = database['database']
        username = database['user']
        passw = database['password']
        servicename = database['service_name']

        try:         

            connection = oracledb.connect(user=username, password=passw, dsn=db,config_dir='/home/rundeck/PycharmProjects/pythonProject')

            cursor = connection.cursor()
            
			# Collect data from database status
			if load_option['option'] == 'firewall':
				try:

					cursor.execute(
						'select * from firewall_logon_log where id_fecha>trunc(sysdate-1)')

					row = cursor.fetchall()
					print(db)
					for i in row:
						data = dict(db=db,
									p_session_user=i[0],
									p_ip_address=i[1],
									p_module=i[2],
									p_id_fecha=i[3])

						try:
							sql = f"""INSERT INTO firewall(db , USER_SESSION, IP_ADDRESS, MODULE, ID_FECHA) VALUES 
								(:db , :p_session_user, :p_ip_address, :p_module,:p_id_fecha)"""

							cursorDiatipo.execute(sql, data)

						except Exception as error:
							print("Oracle: No se puede insertar en la tabla firewall: " + str(error))
					connDiatipo.commit()

				except Exception as error:
					print("Oracle database: "+ db + " No se puede seleccionar en la tabla firewall_logon_log: " + str(error))

        except Exception as error:
            print('No se puede conectar a: ' + db + ':' + str(error))

cursor.close()
connection.close()

# free resources
cursorDiatipo.close()
connDiatipo.close()

