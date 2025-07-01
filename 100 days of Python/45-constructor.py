class person:
    def __init__(self,n,o):
       self.name=n
       self.occu=o

    def info(self):
        print(f"{self.name} is a {self.occu}")


a=person("Fawad", "Developer")
b=person("Sameer","HR")
a.info()
b.info()
# a.name="Sameer"
# a.occu="HR"
# a.info()