class parent():
    def show(self):
        print("inside parent class")
class child(parent):
    def show(self):
        super().show()
        print("inside child class")
obj=child()
obj.show()
    
