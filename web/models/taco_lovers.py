from lib import mongo
from pymongo.errors import DuplicateKeyError

class TacoLover:
    def __init__(self, phone_number):
       self.phone_number = phone_number

    @staticmethod
    def find_by_phone_number(phone_number):
        collection = mongo.get_db().taco_lovers

        try:
            taco_lover =  collection.find_one({
                'phone_number' : phone_number
            })

            return TacoLover(taco_lover['phone_number'])
        except:
            raise TacoLoverNotFoundExcpetion()

    def save(self):
        collection = mongo.get_db().taco_lovers

        try:
            collection.ensure_index('phone_number', unique=True)
            collection.insert({
                'phone_number' : self.phone_number
            })
        except DuplicateKeyError:
            raise TacoLoverAlreadyExistsExpection()

    def delete(self):
        collection = mongo.get_db().taco_lovers

        collection.remove({
            'phone_number' : self.phone_number
        })



class TacoLoverNotFoundExcpetion(Exception):
    pass


class TacoLoverAlreadyExistsExpection(Exception):
    pass

