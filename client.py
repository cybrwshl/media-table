# -*- encoding: utf-8 -*-

import threading
import json

import zmq

import pygame
from myscreen import MyScreen


if not pygame.font:
	print 'Warning, fonts disabled'

if not pygame.mixer:
	print 'Warning, sound disabled'

FRAMES = 30
COLORCHANGE = pygame.USEREVENT + 1


def collect_messages():
	context = zmq.Context()
	sock = context.socket(zmq.PULL)
	sock.bind("tcp://127.0.0.1:5555")
	while True:
		message = sock.recv_json()
		pygame.event.post(pygame.event.Event(COLORCHANGE, message=message))
		print(message)


def json_to_rgb(data):
	s = json.loads(data)

	r = int(s["r"])
	g = int(s["g"])
	b = int(s["b"])

	assert 0 <= r <= 255, "value for 'r' must be between 0 and 255"
	assert 0 <= g <= 255, "value for 'g' must be between 0 and 255"
	assert 0 <= b <= 255, "value for 'b' must be between 0 and 255"

	return r, g, b


def main():
	pygame.init()
	screen = pygame.display.set_mode((1024, 768), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)

	myscreen = MyScreen(screen, (0, 0, 0))

	pygame.display.set_caption("")
	pygame.mouse.set_visible(0)
	pygame.key.set_repeat(1, 30)

	clock = pygame.time.Clock()

	t = threading.Thread(target=collect_messages, args=())
	t.setDaemon(1)
	t.start()

	screen.fill((0, 0, 0))
	running = True

	while running:
		clock.tick(FRAMES)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))

			if event.type == COLORCHANGE:
				r, g, b = json_to_rgb(event.message)
				myscreen.__fade_color__((r, g, b), FRAMES * 5)

		myscreen.__tick__()
		pygame.display.flip()


if __name__ == '__main__':
	main()