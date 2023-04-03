# sample_for_study_kafka_python

// install kafka
wget https://downloads.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
tar -xzf kafka_2.13-3.4.0.tgz
mv kafka_2.13-3.4.0 kafka

// start kafka
// please use several terminals 
kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties
kafka/bin/kafka-server-start.sh kafka/config/server.properties


// make kafka topic for sample
kafka/bin/kafka-topics.sh --create --topic room-status --bootstrap-server localhost:9092
kafka/bin/kafka-topics.sh --create --topic checkout-record --bootstrap-server localhost:9092

// make python virtual environment, please using python 3.9 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

// start api.py
python3 api.py

// start edges
python3 sensor_edge.py
python3 checkout_edge.py


// start consumer
python3 consumer.py
