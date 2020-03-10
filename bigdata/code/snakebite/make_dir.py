# To design a program which creates a directory in user directory
# Execute the code as a  hadoop user
# sudo su hadoop
# python make_dir.py


from snakebite.client import Client

client = Client('localhost',8020)
for p in client.mkdir(['/user/hadoop/test']):
    print(p)
