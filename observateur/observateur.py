import requests

log = "latest.log"
URL = "http://172.105.0.226:5000"

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


def post_actions(actions):

    requests.post(URL, json=actions)


status_prec = {}

for i in range(0, 262, 10):
    status = read_log(i)
    if status_prec != status:
        actions = []
        for player in status:
            if player in status_prec:
                if status[player] != status_prec[player]:
                    if status[player]:
                        # print(player + " Joined")
                        actions.append({"name": player, "action": "join"})
                    else:
                        # print(player + " Left")
                        actions.append({"name": player, "action": "left"})
            else:
                actions.append({"name": player, "action": "join"})
        post_actions(actions)

    status_prec = status