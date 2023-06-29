import paho.mqtt.client as mqtt
broker_address = "127.0.0.1"
broker_port = 1883
client = mqtt.Client()
def on_connect(client, userdata, flags, rc):
    print("Successfully connected to MQTT broker")
    # Subscribe to the desired topic
    client.subscribe("Mother")
def on_message(client, userdata, msg):
    print("Received message:")
    print("Subject: " + msg.topic)
    print("Message: " + msg.payload.decode())

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port)

client.loop_start()
run = True
while run:
    user_input = input("Enter 'stop' to exit: ")
    if user_input.lower() == "stop":
        run = False
client.loop_stop()
client.disconnect()
