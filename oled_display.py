from machine import Pin, SoftI2C
import ssd1306
import framebuf
import images_repo
import utime


class Display:

    def __init__(self):
        # using default address 0x3C
        self.i2c = SoftI2C(sda=Pin(22), scl=Pin(23))
        self.display = ssd1306.SSD1306_I2C(128, 64, self.i2c)

    def run(self, images_list):
        for image in images_list:
            buffer = image

            fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)
            self.display.fill(0)
            self.display.blit(fb, 8, 0)

            self.display.show()
            utime.sleep_ms(100)

    def run_intro(self):
        self.run(images_repo.intro_images_list)

    def run_uv_low(self):
        self.run(images_repo.uv_baixo_images_list)
