import os

cpu = {
  "cpuManager": False,
  "cpuPowerSaver": "None",
  "cpufullPerf": "None",
}

gpu = {
  "gpuManager": False,
  "gpuPowerSaver": None,
  "gpufullPerf": None,
}

msiAfterBurnerFlag=True

def main():
    if configFileExists() == False:
        print("No cfg file detected, Starting one time setup")
        cpu["cpuManager"]=True
        cpu["cpuPowerSaver"]=initCpuPowerSaverPlan()
        cpu["cpufullPerf"]=initCpuFullPerfPlan()
        if msiAfterBurnerFlag:
            cpu["gpuManager"]=True
            cpu["gpuPowerSaver"]=initGpuPowerSaverPlan()
            cpu["gpufullPerf"]=initGpuFullPerfPlan()
        generateConfigFile()
    readSavedConfigFile()


    

def readSavedConfigFile():
    f = open('./settings.cfg', "r")
    for line in f.readlines():
        print(line.split("="))
    f.close()

def generateConfigFile():
    f = open('./settings.cfg', "w")
    for key in cpu.keys():
        f.write("%s=%s\n"%(key,cpu[key]))    
    f.close()
    return 0

def configFileExists():
    if os.path.isfile('./settings.cfg'):
        return True
    return False

def initCpuPowerSaverPlan():
    return 0

def initCpuFullPerfPlan():
    return 0

def initGpuPowerSaverPlan():
    return 0

def initGpuFullPerfPlan():
    return 0


main()