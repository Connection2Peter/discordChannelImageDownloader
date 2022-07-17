import os, sys, time, requests



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
numPerReq = "100"
ResHeader = {"authorization": selfToken}

while True:
    time.sleep(1)

    if psatMsgId == "":
        Parameter = {"limit" : numPerReq}
    else:
        Parameter = {"before" : psatMsgId, "limit" : numPerReq}

    Responses = requests.get(pathOfUrl, params=Parameter, headers=ResHeader).json()
    try:
        psatMsgId = Responses[-1]["id"]

        for resp in Responses:
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


