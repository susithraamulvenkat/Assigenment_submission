import paho.mqtt.client as mqtt
broker_address = "127.0.0.1"  # MQTT broker information
broker_port = 1883
client = mqtt.Client()  # This line creates an instance of the MQTT client using the mqtt.Client() constructor.
client.connect(broker_address, broker_port)  # Connect to the MQTT broker
topic = "Mother"  # Get message from user
info = input("Enter The Information Which You Want To Publish: ")
client.publish(topic, info)  # Publish the message
client.disconnect()  # Disconnect from the MQTT broker
