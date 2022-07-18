import os, sys, time, requests, aniso8601
from datetime import datetime



#NjEzNzE4NDc2NTQ0Mjc4NTI5.GE-WIi.BJP2CBqkW9Ud10YU08MRnv-iguojIRWK6ZjYwI 917394528074354718
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
pathOfUrl = "https://discord.com/api/v9/channels/{}/messages".format(channelId)
psatMsgId = ""
numPerReq = "5"
ResHeader = {"authorization": selfToken}

while True:
    time.sleep(5)

    if psatMsgId == "":
        Parameter = {"limit" : numPerReq}
    else:
        Parameter = {"after" : psatMsgId, "limit" : numPerReq}

    Responses = requests.get(pathOfUrl, params=Parameter, headers=ResHeader).json()
    if len(Responses) == 0:
        time.sleep(5)
    else:
        psatMsgId = Responses[0]["id"]

        for resp in Responses:
            for attach in resp["attachments"]:
                opt = os.path.join(dirOutput, attach["filename"])
                if os.path.exists(opt):
                    continue

                time.sleep(0.2)
    
                with open(opt, "wb") as f:
                    f.write(requests.get(attach["url"]).content)

                print(opt)


print("### Done !!")


