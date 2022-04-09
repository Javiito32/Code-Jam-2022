class module():

    def __init__(self, fun, nextModule, id) -> None:
        pass
    return {
        "id": id,
        "fun": fun,
        "nextModule": nextModule,
        "previousModules": [],
        "activated": False
    }

class Solution:
    def main(self):
        cases = int("1")

        for case in range(1, cases+1):
            modulesAmount = int("4")
            modulesFun = "60 20 40 50".split(" ")
            modulesPointer = "0 1 1 2".split(" ")
            self.modules = []
            self.initiators = []
            self.voidModules = []
            self.initiatorOrder = []
            values = []
            pointed = []
            
            for i in range(modulesAmount):
                modulePointer = int(modulesPointer[i])-1
                pointed.append(modulePointer)
                fun = int(modulesFun[i])
                values.append(fun)
                _module = module(fun, modulePointer, i)
                self.modules.append(_module)
                if modulePointer == -1:
                    self.voidModules.append(_module)

            for i in range(len(self.modules)):
                if self.modules[i]["nextModule"] != -1:
                    self.modules[self.modules[i]["nextModule"]]["previousModules"].append(self.modules[i])
                if i not in pointed:
                    self.initiators.append(i)

            _modules = self.copyModules(self.modules)
            
            #for i in range(len(self.voidModules)):
            #    self.goToTop(i)

            print(self.getLowestModule(self.voidModules[0]["previousModules"]))

            validResult = 0

            for value in self.initiatorOrder:
                validResult += self.getMaxFunOfChain(_modules, value)
            
            print("Case #" + str(case) + ": " + str(validResult))

    def getMaxFunOfChain(self, modules, position):
        if modules[position]['nextModule'] == -1 or modules[modules[position]['nextModule']]['activated']:
            modules[position]['activated'] = True
            return modules[position]['fun']
        else:
            modules[position]['activated'] = True
            return max(self.getMaxFunOfChain(modules, modules[position]['nextModule']), modules[position]['fun'])

    def goToTop(self, index):
        if index in self.initiators:
            self.initiatorOrder.append(index)
        lowestModuleResult = self.getLowestModule(self.modules[index]["previousModules"])
        if lowestModuleResult == -1:
            nextModuleId = self.modules[index]["nextModule"]
            newModule = self.getLowestModule(self.modules[nextModuleId]["previousModules"])
            if newModule == -1:
                return
            self.goToTop(newModule["id"])
        else:
            self.goToTop(lowestModuleResult["id"])
        
    def getLowestModule(self, moduleList, excludeList=[]):
        lowestModuleIndexes = []
        for k in range(len(moduleList)):
            print(lowestModuleIndexes)
            if (len(lowestModuleIndexes) == 0 or moduleList[k]["fun"] < moduleList[lowestModuleIndexes[0]]["fun"]) and moduleList[k] not in excludeList and not moduleList[k]["activated"]:
                lowestModuleIndexes.append(k)
            elif moduleList[k]["fun"] == moduleList[lowestModuleIndexes[0]]["fun"] and moduleList[k] not in excludeList and not moduleList[k]["activated"]:
                lowestModuleIndexes.append(k)

        if len(lowestModuleIndexes) == 0:
            return -1
        elif len(lowestModuleIndexes) == 1:
            return lowestModuleIndexes[0]
        else:
            modules = []
            for index in lowestModuleIndexes:
                modules.append(self.getLowestModule(self.modules[index]["previousModules"]))
            return modules

    def getModulePoints(self, module):
        if module["activated"]:
            return 0
        return module["fun"]

    def copyModules(self, modules):
        _modules = []
        for i in range(len(modules)):
            _modules.append(modules[i].copy())
        return _modules


Solution().main()
