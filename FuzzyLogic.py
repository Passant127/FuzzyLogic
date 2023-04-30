from dataclasses import dataclass


@dataclass
class fuzzysets(object):
    setname: str
    shape: str
    a: int
    b: int
    c: int
    d: int
    centroid: float
    membership: float

    def init(self, setname, shape, a, b, c, d, membership):
        self.name = setname
        self.shape = shape
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.membership = membership


def getCentroid(self):
    return self.centroid


def setCentroid(self, centroid):
    self.centroid = centroid


@dataclass
class varaible:
    name: str
    type: str
    lowebound: float
    upperbound: float
    fuzzysets: list

    def init(self, name, type, lowerbound, upperbound, fuzzysets):
        self.name = name
        self.lowebound = lowerbound
        self.upperbound = upperbound
        self.type = type
        self.fuzzysets = fuzzysets


def getmembership(self, crispv):
    listofmembership = []
    if self.shape == "TRI":
        if (crispv == self.a):
            self.membership = 0
        elif (crispv == self.b):
            self.membership = 1
        elif (crispv == self.c):
            self.membership = 0
        elif (crispv > self.a and crispv < self.b):
            x1 = self.a
            y1 = 0
            x2 = self.b
            y2 = 1
            s = (y2 - y1) / (x2 - x1)
            z = y2 - (s * x2)
            self.membership = s * crispv + z
        elif (crispv > self.b and crispv < self.c):
            x1 = self.b
            y1 = 1
            x2 = self.c
            y2 = 0
            s = (y2 - y1) / (x2 - x1)
            z = y2 - (s * x2)
            self.membership = s * crispv + z
        else:
            self.membership = 0
    if self.shape == "TRAP":
        if (crispv == self.a):
            self.membership = 0
        elif (crispv == self.b):
            self.membership = 1
        elif (crispv == self.c):
            self.membership = 1
        elif (crispv == self.d):
            self.membership = 0
        elif (crispv < self.b and crispv > self.a):
            x1 = self.a
            y1 = 0
            x2 = self.b
            y2 = 1
            s = (y2 - y1) / (x2 - x1)
            z = y2 - (s * x2)
            self.membership = s * crispv + z
        elif (crispv > self.c and crispv < self.d):
            x1 = self.c
            y1 = 1
            x2 = self.d
            y2 = 0
            s = (y2 - y1) / (x2 - x1)
            z = y2 - (s * x2)
            self.membership = s * crispv + z
        else:
            self.membership = 0
    return self.membership


def fuzzification(self, crisp):
    membershipofset = getmembership(self, crisp)
    s = self.setname
    x = {s: membershipofset}
    return x


# infrence of 2 arguments
def inference(s, c1, c2, self):
    result = -1
    l = []
    x = s.split()
    name = x[0]
    for v in vars:
        if v.name == x[0]:
            # print(v.name)
            for sett in v.fuzzysets:
                if sett.setname == x[1]:
                    # print(set.name)
                    n1 = getmembership(sett, c1)
                    sett.membership = n1
                    # print(sett.membership)
    for v in vars:
        if v.name == x[3]:
            # print(v.name)
            for sett in v.fuzzysets:
                if sett.setname == x[4]:
                    # print(set.name)
                    n2 = getmembership(sett, c2)
                    sett.membership = n2
                    # print("ooo",sett.membership)

    if "and" == x[2]:
        result = min(n1, n2)
    elif "or" == x[2]:
        result = max(n1, n2)
    elif "or_not" == x[2]:
        n2 = 1 - n2
        result = max(n1, n2)
    elif "and_not" == x[2]:
        n2 = 1 - n2
        result = min(n1, n2)
    for v in vars:
        if v.name == x[6]:
            # print(v.fuzzysets)
            for sett in v.fuzzysets:
                if sett.setname == x[7]:
                    if sett.membership < result:
                        sett.membership = result
    return result


def Calculatecentroid(self):
    for s in self.fuzzysets:
        if (s.shape == "TRI"):
            a = s.a
            b = s.b
            c = s.c
            centroid = (a + b + c) / 3
            setCentroid(s, centroid)
            # print("w:",centroid)
        else:
            a = s.a
            b = s.b
            c = s.c
            d = s.d
            centroid = (a + b + c + d) / 4
            setCentroid(s, centroid)
            # print("AS",getCentroid(self))

#Staticcc Partttttt
# Sets of Variable As static
# objec = fuzzysets(setname="beginner", shape="TRI", a=0, b=15, c=30, d=0, membership=0, centroid=0)
# objec1 = fuzzysets(setname="intermediate", shape="TRI", a=15, b=30, c=45, d=0, membership=0, centroid=0)
# objec2 = fuzzysets(setname="expert", shape="TRI", a=30, b=60, c=60, d=0, membership=0, centroid=0)
# obj1 = [objec, objec1, objec2]
# var2 = varaible(name="exp_level", type="IN", lowebound=0, upperbound=60, fuzzysets=obj1)
#
# # Sets of Variable
# object = fuzzysets(setname="very_low", shape="TRAP", a=0, b=0, c=10, d=30, membership=0, centroid=0)
# object1 = fuzzysets(setname="low", shape="TRAP", a=10, b=30, c=40, d=60, membership=0, centroid=0)
# object2 = fuzzysets(setname="medium", shape="TRAP", a=40, b=60, c=70, d=90, membership=0, centroid=0)
# object3 = fuzzysets(setname="high", shape="TRAP", a=70, b=90, c=100, d=100, membership=0, centroid=0)
# obj = [object, object1, object2, object3]
# var1 = varaible(name="proj_funding", type="IN", lowebound=0, upperbound=100, fuzzysets=obj)
#
# # Sets of Variable
# object = fuzzysets(setname="low", shape="TRI", a=0, b=25, c=50, d=0, membership=0, centroid=0)
# object1 = fuzzysets(setname="normal", shape="TRI", a=25, b=50, c=75, d=0, membership=0, centroid=0)
# object2 = fuzzysets(setname="high", shape="TRI", a=75, b=100, c=100, d=0, membership=0, centroid=0)
# obj2 = [object, object1, object2]
# var3 = varaible(name="risk", type="OUT", lowebound=0, upperbound=100, fuzzysets=obj2)
#
# # Variables List
# vars = [var1, var2, var3]
#
# # Rules
# rule = ["proj_funding high or exp_level expert => risk low",
#         "proj_funding medium and exp_level intermediate => risk normal",
#         "proj_funding medium and exp_level beginner => risk normal",
#         "proj_funding low and exp_level beginner => risk high",
#         "proj_funding very_low and_not exp_level expert => risk high "]


def defuz(vars):
    out = []
    for v in vars:
        Calculatecentroid(v)
    for v in vars:
        if v.type == "OUT":
            print(v.name)
            out.append(v)
    maxx = []
    maxdegree = 0
    for o in out:
        for s in o.fuzzysets:
            # print(s.membership)
            if maxdegree < s.membership:
                # print(s.setname)
                # print(s.membership)
                maxdegree = s.membership
                maxset = s
            # for sett in v.fuzzysets:
        output1 = Zout(o)
        file = open("C:/Users/Pc/Downloads/Assignment 3/output.txt", 'w')
        file.write("Ptredicted output "+v.name +" is "+ maxset.setname + ":"+ str(round(output1,1)) +"\n")
        file.close()


def Zout(v):
    sum = 0
    sum2 = 0
    for i in v.fuzzysets:
        sum += i.membership * getCentroid(i)
        sum2 += i.membership
    mean = sum / sum2
    return mean


# Main
print("Fuzzy Logic Toolbox")
print("===================")
print("1- Create a new fuzzy system")
print("2-Quit")
choice = int(input())
memerlist = []
if (choice == 1):
    print("Enter the system’s name and a brief description:")
    print("==================================================")
    project_name = input()
    print("Main Menu")
    print("===================")
    print("1-Read File")
    print("2-Exit")
    c = int(input())
    if (c == 1):
        fn = "C:/Users/Pc/Downloads/Assignment 3/Input.txt"
        with open(fn) as f:
            r = f.read().splitlines()
        index = 0
        n = int(r[0])
        index = n + 1
        v = []
        for i in range(n):
            obj = r[i + 1].split(" ")
            name = obj[0]
            type = obj[1]
            lowerbound = int(obj[2])
            upperbound = int(obj[3])
            v.append(varaible(name, type, lowerbound, upperbound, fuzzysets=0))
        print(v)
        index = n + 1
        nofv = int(r[index])
        #print("hhh", nofv)
        for e in range(nofv):
            index += 1
            vname = r[index]
            # print("Name", vname)
            index = index + 1
            nset = int(r[index])
            # print("nset", nset)
            fuzzy = []
            for j in range(nset):
                obj2 = r[index + 1].split()
                index += 1
                if (obj2[1] == "TRI"):
                    f = fuzzysets(obj2[0], shape=obj2[1], a=int(obj2[2]), b=int(obj2[3]), c=int(obj2[4]), d=0, membership=0, centroid=0)
                else:
                    f = fuzzysets(obj2[0], shape=obj2[1], a=int(obj2[2]), b=int(obj2[3]), c=int(obj2[4]), d=int(obj2[5]), membership=0,centroid=0)
                fuzzy.append(f)
            for i in v:
                if i.name==vname:
                    vw=i
            vw.fuzzysets=fuzzy
    index+=1
    rule=[]
    numR=int(r[index])
    for rr in range(numR):
        index+=1
        s=r[index]
        rule.append(s)
    #print(rule)
    index += 1
    numC=int(r[index])
    print("Crisps:")
    lc = []
    for nc in range(numC):
        index+=1
        s=r[index]
        s = s.split(":")
        s =int(s[1])
        lc.append(s)
    print(lc)
    #Access rules => rule
    #Access variables => v
    print(v)
    vars=v
    print(rule)
    for r in rule:
        inference(r, lc[0], lc[1], vars)
    defuz(vars)
if (choice == 2):
    exit()