log = "latest.log"

def read_log(n, log=log):

    status = {}

    with open(log, "r") as f:
        lines = f.readlines()

    for line in lines[:n]:
        if "joined" in line:
            # print(line.split()[3])
            status[line.split()[3]] = True

        if "left" in line:
            # print(line.split()[3])
            status[line.split()[3]] = False

    return status

status_prec = {}

for i in range(262):
    status = read_log(i)
    if status_prec != status:
        for player in status:
            if player in status_prec:
                if status[player] != status_prec[player]:
                    if status[player]:
                        print(player + " Joined")
                    else:
                        print(player + " Left")
            else:
                print(player + " Joined")

        print()

    status_prec = status