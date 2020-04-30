import csv, schedule, time
from easysnmp import Session

def poll(host, com, ver, mib):
    session = Session(hostname=host, community=com, version=ver)
    output = session.get(mib)
    print(output)

with open('inventory.csv') as invfile:
    invreader = csv.reader(invfile)
    for row in invreader:
        host = row[0]
        freq = int(row[1])
        com = row[2]
        ver = int(row[3])
        for mib in row[4:]:
            schedule.every(freq).seconds.do(poll, host, com, ver, mib)

while True:
    schedule.run_pending()
    time.sleep(1)