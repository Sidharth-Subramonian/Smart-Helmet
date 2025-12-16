from mpu6050 import mpu6050
import math
import time

sensor = mpu6050(0x68)

def is_crash():
    accel = sensor.get_accel_data()
    x, y, z = accel['x'], accel['y'], accel['z']
    magnitude = math.sqrt(x**2 + y**2 + z**2)

    print(f"[Crash Check] x:{x:.2f} y:{y:.2f} z:{z:.2f} | Accel Mag: {magnitude:.2f}")

    # Y-axis dead zones (lying on back or stomach)
    y_dead = (-10.15 <= y <= -9.75) or (9.25 <= y <= 10.00)

    # X-axis dead zones (lying sideways)
    x_dead = (x <= -7.2) or (x >= 7.2)

    return y_dead or x_dead

def is_movement():
    accel = sensor.get_accel_data()
    x, y = accel['x'], accel['y']

    # Movement = not inside any dead zone
    y_moving = not (-10.15 <= y <= -9.75 or 9.25 <= y <= 10.00)
    x_moving = not (x <= -7.2 or x >= 7.2)

    return y_moving and x_moving

def detect_crash_with_timer():
    if is_crash():
        print("[Status] Potential crash detected! Waiting 10 seconds for rider response...")
        for i in range(10):
            time.sleep(1)
            if is_movement():
                print("[Status] Movement detected! Rider is responsive. Resuming normal operation.")
                return False
            print(f"[Timer] {10 - i}s remaining...")
        print("[ALERT] Crash confirmed! No response from rider.")
        return True
    return False
