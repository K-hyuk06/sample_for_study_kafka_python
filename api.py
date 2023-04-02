from flask import Flask
from flask_restful import Resource, Api,reqparse
from kafka import KafkaProducer
import json
from api_parser import *
app = Flask(__name__)
api = Api(app)



producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))

class Status(Resource):
    def get(self):
        return {"test":"test"}
    def post(self):
        args=status_parser().parse_args()
        name=args['name']
        temp=args['temp']

        try:
            producer.send('room-status',value={'name':name,'temp':temp}).get()
            print("sended")
            return {"name":name,"success":True}
        except Exception as E:
            print(E)
            return {"name":name,"success":False}


#if get return list of status record
class Record(Resource):
    def get(self):
        pass


# if get return list of alarm
class Warning(Resource):
    def get(self):
        pass

#if post return kafka producer.send
class CheckOut(Resource):
    def post(self):
        args=checkout_parser().parse_args()
        name=args['name']
        checkout=args['checkout']
        try:
            producer.send('checkout-record',value={'name':name,"checkout":checkout})
        except:
            pass
            
           
       

        


api.add_resource(CheckOut, '/api/checkout')
api.add_resource(Status, '/api/status')

api.add_resource(Warning, '/api/warning')
api.add_resource(Record, '/api/record')

if __name__ == '__main__':
    app.run(debug=True)