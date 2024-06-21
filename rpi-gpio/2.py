from gpiozero import PWMOutputDevice
from time import sleep, time
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
tones = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 740, 0]
music = [4, 9, 6, 4, 12, 12, 4, 6, 9, 6, 4, 2, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 12, 4, 4, 4, 4, 4, 4, 7, 7, 7, 5, 7, 6, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 8, 11, 9, 12, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 11, 9, 12, 2, 2, 4, 2, 2, 4, 4, 2, 4, 12, 2, 2, 4, 2, 2, 4, 4, 2, 4]
term = [1, 0.5, 0.5, 0.5, 1.5, 0.5, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125, 0.125, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.375, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25, 0.375, 0.125]

current_status = 0  # current_status 변수를 초기화

try:
    start_time = time()  # 시작 시간 기록
    for i in range(len(music)):
        pwm_device.frequency = tones[music[i]]
        pwm_device.value = 0.5  # 50% 듀티 사이클로 PWM 출력 설정
       
        # LED 색상 변경
        if current_status % 2 == 0:
            pixels.fill((255, 0, 0))  # 빨간색 설정
        else:
            pixels.fill((0, 0, 255))  # 파란색 설정
       
        pixels.show()  # NeoPixel 스트립 업데이트
       
        # 다음 음표 시작까지 대기
        sleep(term[i])
       
        # 다음 음표 시작 시간 계산
        next_note_time = start_time + sum(term[:i+1])
       
        # 현재 시간이 다음 음표 시작 시간까지 대기
        while time() < next_note_time:
            pass
       
        current_status += 1
   
    pwm_device.value = 0  # 모든 작업이 완료되면 PWM 출력을 0으로 설정하여 LED를 끕니다.
finally:
    pwm_device.close()  # 예외 발생 시 PWM 장치를 안전하게 닫습니다.
