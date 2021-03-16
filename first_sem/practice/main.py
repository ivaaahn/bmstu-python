# Проверка того, можно ли делать шаг в заданном направлении
def checkFreeWay(points: set, x: int, y: int, step: int, dir: str) -> bool:
    if dir == "n":
        for yNew in range(y + 1, y + step + 1):
            if (x, yNew) in points:
                return False
    elif dir == "s":
        for yNew in range(y - 1, y - step - 1, -1):
            if (x, yNew) in points:
                return False
    elif dir == "e":
        for xNew in range(x + 1, x + step + 1):
            if (xNew, y) in points:
                return False
    elif dir == "w":
        for xNew in range(x - 1, x - step - 1, -1):
            if (xNew, y) in points:
                return False
    return True


def exploreMe(x: int, y: int, curStep: int, tempWay: list, rPoints: set):
    lastDir = tempWay[-1]

    # проверка, был ли последний ход выгодным.
    # Последний ход по данной оси был curStep+1: следующий ход по той же оси: curStep-1
    maxWay = sum([step for step in range(curStep - 1, 0, -2)])
    ways = []

    if curStep > 0:
        if (lastDir == "w" or lastDir == "e") and maxWay >= abs(x):
            if checkFreeWay(rPoints, x, y, curStep, "n"):
                ways += exploreMe(x, y + curStep, curStep - 1, tempWay + ["n"], rPoints)
            if checkFreeWay(rPoints, x, y, curStep, "s"):
                ways += exploreMe(x, y - curStep, curStep - 1, tempWay + ["s"], rPoints)
        elif (lastDir == "s" or lastDir == "n") and maxWay >= abs(y):
            if checkFreeWay(rPoints, x, y, curStep, "e"):
                ways += exploreMe(x + curStep, y, curStep - 1, tempWay + ["e"], rPoints)
            if checkFreeWay(rPoints, x, y, curStep, "w"):
                ways += exploreMe(x - curStep, y, curStep - 1, tempWay + ["w"], rPoints)
    elif x == y == 0:
        tempWay.reverse()
        way = ["s" if x == "n" else "n" if x == "s" else "e" if x == "w" else "w" if x == "e" else x for x in
               tempWay[:-1]]
        ways = ["".join(way)]
    return ways


def explore(maxStep: int, rPointsOfCity: set) -> list:
    ways = []
    for startDir in "ws":
        ways += exploreMe(0, 0, maxStep, [startDir], rPointsOfCity)
    return ways


# функция для ввода координат ремонтируемых улиц
def rPointsInput(rPointsAmount: int) -> set:
    rPoints = set()
    for curPoint in range(rPointsAmount):
        rPoints.add(
            (tuple(point for point in map(int, input("Введите координаты участка {}: "
                                                     .format(curPoint + 1)).split()))))
        return rPoints

    # функция для ввода всех основных значений
    def inputValues(cityNum: int, maxStep: list, rPointsAmount: list, allrPoints: list):
        curMaxStep = int(input("Введите максимальную длину шага в городе #{}: ".format(cityNum + 1)).strip())
        maxStep.append(curMaxStep)

        currPoints = int(input(
            "Введите кол-во ремонтируемых участков дороги в городе #{}(не более 50): ".format(cityNum + 1)).strip())
        rPointsAmount.append(currPoints)

        # Все координаты улиц(Points), закрытых на ремонт храним в сете, а каждый такой сет в списке allrPoints
        allrPoints.append(rPointsInput(rPointsAmount[cityNum]))

    # Здесь храним максимальный шаг для каждого города
    maxStep = list()

    # Здесь храним количество дорог, закрытых на ремоннт, в данном городе
    rPointsAmount = list()

    # Здесь храним координаты всех закрытых на ремонт дорог для каждого города
    allrPoints = list()

    # Здесь храним кол-во всех городов
    numOfCities = int(input("Введите кол-во городов: ").strip())

    # Ввод основных данных для каждого из городов
    for curCityNum in range(numOfCities):
        inputValues(curCityNum, maxStep, rPointsAmount, allrPoints)

    # Поиск решений для каждого города
    for curCityNum in range(numOfCities):
        ways = explore(maxStep[curCityNum], allrPoints[curCityNum])
        print("")
        print("Город #{}".format(curCityNum + 1))
        for i in range(len(ways)):
            print("{}: {}".format(i + 1, ways[i]))
        print("Голигонов найдено: {}".format(len(ways)))
