class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1=vector(3,4,5)
print(v1)
v2=vector(8,7,6)
print(v2)