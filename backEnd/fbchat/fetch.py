# -*- coding: UTF-8 -*-

from itertools import islice
from fbchat import Client
from fbchat.models import *
from connect import *

client = Client(getUser(), getPass())

# Fetches a list of all users you're currently chatting with, as `User` objects
users = client.fetchAllUsers()

print("users' IDs: {}".format([user.uid for user in users]))
print("users' names: {}".format([user.name for user in users]))


# Fetches a list of the 20 top threads you're currently chatting with
threads = client.fetchThreadList()
# Fetches the next 10 threads
threads += client.fetchThreadList(limit=10)

print("Threads: {}".format(threads))


# Gets the last 10 messages sent to the thread
messages = client.fetchThreadMessages(thread_id="100004155888313", limit=10)
# Since the message come in reversed order, reverse them
messages.reverse()

# Prints the content of all the messages
for message in messages:
    print(message.text)


# If we have a thread id, we can use `fetchThreadInfo` to fetch a `Thread` object
thread = client.fetchThreadInfo("100004155888313")["100004155888313"]
print("thread's name: {}".format(thread.name))
print("thread's type: {}".format(thread.type))


# `searchForThreads` searches works like `searchForUsers`, but gives us a list of threads instead
thread = client.searchForThreads("<name of thread>")[0]
print("thread's name: {}".format(thread.name))
print("thread's type: {}".format(thread.type))
