class Call(object):
    def __init__(self, call_id, caller, caller_number, time, reason):
        self.call_id = call_id
        self.caller = caller
        self.caller_number = caller_number
        self.time = time
        self.reason = reason
    def display(self):
        print "====" + str(self.call_id) + "===="
        print "Caller: " + self.caller
        print "Number: " + self.caller_number
        print "Time: " + self.time
        print "Reason :" + self.reason

class CallCenter(object):
    def __init__(self, call_list):
        self.call_list = call_list
        self.queue_size = len(call_list)
    def add(self, call):
        self.call_list.append(call)
        return self
    def remove(self):
        self.call_list.pop(0)
        return self
    def info(self):
        print "Queue length = " + str(self.queue_size)
        for call in self.call_list:
            print "Name: " + call.caller + " | Number: " + call.caller_number
        return self
    def removeNum(self, number):
        i = 0
        while i < len(self.call_list):
            if self.call_list[i].caller_number == number:
                self.call_list.pop(i)
            i+=1
        return self
    def sort(self):
        #Had to use wrapper to get compare function to be Python 2/3 neutral key
        self.call_list = sorted(self.call_list, key=cmp_to_key(compare))
        return self

def compare(x,y):
    if (x.time.find("am") > -1 and y.time.find("am") > -1) or (x.time.find("pm") > -1 and y.time.find("pm") > -1):
        if x.time > y.time:
            return 1
        elif x.time == y.time:
            return 0
        else:
            return -1
    elif x.time.find("am") > -1 and y.time.find("pm") > -1:
        return -1
    elif x.time.find("pm") > -1 and y.time.find("am") > -1:
        return 1

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

call1 = Call(1,"First Guy", "555-5555", "6:57am", "angry")
call2 = Call(2,"Second Guy", "555-5556", "4:55pm", "angry")
call3 = Call(3,"Last Guy", "555-5557", "6:57pm", "angry")
call4 = Call(4,"Same Guy", "555-5557", "6:57am", "angry")

center = CallCenter([call2,call3,call1,call4])
center.info().sort().info()