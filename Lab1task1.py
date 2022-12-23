import doctest


class GasTurbine:
    def __init__(self, Power: float, KPD: float, G_exh: float, T_exh: float):
        self.Power = Power
        self.KPD = KPD
        self.G_exh = G_exh
        self.T_exh = T_exh
         #Power: Мощность на валу ГТУ, МВт
         #KPD: КПД ГТУ, %
         #G_exh: Расход уходящих газов, кг/с
         #T_exh: Температура уходящих газов, С

        if not isinstance(Power, (int, float)):
            raise TypeError("Мощность на валу ГТУ должнa быть типа int или float")
        if Power <= 0:
            raise PowerError("Мощность на валу ГТУ должнa быть положительным числом")

        if not isinstance(KPD, (int, float)):
            raise TypeError("КПД ГТУ должно быть int или float")
        if KPD < 0:
            raise KPDError("КПД ГТУ не может быть отрицательным числом")
        
        if not isinstance(G_exh, (int, float)):
            raise TypeError("Расход уходящих газов должнен быть int или float")
        if G_exh < 0:
            raise G_Error("Расход уходящих газов не может быть отрицательным числом")
        
        if not isinstance(T_exh, (int, float)):
            raise TypeError("Температура уходящих газов должнa быть int или float")
        if T_exh < 0:
            raise T_Error("Температура уходящих газов не может быть отрицательным числом")

    def Power_t_amb(self, t_amb: float, TNH: float) -> float:
        """
        Метод, вычисляющий мощность на валу ГТУ в зависимости от температуры наружного воздуха t_amb.
        Аргументы:
            t_amb -- температура наружного воздуха, С
            TNH -- относительные обороты турбины, %
        Возвращаемое значение:
            N_t -- мощность на валу ГТУ, МВт
            
        >>> T32 = GasTurbine(32, 36, 102, 510)
        >>> T32.Power_t_amb(15, 100)
        [33.779]
        
        >>> T32.Power_t_amb(-40, 100)
        Traceback (most recent call last)
            ...
            TypeError: t_amb должна быть больше -30 С
        """
        if t_amb > 50:
            raise TypeError("t_amb должна быть меньше +50 С")
        if t_amb < -30:
            raise TypeError("t_amb должна быть больше -30 С")
        if TNH != 100:
            raise TNH_Error("TNH должна быть 100%")
        N_t = self.Power * (-4e-05 * t_amb ** 2 - 0.0052 * t_amb +1.0801)
        return N_t
if __name__ == "__main__":
    doctest.testmod()



class Vehicle:
    """Класс, описывающий ТС"""
    
    
    def __init__(self, passengers: int, fuelcap: float, g_fuel: float):
        self.passengers = passengers
        self.fuelcap = fuelcap
        self.g_fuel = g_fuel
        
        
    def capacity(self) -> int:
        """
        Метод возращает вместимость ТС
        Аргументы: -
        Возвращаемое значение:
            capacity -- вместимость
            >>> v1 = Vehicle(5, 65, 7)
            >>> v1.capacity()
            [5]
            ...
        """
        return self.passengers
        
        
    def range(self) -> float:
        """
        Метод возвращает расстояние, которое машина пройдет на полном баке
        Аргументы: - 
        Возвращаемое значение: 
            range -- расстояние
            >>> v1 = Vehicle(5, 65, 7)
            >>> v1.range()
            [750]
            ...
        """
        return self.fuelcap / self.g_fuel * 100
            
if __name__ == "__main__":
    doctest.testmod()
    
    BMW_X3 = Vehicle(5, 65, 7)
    print('BMW_X3 перевозит', BMW_X3.capacity(), 'пассажиров на расстояние', BMW_X3.range(), 'км')
    
class Drinks:
    """
    Класс, описывающий алкогольные напитки
    strenght - крепость напитка
    """
    def __init__(self, strenght: float):
        self.strenght = strenght
        
    def alc(self, volume: float) -> float:
        """
        Метод возвращает объем спирта в объеме напитка
        Аргументы: volume
        Возвращаемое значение:
        alc -- кол-во спирта
        >>> vodka = Drinks(40)
        >>> vodka.alc(1)
        ...
        """
        alc_cup = volume * self.strenght / 100
        return alc_cup 
        
if __name__ == "__main__":
    doctest.testmod()
    
    
    drink_vol = 1
    vodka = Drinks(40)
    beer = Drinks(4)
    
    print('В', drink_vol, 'литре напитка', vodka.alc(drink_vol), 'литра спирта')