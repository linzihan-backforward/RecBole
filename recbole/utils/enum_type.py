# -*- coding: utf-8 -*-
# @Time   : 2020/8/9
# @Author : Yupeng Hou
# @Email  : houyupeng@ruc.edu.cn

"""
recbole.utils.enum_type
#######################
"""

from enum import Enum


class ModelType(Enum):
    GENERAL = 1
    SEQUENTIAL = 2
    CONTEXT = 3
    KNOWLEDGE = 4
    SOCIAL = 5
    MEMBASE = 6


class DataLoaderType(Enum):
    ORIGIN = 1
    FULL = 2
    NEGSAMPLE = 3


class KGDataLoaderState(Enum):
    RSKG = 1
    RS = 2
    KG = 3


class EvaluatorType(Enum):
    RANKING = 1
    INDIVIDUAL = 2


class InputType(Enum):
    POINTWISE = 1
    PAIRWISE = 2
    LISTWISE = 3


class FeatureType(Enum):
    TOKEN = 'token'
    FLOAT = 'float'
    TOKEN_SEQ = 'token_seq'
    FLOAT_SEQ = 'float_seq'


class FeatureSource(Enum):
    INTERACTION = 'inter'
    USER = 'user'
    ITEM = 'item'
    USER_ID = 'user_id'
    ITEM_ID = 'item_id'
    KG = 'kg'
    NET = 'net'