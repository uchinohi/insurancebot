from pymongo import MongoClient


class Query:
    
    client = MongoClient('mongodb+srv://admin:1234@cluster0.5cqzv.mongodb.net/insurancebot?retryWrites=true&w=majority')
    db = client['insurancebot']
    mobcol = db['mobile']

    @staticmethod
    def search_mobile(number):
        doc = Query.mobcol.find_one({'number': number})
        if doc['number'] == number:
            return True
        else:
            return False

    @staticmethod
    def return_name(number):
        doc = Query.mobcol.find_one({'number': number})
        return doc['name']


    @staticmethod
    def return_claims(number):
        doc = Query.mobcol.find_one({'number': number})
        return doc['claims']

    @staticmethod
    def return_claim_status(number, claimno):
        doc = Query.mobcol.find_one({'number': number})
        return doc['claims'].get(claimno)

