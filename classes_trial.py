class vehicle():
    Number=""
    make=""
    color=""
    value=10.00
    def description(self):
        print("The car number is {0} made by {1} ,color:{2},costs {3} /- rupeees".format(self.Number,self.make,self.color,self.value))
car1=vehicle()
car1.Number="AP21AL8251"
car1.make="BMW"
car1.color="Royal Blue"
car1.value=7500000
print(car1.description())