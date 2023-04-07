import requests

MOTOR_DRIVER_IP_ADDR = "http://192.168.1.160"

import math

def getDuty(x):
    return 1.0/(x*2.727272727272733e+4+math.sqrt((x*2.727272727272733e+4-2.431332087713275e+8)**2+2.057590971198525e+14)-2.431332087713275e+8)**(1.0/3.0)*(-5.903637488052969e+4)+(x*2.727272727272733e+4+math.sqrt((x*2.727272727272733e+4-2.431332087713275e+8)**2+2.057590971198525e+14)-2.431332087713275e+8)**(1.0/3.0)+7.220779220779237e+2

# Example usage
x = 100
result = getDuty(x)
print(result)


if __name__ == "__main__":
    while True:
        try:
            i = int(input("1- Motor 1 Speed\n2- Motor 2 Speed\n--> "))
            if i == 1:
                spd1 = float(input('Motor 1 RPM:\n--> '))
                duty1 = int(getDuty(spd1))
                print(f"Duty set to {duty1}/1000")
                requests.get(MOTOR_DRIVER_IP_ADDR + f"/s/s1/?{duty1}?")
            elif i == 2:
                spd2 = float(input('Motor 2 RPM:\n--> '))
                duty2 = int(getDuty(spd2))
                print(f"Duty set to {duty2}/1000")
                requests.get(MOTOR_DRIVER_IP_ADDR + f"/s/s2/?{duty2}?")

            else :
                print("invalid choice")


        except KeyboardInterrupt:
            break