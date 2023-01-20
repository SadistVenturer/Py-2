class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name (self):
        return self.__name
     
    @property      
    def author (self):
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f'Error input count of pages: {pages!r}')
        else:
            raise AttributeError(f'Error input type of pages: {pages!r}')
         
    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nСтраниц: {self.pages}"
 #   def __repr__(self):
  #      return f"{self.__class__.__name__}(name ={self.name!r}, author ={self.author!r}, pages ={self.pages!r})"
        
  #  def __setattr__(self, attr, value):
   #     if attr == 'pages':
   #         if value > 0:
   #             attr = value
  #          else:
  #              raise AttributeError(f"Введено недопустимое число страниц: {value!r}")


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise AttributeError(f'Error input count of duration: {duration!r}')
        else:
            raise AttributeError(f'Error input type of duration: {duration!r}')
    
    def __str__(self):
        return f"Аудиокнига: {self.name}\nАвтор: {self.author}\nДлительность: {self.duration} часа(часов)"
        #self.duration = duration
    
   # def __repr__(self):
   #     return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
        
    #def __setattr__(self, attr, value):
      #  if attr == 'duration':
        #    if value > 0:
          #      attr = value
            #else:
              #  raise AttributeError(f"Введено недопустимое число страниц: {duration!r}")
        #else:
          #  attr = value

if __name__ == "__main__":
    
    pb1 = PaperBook("Тепловой расчет", 'Г.А. Зальф', 203)
    #pb1.name = "Book1"
    print(pb1.__str__())
    print(pb1.__repr__())
    
    ab1 = AudioBook("Гарри Потный", 'Джуан Роулинг', 6.0)
    #ab1.name = "Book2"
    print(ab1.__str__())
    print(ab1.__repr__())