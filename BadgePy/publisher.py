import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.155.0.214", 1883, 60)

effects = { 
	'off': 			0,
	'on': 			1,
	'blink':		2,
	'pulse':		3,
	'alternate1':	4,
	'alternate2':	5,
	'rainbow':		6
}

def publish(color1=None, color2=None, effect=None, effect_speed=None):
	if color1: 
		client.publish('feeds/color1', color1)
	if color2:
		client.publish('feeds/color2', color2)
	if effect:
		try:
			int(effect)
		except:
			effect = effects[effect]
		client.publish('feeds/effect', effect)
	if effect_speed:
		client.publish('feeds/effectspeed', effect_speed)