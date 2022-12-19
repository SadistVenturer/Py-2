
class IPhone:
    """ Что-то для понимания класса """
    def __init__(self, capacity_memory: float, occupied_memory: float):
        if not isinstance(capacity_memory, (int, float)):
            raise TypeError("Объем памяти типа int или float")
        if capacity_memory <= 0:
            raise ValueError("Объем памяти - положительное число")
        self.capacity_memory = capacity_memory
        if not isinstance(occupied_memory, (int, float)):
            raise TypeError("Заполняемость памяти должна быть типа int или float")
        if occupied_memory < 0:
            raise ValueError("Кол-во занятой памяти не может быть отрицательным")
        self.occupied_memory = occupied_memory
    def is_empty_iphone(self) -> bool:
        def add_data_to_iphone(self, data: float) -> None:
            if not isinstance(water, (int, float)):
                raise TypeError("Заполняемость памяти должна быть типа int или float")
            if data < 0:
                raise ValueError("Кол-во занятой памяти не может быть отрицательным")
        def remove_data_from_iphone(self, estimate_data: float) -> None:
            if __name__ == "__main__":
                import doctest
                doctest.testmod()
            

class Humanity:
    """ Чтоб был докстринг """
    def __init__(self, midlife: float, quality_of_life: float):
        if not isinstance(midlife, (int, float)):
            raise TypeError("Средняя продолжительность жизни только типа int или float")
        if midlife <= 0:
            raise ValueError("Средняя продолжительность жизни - положительное число")
        self.midlife = midlife
        if not isinstance(quality_of_life, (int, float)):
            raise TypeError("Качество жизни должно быть типа int или float")
        if quality_of_life < 0:
            raise ValueError("Качество жизни не может быть отрицательным, хотя......")
        self.quality_of_life = quality_of_life
    def is_empty_humanity(self) -> bool:
        def add_index_to_humanity(self, index: float) -> None:
            if not isinstance(age, (int, float)):
                raise TypeError("Средняя продолжительность жизни должна быть типа int или float")
            if index < 0:
                raise ValueError("Качество жизни не может быть отрицательным, хотя......")
        def remove_index_from_humanity(self, estimate_data: float) -> None:
            if __name__ == "__main__":
                import doctest
                doctest.testmod()
                        

class Ball:
    """ Somehow """
    def __init__(self, air_pressure: float,amount_air: float):
        if not isinstance(air_pressure, (int, float)):
            raise TypeError("Давление воздуха - int или float")
        if midlife <= 0:
            raise ValueError("Давление воздуха - положительное число")
        self.air_pressure = air_pressure
        if not isinstance(amount_air, (int, float)):
            raise TypeError("Кол-во воздуха - типа int или float")
        if amount_air < 0:
            raise ValueError("Кол-во воздуха - не может быть отрицательным")
        self.amount_air = amount_air
    def is_empty_ball(self) -> bool:
        def add_quantity_to_ball(self, quantity: float) -> None:
            if not isinstance(quantity, (int, float)):
                raise TypeError("Давление воздуха - int или float")
            if quantity < 0:
                raise ValueError("Кол-во воздуха - типа int или float")
        def remove_quantity_from_ball(self, estimate_data: float) -> None:
            if __name__ == "__main__":
                import doctest
                doctest.testmod()