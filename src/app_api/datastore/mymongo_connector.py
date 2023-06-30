from ..config.cfg import MONGO_SETTINGS
from pymongo.mongo_client import MongoClient

class MongoConnector():
    def __init__(self):
        self.password = MONGO_SETTINGS["password"]

    def get_client(self):
        uri = f"mongodb+srv://companeat8:{self.password}@cluster0.4rpo890.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri)
        return client

    def get_database(self, client, db_name):
        return client.get_database(db_name)

    def get_report(self, db, report_name):
        records = db.reports
        res = records.find({"report_name":report_name})
        report = []
        for i in res:
            report.append(i)
        return report

    def get_users(client, user_id=None):

        db = client.get_database('entities')
        records = db.users

        if user_id == None:
            all_rests = records.find()
        else:
            filter_query = {"user_id": user_id}
            all_rests = records.find(filter_query)

        users = []
        for i in all_rests:
            users.append(i)

        return users

    def get_restaurants(self, db, projection, query_params=None):
        records = db.rests
        if query_params == None:
            all_rests = records.find({},projection)
        else:
            filter_query = query_params
            all_rests = records.find(filter_query)

        rests = []
        for i in all_rests:
            rests.append(i)

        return rests