class Underscore(object):
    def map(self, list, callback):
        for key in range(len(list)):
            list[key] = callback(list[key])
        return list
        # your code here
    def find(self, list, callback):
        for item in list:
            if callback(item):
                return item
        return False
        # your code here
    def reduce(self, list, callback, *memo):
        try:
            memo = memo[0]
        except:
            memo = 0
        for item in list:
            memo = callback(memo,item)
        return memo
        # your code here
    def filter(self, list, callback):
        i = 0
        while i < len(list):
            if (not callback(list[i])):
                list.pop(i)
                i -= 1
            i += 1
        return list
    def reject(self, list, callback):
        i = 0
        while i < len(list):
            if (callback(list[i])):
                list.pop(i)
                i -= 1
            i += 1
        return list
        # your code
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2)
print(evens)
# should return [2, 4, 6] after you finish implementing the code above