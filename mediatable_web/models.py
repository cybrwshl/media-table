from django.db import models
from mediatable_web.util import *

class SimpleColor(models.Model):
    hex_color = models.CharField(max_length = 7)
    date_of_creation = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.hex_color

    def set_color_from_rgb(self, rgb):
        self.hex_color = rgb_to_hex(rgb)

    def set_default_color(self):
        self.hex_color = rgb_to_hex((0,0,0))