import random

import matplotlib.pyplot as plt
import numpy as np


def creationNuageDePoint(x, y, n, scale=1):
    """
    : param x : Coordonee en x du point de ref
    : param y : Coordonee en y du point de ref
    : param n : Nombre de point a generer
    : param scale : Distance max autorise
    : return : Une double liste des coordonnees x,y
    """
    multiplicateur = [-scale, scale]
    tableauCoordonee = [[x], [y]]
    for i in range(n):
        tirage = np.random.random(2) * multiplicateur[np.random.randint(0, 1)]
        tableauCoordonee[0].append(tirage[0])
        tableauCoordonee[1].append(tirage[1])
    return tableauCoordonee


# [x,y] = creationNuageDePoint(1,1,10)
plt.plot([1, 1, 1], [2, 1, 3])
