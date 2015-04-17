import json

import zmq


def send_color_json((r, g, b)):
	context = zmq.Context()
	sock = context.socket(zmq.PUSH)
	sock.connect("tcp://127.0.0.1:5555")

	message = json.dumps({'r': r, 'g': g, 'b': b})
	sock.send_json(message)

	sock.disconnect("tcp://127.0.0.1:5555")
	context.destroy()