# Leetcode no 1603 : Design Parking System 



class ParkingSystem: 

    def __init__(self, big: int, medium: int, small: int):
        self.Big = big
        self.Medium = medium
        self.Small = small
       

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.Big > 0:
                self.Big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.Medium > 0:
                self.Medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.Small > 0:
                self.Small -= 1
                return True
            else:
                return False
        

def main():
    parkingSystem = ParkingSystem(1, 1, 0)
    print(parkingSystem.addCar(1))  # returns True
    print(parkingSystem.addCar(2))  # returns True
    print(parkingSystem.addCar(3))  # returns False
    print(parkingSystem.addCar(1))  # returns False
    
if __name__ == "__main__":
    main()