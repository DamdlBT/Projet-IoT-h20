log = "latest.log"

status = {}

with open(log, "r") as f:
    lines = f.readlines()

for line in lines[:100]:
    if "joined" in line:
        # print(line.split()[3])
        status[line.split()[3]] = True

    if "left" in line:
        # print(line.split()[3])
        status[line.split()[3]] = False

    if "joined" in line or "left" in line:
        print(status)
    