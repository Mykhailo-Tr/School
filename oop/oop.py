class Car:
    def __init__(self, id: int, doors=4) -> None:
        self.id = id
        self.wheels = 4
        self.doors = doors
        
        
class Sedan(Car):
    def __init__(self, id: int) -> None:
        super().__init__(id, 2)
    
    def start(self) -> None:
        print("Car started!")
        
        
def main():
    car = Car(1)
    audi = Sedan(2)
    audi.start()
    
if __name__ == '__main__':
    main()