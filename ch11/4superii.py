#super() method

# Method	A function defined "inside" a class ✅
# Function	General-purpose code block (may or "may not" be inside a class)

# super().method() — because we're calling a method, not just any function.

# super() gives you "access" to the parent class, and 
# super().method() "calls" the method from that class.

class A:
    a=1
    def __init__(self):
        print('Constructor A')

    def level(self):
        print('level 1')

class B(A):
    b=2
    def __init__(self):
        # super().__init__()
        print('Constructor B')

    def level(self):
        super().level()
        print('level 2')

class C(B):
    c=3
    def __init__(self):
        super().__init__()      #Calling parent constructor
        print('Constructor C')

    def level(self):
        super().level()         #(Using overridden methods)
        print('level 3')

obj=C()
obj.level()