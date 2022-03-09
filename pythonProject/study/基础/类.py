class SetText():
    @classmethod
    def classMethod1(cls,str):
        print(str)
    def __init__(self):
        self.value="高冷"

    def show(self):
        print(self.value)


SetText.classMethod1("曾宇峥")
settext=SetText()
SetText.show(settext)
settext.show()

