def module( fun, nextModule):
    return {
        "fun": fun,
        "nextModule": nextModule,
        "activated": False
    }

def main():
    cases = int(input())

    for case in range(1, cases+1):
        modulesAmount = int(input())
        modulesFun = input().split(" ")
        modulesPointer = input().split(" ")
        _modules = []
        values = []
        initiatorModules = []
        
        for i in range(modulesAmount):
            modulePointer = int(modulesPointer[i])-1
            fun = int(modulesFun[i])
            values.append(fun)
            _modules.append(module(fun, modulePointer))

        for i in range(modulesAmount):
            isActivator = True
            for j in range(modulesAmount):
                if _modules[j]['nextModule'] == i:
                    isActivator = False
            
            if isActivator:
                initiatorModules.append(i)

        maxValidResult = maxTheorical(values, len(initiatorModules))
        validResult = 0

        for i in range(len(initiatorModules)):
            _initiatorModules = initiatorModules.copy()
            _initiatorModules.pop(i)
            calculatedFun = getMaxFun(copyModules(_modules), _initiatorModules, initiatorModules[i])
            if calculatedFun > validResult:
                validResult = calculatedFun
                if calculatedFun == maxValidResult:
                    break
        
        print("Case #" + str(case) + ": " + str(validResult))

def getMaxFun(modules, initiators, position):
    if modules[position]['nextModule'] == -1 or modules[modules[position]['nextModule']]['activated']:
        if len(initiators) == 0:
            modules[position]['activated'] = True
            return modules[position]['fun']
        else:
            modules[position]['activated'] = True
            values = []
            for i in range(len(initiators)):
                _initiators = initiators.copy()
                _initiators.pop(i)
                values.append(getMaxFun(copyModules(modules), _initiators, initiators[i]))
            return max(values) + modules[position]['fun']
    else:
        modules[position]['activated'] = True
        return max(getMaxFun(modules, initiators, modules[position]['nextModule']), modules[position]['fun'])
    
def copyModules(modules):
    _modules = []
    for i in range(len(modules)):
        _modules.append(modules[i].copy())
    return _modules

def maxTheorical(modules, initiatorsAmount):
    maxValue = 0
    for i in range(initiatorsAmount):
        maxValue += modules.pop(modules.index(max(modules)))
    return maxValue

main()
