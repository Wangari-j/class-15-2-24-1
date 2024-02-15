class mountains:
    volcano = ""
    state = ""

    def moExample(self):
        print("Mt.Kenya and Mt. Kilimanjaro are volcano mountains in Africa.")
        

mountains1 = mountains
mountains2 = mountains

mountains1.volcano = "some mountains are volcano"
mountains1.state = "Most are inactive"

print(mountains1.volcano)
print(mountains1.state)

mountains1.moExample
