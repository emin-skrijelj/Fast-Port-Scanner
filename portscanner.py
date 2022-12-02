import socket
import sys
import subprocess
from datetime import datetime
import time
import pyfiglet
import mysql.connector
import asyncio
import requests 


#connecting to mysql database

mydb = mysql.connector.connect(
  host="localhost", #change this
  user="root", #change this
  password="password", #change this
  database="domain" #change this
)

mycursor = mydb.cursor()




async def portScan(port : int) -> None: 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((serverIP,port))
            s.close()
        
        print(f'{port} found open!')
        prts.append(str(port))

    except Exception:
        pass


async def event_loop() -> None:
    '''
        Main event loop
    '''
    tasks = []
    for portNumber in range(0,65555):
        tasks.append(asyncio.create_task(portScan(portNumber)))
    await asyncio.gather(*tasks)




ascii_banner = pyfiglet.figlet_format("L3G4CY")
print(ascii_banner)

print("Choose your option:")
print("-"*36)
print("| 1. Port scanning domains database|")
print("-"*36)
print("| 2. Add domain to database        |")
print("-"*36)



option = input("--- Option:")

subprocess.call('clear', shell=True) #clears everything in you shell/screen




if option == '1':
    mycursor.execute("SELECT ip FROM domains")
    myres = mycursor.fetchall()

    while True:
        for dom in myres:
            prts = []
            serverIP = dom[0]
            t1 = datetime.now()

            try:
                asyncio.run(event_loop())
                val = ','.join(prts)
                sqi = "UPDATE domains SET ports = '{}' where ip = '{}'".format(val,dom[0])
                mycursor.execute(sqi)
                mydb.commit()
                url = "<your webhook url>" 
                data = {
                    "content" : f'```Scanned ip - {dom[0]} --- \n Open Ports: {val} \n Completed at {datetime.now()}```',
                    "username" : "Port Scanner"
                    }
                rez = requests.post(url, json = data)

                try:
                    rez.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)



            except KeyboardInterrupt:
                print("You exited the program... bye!")
                sys.exit()

            except socket.gaierror:
                print("Hostname not resolved.")
                sys.exit()
            except socket.error:
                print("Could not connect to server")
                sys.exit()

            t2 = datetime.now()

            total_time = t2 - t1
            

            print(f'Scanning completed in {total_time}')
            print(f'Scaning completed at {datetime.now()}')
        time.sleep(600)

elif option == '2':
    print(1)
    dom = input("Enter your domain hostname: ")
    dip = socket.gethostbyname(dom)
    sqi = "INSERT INTO domains(ip) VALUES (%s)"
    val = (dip,)
    mycursor.execute(sqi,val)
    mydb.commit()

