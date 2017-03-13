from Phidgets.Devices.Bridge import *
import time

bridge = Bridge()

def initBridge():
    bridge.openPhidget()

    try: 
        print "waiting for attach..."
        bridge.waitForAttach(10000)
        bridge.setEnabled(0, True)
        print "bridge attached!"
    except PhidgetException:
        print "attach failed."
        bridge.closePhidget()

def closeBridge():
    bridge.closePhidget()

def getData(sample, number, index):
    acc = []
    for i in range(number):
        acc += [bridge.getBridgeValue(index)]
        time.sleep(sample)

    return acc

def outputData(name, sample, number, index):
    data = getData(sample, number, index)
    text_file = open(name, "w")

    string = ""
    for i in data:
        string += str(i) + '\n'

    header = "sample rate:  %fs\nsamples:      %i\nindex:        %i\n-------------------\n" % (sample, number, index)
    text_file.write(header + string)
    text_file.close()
