from time import sleep
import board
import neopixel
from gpiozero import PWMOutputDevice
from threading import Thread

# NeoPixel 설정
pixel_pin = board.D10
num_pixels = 4
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

# PWMOutputDevice 설정
pwm_device = PWMOutputDevice(pin=12, frequency=100, initial_value=0)

# NeoPixel을 제어하는 함수
def control_led():
    try:
        while True:
            # NeoPixel LED 제어 코드
            pixels.fill((255, 0, 0))  # 빨간색으로 켜기
            pixels.show()
            sleep(0.5)

            pixels.fill((255, 255, 255))  # 흰색으로 켜기
            pixels.show()
            sleep(0.5)

            pixels[0] = (255, 0, 0)    # 첫 번째 LED: 빨간색
            pixels[1] = (0, 255, 0)    # 두 번째 LED: 초록색
            pixels[2] = (0, 0, 255)    # 세 번째 LED: 파란색
            pixels[3] = (255, 255, 255) # 네 번째 LED: 흰색
            pixels.show()
            sleep(0.5)

            blink_leds(0.2, 0.2, 5)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(1.25)

            blink_leds(0.125, 0.125, 4)

            blink_leds(0.25, 0.25, 1)

            blink_leds(0.125, 0.125, 4)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.125)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            blink_leds(0.125, 0.125, 4)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            blink_leds(0.125, 0.125, 4)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            blink_leds(0.125, 0.125, 7)

            blink_leds(0.0625, 0.0625, 2)

            blink_leds(0.125, 0.125, 4)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.25)

            blink_leds(0.125, 0.125, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.125)

            blink_leds(0.0625, 0.0625, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.125)

            blink_leds(0.0625, 0.0625, 2)

            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.125)

            blink_leds(0.0625, 0.0625, 2)

            blink_leds(0.125, 0.125, 2)


            # LED 꺼지기 (0.375초 꺼짐)
            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.375)

            # LED 켜기 (0.125초 켜짐)
            pixels.fill((255, 0, 0))
            pixels.show()
            sleep(0.125)

            # LED 꺼지기 (다음 단계에서 꺼짐)
            pixels[0] = (0, 0, 0)    # 첫 번째 LED: 빨간색
            pixels[1] = (0, 0, 0)    # 두 번째 LED: 초록색
            pixels[2] = (0, 0, 0)    # 세 번째 LED: 파란색
            pixels[3] = (0, 0, 0) # 네 번째 LED: 흰색
            pixels.show()

    except KeyboardInterrupt:
        pixels.fill((0, 0, 0))  # 프로그램 종료 시 모든 LED 끄기
        pixels.show()

# LED를 깜빡이는 함수
def blink_leds(on_time, off_time, repeat_count):
    for _ in range(repeat_count):
        pixels.fill((255, 0, 0))  # LED 켜기
        pixels.show()
        sleep(on_time)

        pixels.fill((0, 0, 0))  # LED 끄기
        pixels.show()
        sleep(off_time)

# PWMOutputDevice를 사용하여 음악을 연주하는 함수
def play_music():
    tones = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 740, 0]
    music = [4, 9, 6, 4, 12, 12, 4, 6, 9, 6, 4, 2, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 12, 4, 4, 4, 4, 4, 4, 7, 7, 7, 5, 7, 6, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 8, 11, 9, 12, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 11, 9, 12, 2, 2, 4, 2, 2, 4, 4, 2, 4, 12, 2, 2, 4, 2, 2, 4, 4, 2, 4]
    term = [1, 0.5, 0.5, 0.5, 1.5, 0.5, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.375, 0.125]

    try:
        for i in range(len(music)):
            pwm_device.frequency = tones[music[i]]
            pwm_device.value = 0.5  # 50% duty cycle
            sleep(term[i])
            pwm_device.value = 0
    finally:
        pwm_device.close()

# 두 기능을 병렬로 실행하기 위한 스레드 생성
thread_led = Thread(target=control_led)
thread_music = Thread(target=play_music)

# 스레드 시작
thread_led.start()
thread_music.start()

# 메인 스레드가 스레드의 종료를 기다림
thread_led.join()
thread_music.join()

print("Program terminated.")
