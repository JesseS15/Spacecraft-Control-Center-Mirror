# STaTE
# File: SimObject.py 
# Purpose: Define EPS subsytem for use in a SimObject thread

from simapp.models import Sim
from simulation.ACS import ACS
from simulation.TCS import TCS
from simulation.EPS import EPS
from simulation.COMMS import COMMS
from simulation.Payload import Payload
import threading
import time
import random

class SimObject(threading.Thread):

    ################### Initialize  SimObject Thread #######################
    def __init__(self, final_values, pk):
        threading.Thread.__init__(self)
        
        sim = Sim.objects.get(pk=pk)
        self.simName = sim.sim_name
        
        self.finalValues = {
            "roll": 0,
            "pitch": 0,
            "yaw": 0,
            "finalLongitude": 0
        }
        self.finalValues.update(final_values)
        self.finalValues["finalLongitude"] = 81 # Longitude of 81 is ERAU Daytona Beach campus

        self.subsystems = {"ACS": 0, "TCS": 0, "COMMS": 0, "EPS": 0, "Payload": 0}
        self.telemetry = {"ACS": False, "TCS": False, "EPS": False, "Payload": False}
        self.createSubsys()
        self.imageDisplayed = False
        self.stop_flag = threading.Event()

    ################### Create SimObject Thread's Subsystems #######################
    def createSubsys(self):
        self.subsystems["ACS"] = ACS(self.finalValues)
        self.subsystems["EPS"] = EPS()
        self.subsystems["COMMS"] = COMMS()
        self.subsystems["TCS"] = TCS()
        self.subsystems["Payload"] = Payload()
            
    ################### Manage running SimObject Thread #######################
    def run(self):
        # Run until sim is deleted
        while not self.stop_flag.is_set():
            if not self.imageDisplayed:
                self.update()
                time.sleep(1)

    def update(self):
        self.setSubsystemTelemetry()
        self.checkPayloadReady()
        self.subsystems["COMMS"].allTelemetryData = self.telemetry
        self.subsystems["ACS"].update()
        self.subsystems["EPS"].update()
        self.subsystems["TCS"].update()
        displayImage = self.subsystems["COMMS"].update()
        if (displayImage and (not self.imageDisplayed)):
            for subsys in self.subsystems:
                self.subsystems[subsys].consoleLog.append("")
                self.subsystems[subsys].consoleLog.append("ALL SUBSYSTEMS COMPLETED -- MISSION ACCOMPLISHED")
                self.subsystems[subsys].consoleLog.append("Link to image:")
                self.subsystems[subsys].consoleLog.append("http://tiny.cc/sot6vz")
                #self.subsystems[subsys].consoleLog.append("http://[ENTER_DOMAIN:PORT]/fo/imagedisplay/") 
            self.imageDisplayed = True
    
    def setSubsystemTelemetry(self):
        # Using flag telemetryTransferComplete rather than calling function (that is for user command)
        self.telemetry["ACS"] = self.subsystems["ACS"].telemetryTransferComplete
        self.telemetry["EPS"] = self.subsystems["EPS"].telemetryTransferComplete
        self.telemetry["TCS"] = self.subsystems["TCS"].telemetryTransferComplete
        self.telemetry["Payload"] = self.subsystems["Payload"].telemetryTransferComplete

    def checkPayloadReady(self):
        acs = self.telemetry["ACS"]
        eps = self.telemetry["EPS"]
        tcs = self.telemetry["TCS"]
        long = self.subsystems["ACS"].checkLongitude()
        if acs and eps and tcs and long:
            self.subsystems["Payload"].ready = True
            
    def check(self):
        print('Sim Thread for '+ self.simName+' is reachable')

    def stop(self):
        self.stop_flag.set()