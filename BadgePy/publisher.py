import paho.mqtt.client as mqtt
import color_constants as color

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

global_channel = 'feeds'

def publish(color1=None, color2=None, effect=None, effect_speed=None, channel=None):
	global global_channel
	if channel:
		global_channel = channel
	if color1: 
		try:
			c = color.colors[color1].hex_format()
		except:
			c = color1
		client.publish(f'{global_channel}/color1', c)
	if color2:
		try:
			c = color.colors[color2].hex_format()
		except:
			c = color2
		client.publish(f'{global_channel}/color2', c)
	if effect:
		try:
			int(effect)
		except:
			effect = effects[effect]
		client.publish(f'{global_channel}/effect', effect)
	if effect_speed:
		client.publish(f'{global_channel}/effectspeed', effect_speed)