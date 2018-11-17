class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


if __name__ == '__main__':
    x = C()
    print("number of instnace = " + str(C.counter))
    y = C()
    print("number of instnace = " + str(C.counter))
    del x
    print("number of instnace = " + str(C.counter))
    del y
    print("number of instnace = " + str(C.counter))