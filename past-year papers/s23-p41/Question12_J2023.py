class Vehicle():
    # self.__ID string
    # self.__MaxSpeed integer
    # self.__IncreaseAmount integer
    # self.__CurrentSpeed integer
    # self.__HorizontalPosition integer
    def __init__(self, IDinput, MaxSpeedInput, IncreaseAmountInput):
        self.__ID = IDinput
        self.__MaxSpeed = MaxSpeedInput
        self.__IncreaseAmount = IncreaseAmountInput
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0
    
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed
    def SetHorizontalPosition(self, pos):
        self.__HorizontalPosition = pos
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

    def OutputCurrentPosition(self):
        print("current position: ", self.__HorizontalPosition)
        print("current speed: ", self.__CurrentSpeed)
    
class Helicopter(Vehicle):
    # self.__VerticalChange integer
    # self.__MaxHeight integer
    # self.__VerticalPosition integer
    def __init__(self, IDinput, MaxSpeedInput, IncreaseAmountInput, VerticalChangeInput, MaxHeightInput):
        Vehicle.__init__(self, IDinput, MaxSpeedInput, IncreaseAmountInput)
        self.__VerticalChange = VerticalChangeInput
        self.__MaxHeight = MaxHeightInput
        self.__VerticalPosition = 0
    
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self))
        if (Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self)):
            Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self)) 
        Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))

    def OutputCurrentPosition(self):
        print("Current speed: ", Vehicle.GetCurrentSpeed(self))
        print("Horizontal position: ", Vehicle.GetHorizontalPosition(self))
        print("Vertical position: ", self.__VerticalPosition)

def main():
    car = Vehicle("Tiger", 100, 20)
    copter = Helicopter("Lion", 350, 40, 3, 100)
    car.IncreaseSpeed()
    car.IncreaseSpeed()
    car.OutputCurrentPosition()
    copter.IncreaseSpeed()
    copter.IncreaseSpeed()
    copter.OutputCurrentPosition()

main()