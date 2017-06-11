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


class Artanis:


    def append(self, variables, key, willappended, mode1, mode2= 'string'):   # 가칭

        if mode1 == 'direct':
            if mode2 == 'string':
                self.willappended = willappended
                variables[key].append(self.willappended)

            if mode2 == 'float':
                self.willappended = float(willappended)
                variables[key].append(self.willappended)

        if mode1 == 'varappend':
                self.willappended = variables[willappended]
                variables[key].append(self.willappended)


    def listsorts(self, variables, key, mode):      # 가칭
        if mode == 'sort':
            variables[key].sort()

        if mode == 'reverse':
            variables[key].reverse()


    def pop(self, variables, key, receive):             # 가칭
        variables[receive] = variables[key].pop()

    def count(self, variables, key, counted, receive, mode):       #가칭
        if mode == 'direct':
            self.counted = counted

        if mode == 'varcount':
            self.counted = variables[counted]

        variables[receive] = variables[key].count(counted)


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

    def totalrecall(self, variables, mode, line):      # while
        self.valuea = variables[self.name1]
        self.valueb = variables[self.name2]
        self.line = line

        if mode =='right':          # 전부 가칭
            if self.valuea > self.valueb:
                return 1
            else:
                return 0
        if mode == 'righteq':
            if self.valuea >= self.valueb:
                return 1
            else:
                return 0
        if mode == 'left':
            if self.valuea < self.valueb:
                return 1
            else:
                return 0
        if mode == 'lefteq':
            if self.valuea <= self.valueb:
                return 1
            else:
                return 0
        if mode == 'eq':
            if self.valuea == self.valueb:
                return 1
            else:
                return 0
        if mode == 'noteq':
            if self.valuea != self.valueb:
                return 1
            else:
                return 0


class Jaina:


    def frostbolt(self, variables, key, cvalue, mode):         # var calculate
        self.var = variables[key]
        self.cvalue = cvalue

        if mode == 'wintersreach':
            
            variables[key] = float(self.var) + float(cvalue)

        if mode == 'lingeringchill':
            variables[key] = float(self.var) - float(cvalue)

        if mode == 'deepchill':
            variables[key] = float(self.var) * float(cvalue)

        if mode == 'conjurerspursuit':
            variables[key] = float(self.var) / float(cvalue)

        if mode == 'frostbitten':
            variables[key] = float(self.var) % float(cvalue)


    def arcaneintellect(self, variables, akey, bkey, resultkey, mode):

        self.a = variables[akey]
        self.b = variables[bkey]
        variables[resultkey] = float(0)

        if mode == 'plus':                          # 전부 가칭
            self.result = self.a + self.b

        if mode == 'minus':
            self.result = self.a - self.b

        if mode == 'multiple':
            self.result = self.a * self.b

        if mode == 'divide':
            self.result = self.a / self.b

        if mode == 'remainder':
            self.result = self.a % self.b

        if mode == 'square':
            self.result = self.a ** self.b

        variables[resultkey] = self.result


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