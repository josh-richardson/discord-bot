import discord
import datetime

index = {}

messageFrequencyTimelength = 5
messagesPerTimelength = 5
messageSimilarityTimelength = 20
similarMessagesPerTimeLength = 5
username = "your-username"
password = "your-password"

client = discord.Client()
client.login(username, password)


@client.event
def on_message(message):
    userID = message.author.id
    now = datetime.datetime.now()

    if userID in index:
        potentialSpam = 0
        messagesToCompare = []
        for messageData in index[userID]:
            elapsedTime = int(divmod((now - messageData[1]).total_seconds(), 60)[1])
            if elapsedTime < messageFrequencyTimelength:
                potentialSpam += 1
            if elapsedTime < messageSimilarityTimelength:
                messagesToCompare.append(messageData[0])

        if potentialSpam >= messagesPerTimelength:
            client.delete_message(message)
            print "Deleted message: flooding."
        else:
            similarMessages = 0
            content = message.content
            for msg in messagesToCompare:
                if content == msg:
                    similarMessages += 1
                elif len(content) >= 10 and len(msg) >= 10:
                    if content[:10] == msg[:10] or content[10:] == msg[10:]:
                        similarMessages += 1
            if similarMessages >= similarMessagesPerTimeLength:
                client.delete_message(message)
                print "Deleted message: similarity."

    if userID not in index:
        index[userID] = [[message.content, now]]
    else:
        index[userID].append([message.content, now])
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run()

