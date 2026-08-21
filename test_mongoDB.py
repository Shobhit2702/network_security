from pymongo import MongoClient
uri = "mongodb+srv://shobhit9532_db_user:Shobhit2702@cluster0.ibrius5.mongodb.net/?appName=Cluster0"
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)