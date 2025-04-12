class color:
    def __init__(self):
        self.name="green"
        self.lg=self.Lightgreen()
    def show(self):
        print('Name:',self.name)
    class Lightgreen:
        def __init__(self):
            self.name='Lightgreen'
            self.code="024avc"
        def display(self):
            print('Name:',self.name)
            print('code:',self.code)
outer=color()
outer.show()
g=outer.lg
g.display()

