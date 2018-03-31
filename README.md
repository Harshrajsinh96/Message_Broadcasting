# Message_Broadcasting

Built Client-Server chatting application using ZeroMQ messaging library in python to plan a distributed concurrent chatting application. The concurrency of message delivery was achieved because of the absence of message broker. The aim was to make BROADCAST messaging service, so PUB-SUB technique was applied to achieve parallel pipelining.