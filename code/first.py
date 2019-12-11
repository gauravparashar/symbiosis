# To execute the code we need to install snakebite python package
# The aim of the code is to display all the contents of the root of HDFS
# The client function takes two parameters Hostname or IP address of the NameNode and port number
# 

from snakebite.client import Client

client=Client('localhost',8020)
for x in client.ls(['/']):
    print(x)

