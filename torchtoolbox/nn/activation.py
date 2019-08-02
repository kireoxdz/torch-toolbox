# -*- coding: utf-8 -*-
# @Author  : DevinYang(pistonyang@gmail.com)
__all__ = ['Swish']

from .functional import swish
from torch import nn


class Swish(nn.Module):
    """Switch activation from 'SEARCHING FOR ACTIVATION FUNCTIONS'
        https://arxiv.org/pdf/1710.05941.pdf
    """

    def __init__(self, beta=1.0):
        super(Swish, self).__init__()
        self.beta = beta

    def forward(self, x):
        return swish(x, self.beta)
