from random import randint
s = ['💎','🎯', '🐀']
x = 3
y = 3
def gen_row(l):
    row = []
    for i in range(0,l):
        el_index = randint(0,len(s)-1)
        row.append(el_index)
    return row

def gen_field(x, y):
    field = []
    for i in range (0, y):
        field.append(gen_row(x))
    return field


def visual(field):
    symbol_map = {0: '🐀', 1: '💎', 2: '🎯', 3: '🤖'}
    vis = []
    for i in field:
        for j in i:
            symbol = symbol_map[j]
            vis.append(symbol)
    for i in range(0, len(vis), y):
        pole = vis[i:i + y]
        print(pole)

def check_gors(field):
    scoregors = 0
    for row in field:
        scoregors += check_line(row)
    return scoregors

def check_verts(field):
    scorevert = 0
    for j in range(y):
        vert = []
        for i in range(x):
            vert.append(field[i][j])
        scorevert += check_line(vert)
    return scorevert

def check_diagx(field):
    scorediagx = 0
    diagx = []
    for i in range(x):
        diagx.append(field[i][i])
    scorediagx += check_line(diagx)
    return scorediagx


def check_diagy(field):
    scorediagy = 0
    diagy = []
    for i in range(x):
        diagy.append(field[i][x-1-i])
    scorediagy += check_line(diagy)
    return scorediagy



def check_line(row):
    score = 0
    count = 0
    el = row[0]
    for i in row[1:len(row)]:
        if i != el:
            pass
        else:
            count += 1
    if count >= len(row) - 1:
        score += 1
    return score

field = gen_field(x, y)
score = check_gors(field) + check_verts(field) + check_diagx(field) + check_diagy(field)
if score == 1:
    print("Ты выиграл!")
if score > 1:
    print("Ты выиграл X", score, sep='', end='\n')
#check_gors(field)
#check_verts(field)
#check_diagx(field)
#check_diagy(field)
visual(field)