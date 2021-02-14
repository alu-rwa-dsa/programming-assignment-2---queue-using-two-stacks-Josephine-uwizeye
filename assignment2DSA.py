class Queue():
    def main(self):
        self.s1 = []
        self.s2= []

        for i in range(int(input())):
            a = list(map(int, input().split()))

            if a[0] == 1: #this will push item to stack1
                self.s1.append(a[1])

            elif a[0] == 2: # tthis will ake element from s1 to s2
                if not self.s2:
                    while self.s1:
                        self.s2.append(self.s1.pop()) #this will pop from s1 & append to s2
                self.s2.pop()

            elif a[0] == 3: # this will check element on top of the stack
                if not self.s2:
                    while self.s1:
                        self.s2.append(self.s1.pop())
                print(self.s2[-1])


if __name__ == '__main__':
    x = Queue()
    x.main()