class Distance:
    def __init__(self, km , m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Constructor called, Object deleted.")

    def displayData(self):
        print(f"{self.km} km, {self.m} m, {self.cm} cm")

    def __add__(self, other):
        n_km = self.km + other.km
        n_m = self.m + other.m
        n_cm = self.cm + other.cm

        if n_cm >= 100:
            n_m += n_cm // 100
            n_cm += n_cm % 100

        if n_m >= 1000:
            n_km += n_m // 1000
            n_m = n_m % 1000

        return Distance(n_km, n_m, n_cm)
    
    def __sub__(self, other):
        n_km = self.km + other.km
        n_m = self.m + other.m
        n_cm = self.cm + other.cm

        if n_cm < 0:
            n_m -= 1
            n_cm += 100

        if n_m < 0:
            n_km  -= 1
            n_m += 1000

        return Distance(n_km, n_m, n_cm)
    
d1 = Distance(2, 500, 75)
d2 = Distance(1, 800, 50)

print("Distance 1: ")
d1.displayData()

print("Distance 2: ")
d2.displayData()

d3 = d1 + d2
print("After Addition: ")
d3.displayData()

d4 = d1 - d2
print("After Substraction: ")
d3.displayData()