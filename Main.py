from tkinter import *
from Node import Node
from Connector import Connector
from math import sqrt
import time
import random

tk = Tk()
tk.title("Модель Барабаши — Альберт")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=800, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
tm = 0.1

r = 200
x0=400
y0=400

x = 400
y = 200
ylim=y+y0
N = 50
m0 = 20
count = 0
nodes = []


def calculate_coords():
    global y
    global x
    global count
    # print(count)
    if (N % 2 != 0 and count == N // 2):
        count += 1
        x = x0 - sqrt(r ** 2 - (y0 - y) ** 2)
        return
    h = 0
    m = True
    if (x >= x0 and y < ylim):
        h = 2 * y0 / (N)
        y = y + h
        x = x0 + sqrt(r ** 2 - (y0 - y) ** 2)
        m = False
        count += 1
        return

    if (x <= 400 or m):
        h = -2 * 400 / (N)
        y = y + h
        x = 400 - sqrt(r ** 2 - (400 - y) ** 2)
        count += 1
        return
    # print(h)


def sum():
    summa = 0
    for i in nodes:
        summa += i.get_rank()
    return summa


def get_probability(node):
    return node.rank / sum()


nodes.append(Node(canvas, x, y, 0))

for i in range(1, m0):
    calculate_coords()
    nodes.append(Node(canvas, x, y, 0))
    a = random.randint(0, i - 1)
    # a = i-1
    # Connector(canvas, nodes[i], nodes[a]).connect()
random.shuffle(nodes)
for n1 in nodes:
    for n2 in nodes:
        if (random.randint(0, 6) >=1 and n1!=n2):
            Connector(canvas, n1, n2).connect()

tk.update_idletasks()
tk.update()
time.sleep(tm)

for i in range(m0, N):
    calculate_coords()
    nodes = sorted(nodes, key=get_probability, reverse=True)
    j = 0
    nodes.append(Node(canvas, x, y, 0))
    if (len(nodes) > 1):
        rnk = nodes[0].get_rank()
        while ((j != len(nodes) - 1) and (nodes[j].get_rank() == rnk)):
            # print(j)
            Connector(canvas, nodes[len(nodes) - 1], nodes[j]).connect()
            j += 1

    tk.update_idletasks()
    tk.update()
    time.sleep(tm)
time.sleep(60)
