import csv

def getYoutubeURLs(_threads):
    lastMessage = getLast()
    
    for thread in threads:
        th = thread
        messages = client.fetchThreadMessages(thread_id=thread.uid, limit=10)
        # Since the message come in reversed order, reverse them
        messages.reverse()
        print("Messages from "+thread.name+" : ")
        # Prints the content of all the messages
        for message in messages:
            strMessage = str(message.text)
            print("\t"+strMessage)
            if(strMessage.find("youtube") != -1):
                URLs.append(strMessage)
    return URLs

def getLast():
    last["uid"]=[]
    last["ts"]=[]
    last["executed"]=[]
    
    f = open('lastMessage.csv', 'r')
    with f:
        reader = csv.DictReader(f)
        for row in reader:
            last["uid"].append(row["uid"])
            last["ts"].append(row["ts"])
            last["executed"].append(row["executed"])
    return last
    
def getUserRankInLast(_uid,_last):
    userIndex = 0
    for user in _last["uid"]:
        if(user == _uid):
            return userIndex
        else:
            userIndex+=1
