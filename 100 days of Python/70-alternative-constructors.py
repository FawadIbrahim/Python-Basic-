class employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.name=name
        self.id=id
        self.language=language

Fawad=employee('Fawad',2021)
Sameer=programmer('Sameer',2022,'Python')
print(Fawad.name)
print(Fawad.id)
print(Sameer.id)
