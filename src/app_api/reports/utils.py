import json
from typing import Dict
from ..datastore.mymongo_connector import MongoConnector

def get_api_report(query_params: Dict, report_name=None):
    mongo_connector = MongoConnector()
    client = mongo_connector.get_client()
    db = mongo_connector.get_database(client, "api")
    res_report = mongo_connector.get_report(db, report_name)[0]
    db = mongo_connector.get_database(client, res_report["db"])
    projection = {'_id': False}

    if len(query_params) == 0:
        res = getattr(mongo_connector, report_name)(db, projection)
    else:
        res = getattr(mongo_connector, report_name)(db, query_params, projection)

    # get_report(db, report_name, query_params)
    client.close()

    return res

