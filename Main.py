import paho.mqtt.client as mqtt
import time

#MQTT Basics: https://www.hivemq.com/mqtt-essentials/
#Python MQTT Example: http://www.steves-internet-guide.com/into-mqtt-python-client/

broker_address = "broker.hivemq.com"
broker_port = 1883
topic = "vic_4rotor/ignition"

def handleOnConnect(client, userdata, flags, rc):
    print("*" * 20)
    print(f'Connected With Result Code {rc}')
    print("\n")

def handleOnMessage(client, userdata, message):
    print("*" * 20)
    print(f'Message received: {str(message.payload.decode("utf-8"))}')
    print(f'Message topic: {message.topic}')
    print(f'Message qos: {message.qos}')
    print(f'Message retain flag: {message.qos}')
    print("\n")

print(f'Broker Address is: {broker_address}')
print(f'Topic is: {topic}')

client = mqtt.Client("myClient")
client.on_connect = handleOnConnect
client.on_message = handleOnMessage
print("Initialized client")

print("Connecting to broker...")
client.connect(broker_address, broker_port)
client.loop_start()
client.subscribe(topic)

print(f'Publishing messages to the following topic: {topic}')
client.publish(topic, "Position_1")
client.publish(topic, "Position_2")
client.publish(topic, "Position_3")
client.publish(topic, "Position_4")
client.publish(topic, "Position_2")
client.publish(topic, "Position_3")
client.publish(topic, "Position_1")

time.sleep(4) #Wait for messages
client.loop_stop()

print("That's all folks!")