def fun1(msg):
    def func2():
        print(msg)
    func2()
fun1("Hello")