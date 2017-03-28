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
    counter = 0
    for i in range(number):
        data = bridge.getBridgeValue(index)
        if data < -400 and counter < 10:
            print "ERROR!!"
            return -1
        acc += [data]
        time.sleep(sample)
        counter += 1

    return acc

def outputData(descr, name, sample, number, index):
    data = getData(sample, number, index)
    if data == -1:
        return
    text_file = open(name, "w")

    string = ""
    for i in data:
        string += str(i) + '\n'

    header = "sample rate:  %fs\nsamples:      %i\nindex:        %i\n-------------------\n" % (sample, number, index)
    text_file.write(descr+'\n\n'+header + string)
    text_file.close()
