from kafka import KafkaConsumer
import json
import time
import datetime
import asyncio
# To consume latest messages and auto-commit offsets

room_status_consumer = KafkaConsumer('room-status',
                         bootstrap_servers=['localhost:9092'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))

checkout_consumer =KafkaConsumer('checkout-record',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
def create_data():
    data={
        "room101":{"temp":0,"count":0,"max":0,"min":0},
        "room102":{"temp":0,"count":0,"max":0,"min":0}}
    return data



async def status_process():
    present_time=time.time()
    data=create_data()

    while True:
        if time.time()-present_time>10:
            print(data)
            data= create_data()
            present_time=time.time()
        msg_pack = room_status_consumer.poll(timeout_ms=1000)

        for tp,messages in msg_pack.items():
            # print(messages)
            for message in messages:
                print(message.value)
                msg_data=data[message.value['name']]
                msg_data['temp']=message.value['temp']
                msg_data['count']+=1
                msg_data['min']=min(message.value['temp'],msg_data['min'])
                msg_data['max']=max(message.value['temp'],msg_data['max'])
        await asyncio.sleep(1)


async def checkout_alarm():
    while True:
        start_time=datetime.datetime.now()
        #checkout_alarm="You should check alarm!"
        await asyncio.sleep(10)
        end_time=datetime.datetime.now()
        print("start....")

        messages=[]
        max_message=5
        for message in checkout_consumer:
                if message.timestamp >= start_time.timestamp() * 1000 and message.timestamp <= end_time.timestamp() * 1000:
                    messages.append(message)
                    print(message)
                if len(messages)>= 0:
                    break

        print(messages)
        print("end..")
        

async def main():
    checkout_alarm_task=asyncio.create_task(checkout_alarm())

    status_process_task= asyncio.create_task(status_process())
    await asyncio.gather(checkout_alarm_task,status_process_task)


  
asyncio.run(main())
