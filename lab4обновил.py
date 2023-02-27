import doctest
class Car:
    
    """
    Класс, описывающий автомобили
    """
    count_of_wheels = 4
    
    def __init__(self, model: str, year: int, engine_capacity: float, cost: int, odometer: int, passengers: int):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.cost = cost
        self.odometer = odometer
        self.passengers = passengers
    #def display_info(self):
      #  print(f" Автомобиль {self.model}, выпущенный в {self.year} году с объемом двигателя {self.engine_capacity}. Стоит {self.cost} с  пробегом {self.odometer} километров. База оснащена {self.count_of_wheels} колесами.")
    
    def __str__(self):
        return f" Автомобиль {self.model}, выпущенный в {self.year} году с объемом двигателя {self.engine_capacity}. Стоит {self.cost} с  пробегом {self.odometer} километров. База оснащена {self.count_of_wheels} колесами. Вмещает аж {self.passengers})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, year={self.year!r}, engine_capacity={self.engine_capacity!r}, cost={self.cost!r}, odometer={self.odometer!r}, count_of_wheels={self.engine_capacity!r}, passengers={self.passengers!r})"
     
    def capacity(self) -> int:
        """
        Метод возращает вместимость ТС
        Аргументы: -
        Возвращаемое значение:
            capacity -- вместимость
            >>> car1 = Car(2020, 3.0, 4000000, 25000, 5)
            >>> car1.capacity()
            [5]
            ...
        """
        return self.passengers   
    
    def something(self) -> str:
        """
        Метод возращает что-то
        Аргументы: сомнительные
        Возвращаемое значение:
            something -- что-то
            >>> car1 = Car(2020, 3.0, 4000000, 25000, 5, something)
            >>> car1.something()
            [5]
            ...
        """
        return self.somehow
        
class Cargo(Car):

    """
    Дочерний класс, описывающий грузовые автомобили
    """
    count_of_wheels = 8
    
    def __init__(self, model: str, year: int, engine_capacity: float, cost: int, odometer: int, passengers: int, fuelcap: float, g_fuel: float):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.cost = cost
        self.odometer = odometer
        self.passengers = passengers
        self.fuelcap = fuelcap
        self.g_fuel = g_fuel
    
    def range(self) -> float:
        """
        Метод возвращает расстояние, которое машина пройдет на полном баке
        Аргументы: - 
        Возвращаемое значение: 
            range -- расстояние
            >>> car2 = Cargo(2010, 8.0, 1E7, 250000, 2, 200, 15)
            >>> car2.range()
            []
            ...
        """
        return self.fuelcap / self.g_fuel * 100
        
    

if __name__ == "__main__":
    doctest.testmod()
    
    car1 = Car('BMW', 2020, 3.0, 4000000, 25000, 5 )
    print(car1.__str__())
    print(car1.__repr__())
    car2 = Cargo('MAN', 2010, 8.0, 1E7, 250000, 2, 200, 15)
    print(car2.__str__())
    print(car2.__repr__())