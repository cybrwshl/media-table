class MyScreen(object):
	def __init__(self, screen, color):
		self.animation_frame = -1
		self.frames = 0
		self.screen = screen
		self.current_color = color
		self.current_exact_color = color
		self.next_color = color
		self.screen.fill(color)

	def __set_color__(self, color):
		self.screen.fill(color)
		self.animation_frame = -1

	def __fade_color__(self, color, frames):
		self.animation_frame = 0
		self.next_color = color
		self.frames = frames

	def __tick__(self):
		# if there's no animation running there's nothing to do
		if self.animation_frame == -1:
			return

		self.animation_frame += 1
		if self.animation_frame >= self.frames:
			self.current_color = self.next_color
			self.animation_frame = -1
			self.screen.fill(self.current_color)
			return
		self.fade_color_rgb_calc()

	def fade_color_alpha_calc(self):
		# first set to current color
		self.screen.fill(self.current_color)

		# make a copy and fill it with the next color
		copy = self.screen.copy()
		copy.fill(self.next_color)

		# calculate alpha
		alpha = int((255.0 / self.frames) * self.animation_frame)
		copy.set_alpha(alpha)

		# 'merge' both images
		self.screen.blit(copy, (0, 0))

	def fade_color_rgb_calc(self):
		self.current_color = self.get_exact_color_rgb()
		self.screen.fill(self.current_color)

	def get_exact_color_rgb(self):
		r1, g1, b1 = self.current_color
		r2, g2, b2 = self.next_color

		r3 = r1 + (float(r2 - r1) / (self.frames - self.animation_frame))
		g3 = g1 + (float(g2 - g1) / (self.frames - self.animation_frame))
		b3 = b1 + (float(b2 - b1) / (self.frames - self.animation_frame))

		return r3, g3, b3