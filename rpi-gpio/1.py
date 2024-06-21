from gpiozero import PWMOutputDevice
from time import sleep
import board
import neopixel

# GPIO 핀 설정 및 LED 개수 설정
pixel_pin = board.D10
num_pixels = 4

# NeoPixel 객체 생성
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

# PWM 설정
pwm_device = PWMOutputDevice(pin=12, frequency=100, initial_value=0.5)

# 음악 및 깜빡임 패턴 설정
tones = [523,587,659,698,784,880,988,1047,1175,1319,1397,1480,0]
music = [4, 9, 6, 4, 12, 12, 4, 6, 9, 6, 4, 2, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 12, 4, 4, 4, 4, 4, 4, 7, 7, 7, 5, 7, 6, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 8, 11, 9, 12, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 11, 9, 12, 2, 2, 4, 2, 2, 4, 4, 2, 4, 12, 2, 2, 4, 2, 2, 4, 4, 2, 4]
term = [1, 0.5, 0.5, 0.5, 1.5, 0.5, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.375, 0.125]

current_status = 0  # current_status 변수를 초기화

try:
    for i in range(len(music)):
        pwm_device.frequency = tones[music[i]]
        pwm_device.value = 0.5  # 50% duty cycle
       
        if current_status % 3 == 0:
            pixels.fill((255, 0, 0))  # 모든 픽셀을 빨간색으로 설정
        elif current_status % 3 == 1:
            pixels.fill((0, 0, 255))  # 모든 픽셀을 파란색으로 설정
        else:
            pixels.fill((255, 255, 255))  # 모든 픽셀을 흰색으로 설정
       
        pixels.show()  # LED 스트립 업데이트
        sleep(term[i])
       
        current_status += 1
   
    pwm_device.value = 0
finally:
    pwm_device.close()