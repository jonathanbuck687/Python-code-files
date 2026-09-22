from gpiozero import LED
from time import sleep

def binaryConverter(num):
    if (num == 0):
        return "0"
    if (num == 1):
        return "1"
    return (binaryConverter(num // 2) + str(num % 2))

def twosCompliment(num):
    twosCompliment.binary = binaryConverter(abs(num))
    twosCompliment.binary = twosCompliment.binary.zfill(8)
    i = 0
    while (i < len(twosCompliment.binary)):
        if twosCompliment.binary[i:i + 1] == "1":
            twosCompliment.binary2 += "0"
        else:
            twosCompliment.binary2 += "1"
        i += 1
    twosCompliment.binary = twosCompliment.binary2
    if (twosCompliment.binary[len(twosCompliment.binary) - 1:] == "0"):
        twosCompliment.binary = twosCompliment.binary[:len(twosCompliment.binary) - 1] + "1"
    else:
        j = len(twosCompliment.binary) - 2
        while j >= 0:
            if twosCompliment.binary[j : j + 1] == "0":
                twosCompliment.binary = twosCompliment.binary[:j] + "1"
                for i in range(j, len(twosCompliment.binary)):
                    twosCompliment.binary += "0"
            j -= 1
    return twosCompliment.binary

twosCompliment.binary = ""
twosCompliment.binary2 = ""
def main():
    lights = [LED(4), LED(17), LED(27), LED(22), LED(5), LED(6), LED(13), LED(19)]
    num = int(input("Enter an integer betwen -128 - 255 inclusive: ")) 
    if num >= 0:
        binar = binaryConverter(num)
        if (len(binar) < 8):
            while len(binar) < 8:
                binar = "0" + binar
    else:
        binar = twosCompliment(num)

    print(binar)
    i = 0
    if (num < 0):
        sign = LED(26)
        sign.on()
    while i < len(binar):
        if (binar[i:i + 1] == "1"):
            lights[i].on()
            sleep(1)
        i += 1

main()

