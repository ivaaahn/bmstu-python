from tkinter import *
from tkinter import messagebox as mb
from math import sqrt, fabs

points = []
points_normal = []



CANVAS_WIDTH = 651
CANVAS_HEIGHT = 551
RECTANGLE = 1
WORK_WIDTH = CANVAS_WIDTH - RECTANGLE
WORK_HEIGHT = CANVAS_HEIGHT - RECTANGLE
PREC = 2

def clearCanvas() -> None:
    points.clear()
    points_normal.clear()
    canvas.delete("all")
    canvas.create_line(0, WORK_HEIGHT/2, WORK_WIDTH, WORK_HEIGHT/2, fill='black')  # OX
    canvas.create_line(WORK_WIDTH/2, 0, WORK_WIDTH/2, WORK_HEIGHT, fill='black')  # OY

    for i in range(5, WORK_WIDTH+1, 10):
        canvas.create_line(i, WORK_HEIGHT/2-2, i, WORK_HEIGHT/2+2, fill='black')

    for i in range(5, WORK_HEIGHT+1, 10):
        canvas.create_line(WORK_WIDTH/2-2, i, WORK_WIDTH/2+2, i, fill='black')

    canvas.create_text(WORK_WIDTH-10, WORK_HEIGHT/2+10, text='X')
    canvas.create_text(WORK_WIDTH/2-10, 10, text='Y')
    canvas.create_text(WORK_WIDTH/2-10, WORK_HEIGHT/2+10, text='O')
    canvas.create_rectangle(2, 2, CANVAS_WIDTH, CANVAS_HEIGHT, width=RECTANGLE)


def getLen(A: tuple, B: tuple) -> float:
    return sqrt((B[0]-A[0])*(B[0]-A[0]) + (B[1]-A[1])*(B[1]-A[1]))


def getLambda(A: tuple, B: tuple, C: tuple) -> float:
    return getLen(A, B) / getLen(A, C)


def getSquare(A: tuple, B: tuple, C: tuple) -> float:
    det = (A[0]-C[0])*(B[1]-C[1]) - (B[0]-C[0])*(A[1]-C[1])
    return fabs(det/2)


def getDiffSquare(A: tuple, B: tuple, C: tuple, L: tuple) -> float:
    return abs(getSquare(A, B, L) - getSquare(A, C, L))


def getCoord(A: tuple, B: tuple, lmbd: float) -> tuple:
    x = round((A[0] + lmbd * B[0]) / (1 + lmbd), 1)
    y = round((A[1] + lmbd * B[1]) / (1 + lmbd), 1)
    return (x, y,)


def checkError(x: str, y: str) -> bool:
    try:
        x = float(x)
        y = float(y)
        return True
    except:
        mb.showerror('Ошибка', 'Введены некорректные данные!')
        return False


def addPoint(event, src: str = 'entry', point: tuple = ()) -> None:
    global points

    if src == 'entry':
        x, y = eAddX.get(), eAddY.get()
        if checkError(x, y):
            point = denormalizeCoord(float(x), float(y))
            point_n = (float(x), float(y),)
            eAddX.delete(0, END)
            eAddY.delete(0, END)
        else:
            return
    else:
        point_n = normalizeCoord(point[0], point[1])

    if (0 <= point[0] <= WORK_WIDTH) and (0 <= point[1] <= WORK_HEIGHT):
        if point not in points:
            points.append(point)
            points_normal.append(point_n)
        else:
            mb.showwarning('Предупреждение', 'Данная точка уже была введена')
            return
    else:
        mb.showerror('Ошибка', 'Некорректный диапазон!')
        return

    if src == 'entry':
        canvas.create_line(point[0], point[1], point[0], point[1], width=3, fill='red',
                           capstyle=ROUND, smooth=TRUE, splinesteps=1)

    eAmountPoints.configure(state=NORMAL)
    eAmountPoints.delete(0, END)
    eAmountPoints.insert(0, str(len(points)))
    eAmountPoints.configure(state=DISABLED)


def solution() -> None:
    ans_points = []
    ans_points_n = []
    ans_diff = -1
    ans_diff_n = -1
    L_best = tuple()
    L_best_n = tuple()
    

    if len(points) < 3:
        mb.showerror('Ошибка', 'Введите хотя бы три точки!')
        return

    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                curr_points = [points[i], points[j], points[k]]
                curr_points_n = [points_normal[i], points_normal[j], points_normal[k]]
                for p in range(3):
                    A, B, C = curr_points[p], curr_points[(p + 1) % 3], curr_points[(p + 2) % 3]
                    A_n, B_n, C_n = curr_points_n[p], curr_points_n[(p + 1) % 3], curr_points_n[(p + 2) % 3]
                    if getSquare(A, B, C) < 1:
                        break
                    if ((getLen(A,B)) + getLen(A,C) - getLen(B,C) < PREC) or ((getLen(A,B)) + getLen(B,C) - getLen(A,C) < PREC) or\
                         ((getLen(B,C)) + getLen(A,C) - getLen(A,B) < PREC):
                        break
                    
                    lmbd = getLambda(A, B, C)
                    L = getCoord(B, C, lmbd)
                    L_n = getCoord(B_n, C_n, lmbd)
                    diff = getDiffSquare(A, B, C, L)
                    diff_n = getDiffSquare(A_n, B_n, C_n, L_n)
                    if (diff < ans_diff) or (ans_diff == -1):
                        ans_points = [A, B, C]
                        ans_points_n = [A_n, B_n, C_n]
                        ans_diff = diff
                        ans_diff_n = diff_n
                        L_best = L
                        L_best_n = L_n

    if len(ans_points) < 3:
        mb.showerror('Ошибка', 'Точки лежат на одной прямой!')
        return

    for q in (eBestPAX, eBestPAY, eBestPBY, eBestPCX, eBestPCY, eBestPBX, eDiff):
        q.configure(state=NORMAL)
        q.delete(0, END)

    Ax, Ay = ans_points[0][0], ans_points[0][1]
    Bx, By = ans_points[1][0], ans_points[1][1]
    Cx, Cy = ans_points[2][0], ans_points[2][1]
    Lx, Ly = L_best[0], L_best[1]

    canvas.create_line(Ax, Ay, Bx, By, width=1, fill='green')
    canvas.create_line(Cx, Cy, Bx, By, width=1, fill='green')
    canvas.create_line(Ax, Ay, Cx, Cy, width=1, fill='green')
    canvas.create_line(Ax, Ay, Lx, Ly, width=1, fill='blue')
    canvas.create_line(Ax, Ay, Ax, Ay, width=5, fill='red',
                       capstyle=ROUND, smooth=TRUE, splinesteps=1)
    canvas.create_line(Bx, By, Bx, By, width=5, fill='red',
                       capstyle=ROUND, smooth=TRUE, splinesteps=1)
    canvas.create_line(Cx, Cy, Cx, Cy, width=5, fill='red',
                       capstyle=ROUND, smooth=TRUE, splinesteps=1)
    canvas.create_line(Lx, Ly, Lx, Ly, width=5, fill='red',
                       capstyle=ROUND, smooth=TRUE, splinesteps=1)
                       
    Ax_n, Ay_n = ans_points_n[0][0], ans_points_n[0][1]
    Bx_n, By_n = ans_points_n[1][0], ans_points_n[1][1]
    Cx_n, Cy_n = ans_points_n[2][0], ans_points_n[2][1]
    Lx_n, Ly_n = L_best_n[0], L_best_n[1]

    # Ax, Ay = normalizeCoord(Ax, Ay)
    # Bx, By = normalizeCoord(Bx, By)
    # Cx, Cy = normalizeCoord(Cx, Cy)
    # Lx, Ly = normalizeCoord(Lx, Ly)

    for i, j in zip((Ax_n, Ay_n, Bx_n, By_n, Cx_n, Cy_n), (eBestPAX, eBestPAY, eBestPBX, eBestPBY, eBestPCX, eBestPCY)):
        j.insert(0, i)

    ans_diff_n = getDiffSquare((Ax_n, Ay_n,), (Bx_n, By_n,), (Cx_n, Cy_n,), (Lx_n, Ly_n,))
    eDiff.insert(0, round(ans_diff_n, 1))

    for q in (eBestPAX, eBestPAY, eBestPBY, eBestPCX, eBestPCY, eBestPBX, eDiff):
        q.configure(state=DISABLED)


def normalizeCoord(x: int, y: int) -> (float, float,):
    x = round((x - WORK_WIDTH/2)*100/WORK_WIDTH, 1)
    y = round(-(y - WORK_HEIGHT/2)*100/WORK_HEIGHT, 1)
    return (x, y,)


def denormalizeCoord(x: float, y: float) -> (int, int,):
    x = round(x * WORK_WIDTH / 100 + WORK_WIDTH/2)
    y = round(-y * WORK_WIDTH / 100 + WORK_HEIGHT/2)

    return (x, y,)


def getPos(event):
    x, y = normalizeCoord(event.x, event.y)

    eXPos.configure(state=NORMAL)
    eYPos.configure(state=NORMAL)

    eXPos.delete(0, END)
    eYPos.delete(0, END)

    eXPos.insert(0, str(x))
    eYPos.insert(0, str(y))

    eXPos.configure(state=DISABLED)
    eYPos.configure(state=DISABLED)


def setPoint(event) -> None:
    x, y = event.x, event.y
    canvas.create_line(x, y, x, y, width=3, fill='red',
                       capstyle=ROUND, smooth=TRUE, splinesteps=1)
    addPoint('', 'canvas', (x, y,))


root = Tk()
root.title("Лабораторная работа #4")
root.geometry("1000x600")
root.resizable(0, 0)


fWorkDir = Frame(root)
fWorkDir.pack(side=LEFT, anchor='n')

fAddPoint = Frame(fWorkDir)
lAddPoint = Label(fAddPoint, text='Введите точку:', font="Segoe 13 bold")
lAddX = Label(fAddPoint, text='X:', font="Segoe 12")
lAddY = Label(fAddPoint, text='Y:', font="Segoe 12")
eAddX = Entry(fAddPoint, font=18, width=8)
eAddY = Entry(fAddPoint, font=18, width=8)
bAddPoint = Button(fAddPoint, text='Add', command=lambda x='entry': addPoint("", x), font='Cambria 12 bold',
                   width=10, height=2, bg='black', activebackground="#0B5FA4", fg='white')

fAddPoint.pack(side=TOP, anchor='w', pady=20)
lAddPoint.pack(side=TOP, pady=10)
lAddX.pack(side=LEFT, padx=5)
eAddX.pack(side=LEFT, ipady=8)
lAddY.pack(side=LEFT, padx=5)
eAddY.pack(side=LEFT, ipady=8)
bAddPoint.pack(padx=10)


fAmountPoints = Frame(fWorkDir)
lAmountPoints = Label(
    fAmountPoints, text='Точек введено:', font="Segoe 13 bold")
eAmountPoints = Entry(fAmountPoints, font=18, width=8)
eAmountPoints.insert(0, len(points))
eAmountPoints.configure(state=DISABLED)


fAmountPoints.pack(pady=5)
lAmountPoints.pack()
eAmountPoints.pack(ipady=8)

bSearch = Button(fWorkDir, text='Search', command=solution, font='Cambria 12 bold',
                 width=20, height=2, bg='black', activebackground="#0B5FA4", fg='white')
bSearch.pack(pady=20)


fAnswer = Frame(fWorkDir)
Label(fAnswer, text='Answer:', font="Segoe 12 bold").pack(pady=5)
fBestPoints = Frame(fAnswer)
fAnswer.pack(pady=5)
fBestPoints.pack(pady=5)

fBestAPoint = Frame(fBestPoints)
lBestAPoint = Label(fBestAPoint, text='A:', font="Segoe 12 bold")

fBestPALabel = Frame(fBestAPoint)
lBestPAX = Label(fBestPALabel, text='X:', font="Segoe 12 bold")
lBestPAY = Label(fBestPALabel, text='Y:', font="Segoe 12 bold")

fBestPAEntry = Frame(fBestAPoint)
eBestPAX = Entry(fBestPAEntry, font=18, width=5, state=DISABLED)
eBestPAY = Entry(fBestPAEntry, font=18, width=5, state=DISABLED)

fBestAPoint.pack(side=LEFT)
lBestAPoint.pack()
fBestPALabel.pack()
lBestPAX.pack(side=LEFT, padx=5)
lBestPAY.pack(side=LEFT, padx=5)
fBestPAEntry.pack()
eBestPAX.pack(side=LEFT, ipady=8)
eBestPAY.pack(side=LEFT, ipady=8)


fBestBPoint = Frame(fBestPoints)
lBestBPoint = Label(fBestBPoint, text='B:', font="Segoe 12 bold")

fBestPBLabel = Frame(fBestBPoint)
lBestPBX = Label(fBestPBLabel, text='X:', font="Segoe 12 bold")
lBestPBY = Label(fBestPBLabel, text='Y:', font="Segoe 12 bold")

fBestPBEntry = Frame(fBestBPoint)
eBestPBX = Entry(fBestPBEntry, font=18, width=5, state=DISABLED)
eBestPBY = Entry(fBestPBEntry, font=18, width=5, state=DISABLED)

fBestBPoint.pack(side=LEFT)
lBestBPoint.pack()
fBestPBLabel.pack()
lBestPBX.pack(side=LEFT, padx=5)
lBestPBY.pack(side=LEFT, padx=5)
fBestPBEntry.pack()
eBestPBX.pack(side=LEFT, ipady=8)
eBestPBY.pack(side=LEFT, ipady=8)


fBestCPoint = Frame(fBestPoints)
lBestCPoint = Label(fBestCPoint, text='C:', font="Segoe 12 bold")

fBestPCLabel = Frame(fBestCPoint)
lBestPCX = Label(fBestPCLabel, text='X:', font="Segoe 12 bold")
lBestPCY = Label(fBestPCLabel, text='Y:', font="Segoe 12 bold")

fBestPCEntry = Frame(fBestCPoint)
eBestPCX = Entry(fBestPCEntry, font=18, width=5, state=DISABLED)
eBestPCY = Entry(fBestPCEntry, font=18, width=5, state=DISABLED)

fBestCPoint.pack(side=LEFT)
lBestCPoint.pack()
fBestPCLabel.pack()
lBestPCX.pack(side=LEFT, padx=5)
lBestPCY.pack(side=LEFT, padx=5)
fBestPCEntry.pack()
eBestPCX.pack(side=LEFT, ipady=8)
eBestPCY.pack(side=LEFT, ipady=8)


fDiff = Frame(fAnswer)
lDiff = Label(fDiff, text='Best Difference: ', font="Segoe 12 bold")
eDiff = Entry(fDiff, font=18, width=10, state=DISABLED)

fDiff.pack(pady=15)
lDiff.pack(side=LEFT)
eDiff.pack(side=LEFT, ipady=8)


fCanvas = Frame(root)
fCanvas.pack(side=LEFT)

canvas = Canvas(fCanvas, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.bind("<Button-1>", setPoint)
canvas.bind("<Motion>", getPos)
canvas.pack()

clearCanvas()

fPosition = Frame(fCanvas)

lXPos = Label(fPosition, text='X:', font="Segoe 7 bold")
lYPos = Label(fPosition, text='Y:', font="Segoe 7 bold")
eXPos = Entry(fPosition, font=4, width=8, state=DISABLED)
eYPos = Entry(fPosition, font=4, width=8, state=DISABLED)
bclearCanvas = Button(fPosition, text='Clear', command=clearCanvas, font='Cambria 12 bold',
                 width=5, height=1, bg='black', activebackground="#0B5FA4", fg='white')



fPosition.pack()
lXPos.pack(side=LEFT)
eXPos.pack(side=LEFT)
lYPos.pack(side=LEFT)
eYPos.pack(side=LEFT)
bclearCanvas.pack(side=RIGHT, anchor='e')

root.bind('<Return>', addPoint)

root.mainloop()
