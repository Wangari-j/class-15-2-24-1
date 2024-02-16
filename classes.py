class Mountains:
    volcano = ""
    state = ""

    def moExample(self):
        print("Mt.Kenya and Mt. Kilimanjaro are volcano mountains in Africa.")
        
    def __init__(self,volcano,state):
        self.volcano = volcano
        self.state = state


mountains1 = Mountains("kenya", "dormant")
mountains2 = Mountains("volcano","state")

mountains1.volcano = "some mountains are volcano"
mountains1.state = "Most are inactive"

print(mountains1.volcano)
print(mountains1.state)

mountains1.moExample()
