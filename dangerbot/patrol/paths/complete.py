def combine(a, b):
    return (a[0] + b[0], a[1] + b[1])


#
# These tuples represent the coordinate diff requrired to move in a particular direction.
# U - up (north), R - right (east), D - down (south), L - left (west)
# UR - northeast, DR - southeast, DL - southwest, UL - northwest
#
U = (-1, 0)
R = (0, 1)
D = (1, 0)
L = (0, -1)
_ = (0, 0)

UR = combine(U, R)
DR = combine(D, R)
DL = combine(D, L)
UL = combine(U, L)

#
# Each of these paths is a route to move through a suburb of Malton
# Suburbs in Malton are defined by 10x10 grids of blocks, starting from (0, 0) in the top left
#
SUBURB_PATHS = [
    [  # 0
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
    ],
    [  # 1
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
    ],
    [  # 2
        [D, R, D, R, D, R, D, R, D, R],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [R, U, R, U, R, U, R, U, R, U],
    ],
    [  # 3
        [L, D, L, D, L, D, L, D, L, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, L, U, L, U, L, U, L, U, L],
    ],
    [  # 4
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
    ],
    [  # 5
        [R, R, R, R, R, R, R, R, R, R],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
    ],
    [  # 6
        [R, R, R, R, R, R, R, R, R, D],
        [UL, D, L, D, L, D, L, D, L, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, L, U, L, U, L, U, L, U, L],
    ],
    [  # 7
        [R, D, R, D, R, D, R, D, R, D],
        [U, R, U, R, U, R, U, R, U, UR],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
    ],
    [  # 8
        [U, D, L, D, L, D, L, D, L, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, L, U, L, U, L, U, L, U, L],
    ],
    [  # 9
        [D, R, D, R, D, R, D, R, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [R, U, R, U, R, U, R, U, R, U],
    ],
    [  # 10
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, D],
        [D, L, L, L, L, L, L, L, L, D],
        [R, R, R, R, R, R, R, D, U, L],
        [D, L, L, L, L, L, L, L, _, _],
        [R, R, R, R, R, R, R, D, _, _],
        [D, L, L, L, L, L, L, L, _, _],
    ],
    [  # 11
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [U, L, L, L, L, L, L, L, L, L],
        [R, R, R, R, R, R, R, R, R, U],
        [_, UL, L, L, L, L, L, L, L, L],
        [_, R, R, R, R, R, R, R, R, U],
        [_, U, L, L, L, L, L, L, L, L],
    ],
    [  # 12
        [D, R, D, R, D, R, D, R, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, D, U, D, U, D, U],
        [D, U, D, U, R, U, DR, U, D, U],
        [R, U, R, U, _, _, _, U, R, U],
    ],
    [  # 13
        [L, D, L, L, _, _, _, D, L, D],
        [U, D, R, U, _, _, _, D, U, D],
        [U, D, U, D, L, D, L, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, D, U, D, U, D, U, D, U, D],
        [U, L, U, L, U, L, U, L, U, L],
    ],
]

MALTON = [
    [7, 0, 5, 0, 5, 0, 5, 0, 5, 0],
    [1, 0, 4, 0, 4, 0, 4, 0, 4, 0],
    [1, 0, 4, 0, 4, 0, 4, 0, 4, 0],
    [1, 0, 4, 0, 4, 0, 4, 0, 4, 0],
    [1, 0, 4, 0, 4, 0, 4, 10, 11, 0],
    [1, 0, 4, 0, 4, 0, 4, 0, 4, 0],
    [1, 0, 4, 0, 4, 0, 4, 0, 4, 0],
    [1, 0, 4, 0, 4, 0, 4, 0, 4, 0],
    [1, 2, 9, 2, 9, 2, 9, 2, 12, 0],
    [8, 3, 3, 3, 3, 3, 3, 3, 13, 6]
]
