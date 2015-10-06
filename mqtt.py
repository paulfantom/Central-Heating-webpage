SENSORS_DATA = {}

def on_connect(client, userdata, flags, rc):
    client.subscribe('room/1/#')
    client.subscribe('outside/#')
    client.subscribe('solarControl/#')

def on_message(client, userdata, message):
    try:
        SENSORS_DATA[message.topic] = float(message.payload)
        print(message.topic+" : "+str(SENSORS_DATA[message.topic]))
    except ValueError:
        try:
            #TODO check if JSON
            SENSORS_DATA[message.topic] = str(message.payload)
        except Exception:
            SENSORS_DATA[message.topic] = str(message.payload)
    except AttributeError:
        pass 
