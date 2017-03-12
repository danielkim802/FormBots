from Phidgets.Devices.Bridge import *
import time

bridge = Bridge()

def initBridge():
    bridge.openPhidget()

    try: 
        print "waiting for attach..."
        bridge.waitForAttach(10000)
        print "bridge attached!"
    except PhidgetException:
        print "attach failed."
        bridge.closePhidget()

    bridge.setEnabled(0, True)

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

    header = "sample rate:  %f\nsamples:      %i\nindex:        %i\n-------------------\n" % (sample, number, index)
    text_file.write(header + string)
    text_file.close()
