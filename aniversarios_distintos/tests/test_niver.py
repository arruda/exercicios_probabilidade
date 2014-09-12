# -*- coding: utf-8 -*-
from __future__ import division
import unittest

import math

from niver import prob_nivers


class TestNiver(unittest.TestCase):

    def test_probabilidade_1_pessoas(self):
        r = 1
        p_esperado = 1

        p_resultado = prob_nivers(r)
        self.assertEquals(p_esperado, p_resultado)

    def test_probabilidade_365_pessoas(self):
        r = 365
        p_esperado = math.factorial(365)/pow(365, 365)

        p_resultado = prob_nivers(r)
        self.assertEquals(p_esperado, p_resultado)

    def test_probabilidade_366_pessoas(self):
        r = 366
        p_esperado = 0

        p_resultado = prob_nivers(r)
        self.assertEquals(p_esperado, p_resultado)
