class Tassadar:  # Tassadar manage data
    def __init__(self, name):
        self.name = name

    def psiinfusion(self, variables, objects, mode = ''):  # declare variables
        self.variables = variables
        self.objects = objects

        if mode == 'focusedbeam':
            self.objects = float(self.objects)
        if mode == 'psionicecho':
            self.objects = objects.split("storm")
            for i in range(len(self.objects)):
                self.objects[i] = float(self.objects[i])
        if mode == 'psionicechoW':
            self.objects = objects.split("storm")

        self.variables[self.name] = self.objects

    def templarswill(self, variables, listkey, mode):  # sum,len,max,min list
        self.listkey = listkey
        self.vlist = variables.get('{0}'.format(self.listkey))
        self.mode = mode

        if self.mode == 'khalascelerity':
            return sum(self.vlist)
        if self.mode == 'khalasembrace':
            return len(self.vlist)
        if self.mode == 'khalashighlight':
            return max(self.vlist)
        if self.mode == 'khalaslowlight':
            return min(self.vlist)

class Tracer:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def spatialecho(self, variables, mode, line, lineplus = 4):     # if
        self.valuea = variables[self.name1]
        self.valueb = variables[self.name2]
        self.lineplus = int(lineplus)

        if mode == 'getstuffed!':
            if self.valuea > self.valueb:
                return 1
            else:
                line += self.lineplus
                return 0
        if mode == 'getstuffed':
            if self.valuea >= self.valueb:
                return 1
            else:
                line += self.lineplus
                return 0
        if mode == '!deffutsteg':
            if self.valuea < self.valueb:
                return 1
            else:
                line += self.lineplus
                return 0
        if mode == 'deffutsteg':
            if self.valuea <= self.valueb:
                return 1
            else:
                line += self.lineplus
                return 0
        if mode == 'lockedandloaded':
            if self.valuea == self.valueb:
                return 1
            else:
                line += self.lineplus
                return 0
        if mode == 'loadedandlocked':
            if self.valuea != self.valueb:
                return 1
            else:
                line += self.lineplus
                return 0

    def totalrecall(self, variables, mode, line, linelimit,lineminus = 4):      # while
        self.valuea = variables[self.name1]
        self.valueb = variables[self.name2]
        self.line = line
        self.linetogo = linelimit - lineminus

        if mode =='':
            while self.valuea > self.valueb:
                self.line = self.linetogo
                pass
        if mode == '':
            while self.valuea >= self.valueb:
                self.line = self.linetogo
                pass
        if mode == '':
            while self.valuea < self.valueb:
                self.line = self.linetogo
                pass
        if mode == '':
            while self.valuea <= self.valueb:
                pass
        if mode == '':
            while self.valuea == self.valueb:
                pass
        if mode == '':
            while self.valuea != self.valueb:
                pass

class Jaina:
    def frostbolt(self, variables, key, cvalue, mode):         # var calculate
        self.key = key
        self.var = variables(key)
        self.cvalue = cvalue
        self.mode = mode

        if self.mode == 'wintersreach':
            variables[key] = self.var + cvalue
        if self.mode == 'lingeringchill':
            variables[key] = self.var - cvalue
        if self.mode == 'deepchill':
            variables[key] = float(self.var) * float(cvalue)
        if self.mode == 'conjurerspursuit':
            variables[key] = float(self.var) / float(cvalue)

class Ragnaros:
    def livingmeteor(self, variables, mode = 'lavasurge', willprinted = ''):
        self.willprinted = willprinted
        if mode == 'lavasurge':               # direct input - print
            print(self.willprinted)
        if mode == 'flamesofsulfuron':               # key mode
            print(variables[self.willprinted])


    def handofragnaros(self, mode = 'catchingfire', printstring = ''):
        self.printstring = printstring
        self.result = 0
        if mode == 'engulfingflame':
            self.result = float(input(self.printstring))
            return self.result
        if mode == 'catchingfire':
            self.result = str(input(self.printstring))
            print(self.result)
            return self.result