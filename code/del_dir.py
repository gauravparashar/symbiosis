from snakebite.client import Client
client = Client('localhost',8020)
for p in client.delete(['/user/hadoop/test'], recurse=True):
    print(p)
