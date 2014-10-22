#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import math


def combinacao(n, p):
    """
    Combinação de N, P à P
    """
    n_fat = math.factorial(n)
    p_fat = math.factorial(p)
    n_menos_p_fat = math.factorial(n-p)

    return n_fat / (p_fat * n_menos_p_fat)


def bernuille():
    pass


def distribuicao_binomial(n, p, X):
    """
    Binomial:
    n = Total de elementos
    p = probabilidade de sucesso
    X = variavel aleatoria
    """

    return
