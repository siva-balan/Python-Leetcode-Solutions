class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.arr = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.arr[0] > 0:
            self.arr[0] -=1
            return True
        elif carType == 2 and self.arr[1] > 0:
            self.arr[1] -=1
            return True
        elif carType == 3 and self.arr[2] > 0:
            self.arr[2] -=1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
