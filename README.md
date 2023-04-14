# kv_store_cloud
This Implementats a TCP server, that stores and retrieves data for different clients using get and set command. It also handles more than one request at a time. 

# Understanding Problems
First problem is when requesting set and get command, input should in specific format so that server can parse it as per the request.
  o Intermediate Problem-
    ▪ set command should be two lines request, while get command will be one line.
Second problem is that server will be assigned one port, in case of multiple requests, all requests will be coming from same port, if the request will be processed on that port, processing will be slow, and we need to make this processing concurrent.
