from abc import ABC, abstractmethod
"""
Стратегия – это поведенческий паттерн проектирования, который
определяет семейство схожих алгоритмов и помещает каждый из них в
собственный класс, после чего алгоритмы можно взаимозаменять прямо во
время исполнения программы.
Вы решили написать приложение-навигатор для путешественников.
Оно должно показывать красивую и удобную карту, позволяющую с лёгкостью
ориентироваться в незнакомом городе.
Одной из самых востребованных функций являлся поиск и
прокладывание маршрутов. Пребывая в неизвестном ему городе, пользователь
должен иметь возможность указать начальную точку и пункт назначения, а
навигатор – проложит оптимальный путь.
В этом примере каждый алгоритм поиска пути переедет в свой
собственный класс. В этих классах будет определён лишь один метод,
принимающий в параметрах координаты начала и конца пути, а
возвращающий массив точек маршрута. Реализуйте класс навигатора,
который по переданной ему стратегии выполняет построение маршрута.
"""


class Point:
    def __init__(self, point_x: int, point_y: int):
        self.__point_x = point_x
        self.__point_y = point_y

    def __str__(self):
        return f"{self.__point_x}, {self.__point_y}"

class BaseStrategy(ABC):

    @abstractmethod
    def build_route(self, start: Point, finish: Point):
        raise NotImplementedError

class WalkingStrategy(BaseStrategy):
    def build_route(self, start: Point, finish: Point):
        return f"Маршрут пешком из пункта {start} построен в пункт {finish} "

class DriveStrategy(BaseStrategy):
    def build_route(self, start: Point, finish: Point):
        return f"Маршрут на автомобиле из пункта {start} построен в пункт {finish}"

class Transport(BaseStrategy):
    def build_route(self, start: Point, finish: Point):
        return f"Маршрут на общественном транспорте из пункта {start} построен в пункт {finish}"

class Navigator:
    strategy: BaseStrategy

    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def build_route(self,start: Point, finish: Point):
        return self.strategy.build_route(start,finish)


def execute_application():

    st = Point(1, 9)
    fin = Point(52,64)
    navigator = Navigator()
    walk = WalkingStrategy()
    car = DriveStrategy()
    tran = Transport()

    navigator.set_strategy(car)
    print(navigator.build_route(st, fin))

    navigator.set_strategy(walk)
    print(navigator.build_route(st, fin))

    navigator.set_strategy(tran)
    print(navigator.build_route(st, fin))



if __name__ == "__main__":
    execute_application()
