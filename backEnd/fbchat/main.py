from itertools import islice
from fbchat import Client
from fbchat.models import *
from os import system
from connect import *
from youtube import *
from getQuery import *

client = Client(getUser(), getPass())

# Fetches a list of all users you're currently chatting with, as `User` objects
users = client.fetchAllUsers()

print("users' IDs: {}".format([user.uid for user in users]))
print("users' names: {}".format([user.name for user in users]))


# Fetches a list of the 20 top threads you're currently chatting with
threads = client.fetchThreadList()
# Fetches the next 10 threads
threads += client.fetchThreadList(limit=10)

# print("Threads: {}".format(threads))
URLs = getYoutubeURLs(threads)


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
            strAnswer = "Thanks "+thread.first_name + \
                ", let's play "+getVideoTitle(strMessage)
            client.send(Message(text=strAnswer), thread_id=thread.uid,
                        thread_type=ThreadType.USER)
            system("chromium-browser "+strMessage+"?autoplay=1")


#
#
#

def killChromium():
    system("pkill -o chromium-browse")