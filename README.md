# sample_for_study_kafka_python

1. install kafka

wget https://downloads.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz

tar -xzf kafka_2.13-3.4.0.tgz

mv kafka_2.13-3.4.0 kafka

2. start kafka,please use several terminals 

kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties

kafka/bin/kafka-server-start.sh kafka/config/server.properties


3. make kafka topic for sample

kafka/bin/kafka-topics.sh --create --topic room-status --bootstrap-server localhost:9092

kafka/bin/kafka-topics.sh --create --topic checkout-record --bootstrap-server localhost:9092

4. make python virtual environment, please using python 3.9 

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt


5. start server

python3 api.py

6. start edges

python3 sensor_edge.py

python3 checkout_edge.py


7. start consumer

python3 consumer.py
