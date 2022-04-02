class Permutator():
    def __init__(self, modules, maxValidResult, nums):
        self.modules = modules
        self.maxValidResult = maxValidResult
        self.result = 0
        self.permute_util(nums,0,[])

    def permute_util(self,given_list,start,curr):
        if start > len(given_list)-1:
            self.searchMaxValue(curr)
            return
        for i in range(start,len(given_list)):
            if self.result != self.maxValidResult:
                self.swap(given_list,start,start+(i-start)) 
                self.permute_util(given_list,start+1,curr+[given_list[start]])
                self.swap(given_list, start, start + (i - start))
            else:
                break

    def swap(self,nums,index1,index2):
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp

    def searchMaxValue(self, order):
        acum = 0
        _modules = copyModules(self.modules)
        for i in order:
            acum += getMaxFunOfChain(_modules, i)
        if acum > self.result:
            self.result = acum
    
    def getResult(self):
        return self.result

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
        modules = []
        values = []
        initiatorModules = []
        
        for i in range(modulesAmount):
            modulePointer = int(modulesPointer[i])-1
            fun = int(modulesFun[i])
            values.append(fun)
            modules.append(module(fun, modulePointer))

        for i in range(modulesAmount):
            isActivator = True
            for j in range(modulesAmount):
                if modules[j]['nextModule'] == i:
                    isActivator = False
            
            if isActivator:
                initiatorModules.append(i)

        maxValidResult = maxTheorical(values, len(initiatorModules))

        permutator = Permutator(modules, maxValidResult, initiatorModules)

        validResult = permutator.getResult()
        

        #for i in range(len(initiatorModules)):
        #    _initiatorModules = initiatorModules.copy()
        #    _initiatorModules.pop(i)
        #    calculatedFun = getMaxFunOfChain(copyModules(_modules), initiatorModules[i])
        #    if calculatedFun > validResult:
        #        validResult = calculatedFun
        #        if calculatedFun == maxValidResult:
        #            break
        
        print("Case #" + str(case) + ": " + str(validResult))

def getMaxFunOfChain(modules, position):
    if modules[position]['nextModule'] == -1 or modules[modules[position]['nextModule']]['activated']:
        modules[position]['activated'] = True
        return modules[position]['fun']
    else:
        modules[position]['activated'] = True
        return max(getMaxFunOfChain(modules, modules[position]['nextModule']), modules[position]['fun'])
    
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
