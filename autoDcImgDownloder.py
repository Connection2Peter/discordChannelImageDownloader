import os, sys, time, requests, aniso8601
from datetime import datetime



##### Args & Vars
usage  = "\nUsage   :\n python %s {DIROUTPUT} {TOKEN} {CHNNELID}" % sys.argv[0]
usage += "\nExample :\n python %s ImageDownload token channelId\n" % sys.argv[0]
if len(sys.argv) < 4:
    exit(usage)


dirOutput = sys.argv[1]
selfToken = sys.argv[2]
channelId = sys.argv[3]

if not os.path.isdir(dirOutput):
    exit("\nError :\n DIROUTPUT not Existed.\n")



##### Main Program
modeDurat = True
EntimeOut = 0
pathOfUrl = "https://discord.com/api/v9/channels/{}/messages".format(channelId)
psatMsgId = ""
numPerReq = "100"
ResHeader = {"authorization": selfToken}

launchTimeStamp = datetime.timestamp(datetime(2022, 7, 19, 12,  0,  0))
finishTimeStamp = datetime.timestamp(datetime(2022, 7, 31, 0,  0,  0))

while True:
    time.sleep(1)

    if EntimeOut > 100:
            break

    if psatMsgId == "":
        Parameter = {"limit" : numPerReq}
    else:
        Parameter = {"before" : psatMsgId, "limit" : numPerReq}

    Responses = requests.get(pathOfUrl, params=Parameter, headers=ResHeader).json()
    try:
        psatMsgId = Responses[-1]["id"]

        for resp in Responses:
            if modeDurat:
                parseTime = datetime.timestamp(aniso8601.parse_datetime(resp["timestamp"]))

                if launchTimeStamp < parseTime and parseTime < finishTimeStamp:
                    for attach in resp["attachments"]:
                        time.sleep(0.2)

                        img = requests.get(attach["url"])
                        opt = os.path.join(dirOutput, attach["filename"])

                        if os.path.exists(opt):
                            opt = os.path.join(dirOutput, str(time.time()) + attach["filename"])

                        with open(opt, "wb") as f:
                            f.write(img.content)
    
                        print(opt)
                else:
                    EntimeOut += 1
            else:
                parseTime = datetime.timestamp(aniso8601.parse_datetime(resp["timestamp"]))

                if launchTimeStamp < parseTime and parseTime < finishTimeStamp:
                    for attach in resp["attachments"]:
                        time.sleep(0.2)

                        img = requests.get(attach["url"])
                        opt = os.path.join(dirOutput, attach["filename"])

                        if os.path.exists(opt):
                            opt = os.path.join(dirOutput, str(time.time()) + attach["filename"])

                        with open(opt, "wb") as f:
                            f.write(img.content)
    
                        print(opt)
    except:
        break


print("### Done !!")


