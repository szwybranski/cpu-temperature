# Based on https://www.raspberrypi.org/learning/temperature-log/
from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()
plt.ion()
x = []
y = []

def write_log(data):
    with open("cpu_temp.csv", "a") as log:
        log.write(data)

def format_with_date(temp):
    return "{0}; {1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp))

def add_and_trim_old(array, new_element):
    array.append(new_element)
    if len(array) > 100:
        del array[0]

def graph(temp):
    add_and_trim_old(y, temp)
    add_and_trim_old(x, time())

    plt.clf()
    plt.ylabel("temperature")
    plt.xlabel(format_with_date(temp))
    plt.plot(x, y, 'ro')
    plt.draw()

while True:
    temp = cpu.temperature
    date_and_temp = format_with_date(temp)
    print(date_and_temp)
    #write_log(date_and_temp)
    graph(temp)
    sleep(10)
