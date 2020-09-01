#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from random import randint
from time import sleep

ts = TouchSensor(INPUT_1)

m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
m3 = LargeMotor(OUTPUT_C)

print("ready!")

ts.wait_for_bump() # wait for user to calibrate motors

m1.reset()
m2.reset()
m3.reset()

while True:
    ts.wait_for_bump()
    m1.on(speed=randint(-100, 100))
    m2.on(speed=randint(-100, 100))
    m3.on(speed=randint(-100, 100))
    ts.wait_for_bump()
    m1.off(brake=False)
    ts.wait_for_bump()
    m2.off(brake=False)
    ts.wait_for_bump()
    m3.off(brake=False)
    ts.wait_for_bump()
    pos1 = round(m1.position / 45) * 45
    pos2 = round(m2.position / 45) * 45
    pos3 = round(m3.position / 45) * 45
    m1.on_to_position(100, pos1)
    m2.on_to_position(100, pos2)
    m3.on_to_position(100, pos3)
