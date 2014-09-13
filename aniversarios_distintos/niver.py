#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import math


def prob_nivers(num_pessoas=0):
    """
    Verifica a probabilidade de `num_pessoas` escolhidas terem todas
     aniversários em dias diferentes.

    A formula do exercicio é a seguinte:
    365!/(365-r)! * (365)^r
    onde r é `num_pessoas`
    """

    num_dias_ano = 365

    # se tiver mais de 365 pessoas retorna logo 0,
    # e evita fazer fatorial de numero negativo
    if num_pessoas > num_dias_ano:
        return 0

    # 350!
    fatorial_num_dias = math.factorial(num_dias_ano)

    num_dias_menos_pessoas = num_dias_ano - num_pessoas

    # (365 - num_pessoas)!
    fatorial_num_dias_menos_pessoas = math.factorial(num_dias_menos_pessoas)

    # 350^num_pessoas
    universo = pow(num_dias_ano, num_pessoas)

    # (365 - num_pessoas)! * (365)^num_pessoas
    universo = fatorial_num_dias_menos_pessoas * universo

    probabilidade = fatorial_num_dias / universo
    return probabilidade

if __name__ == "__main__":
    print "probailidade em..."
    for r in xrange(0, 368):
        print "%d pessoas:" % r
        print "\t %s" % str(prob_nivers(r))
