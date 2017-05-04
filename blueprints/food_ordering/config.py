# -*- coding: utf-8 -*-
"""This module contains the Food Ordering Blueprint Application"""


PARSER_CONFIG = {
    'dish': [{'type': 'option', 'max_instances': None}, {'type': 'quantity', 'right': False}],
    'option': [{'type': 'quantity', 'right': False}],
    'restaurant': [],
    'cuisine': [],
    'category': []
}

CLASSIFIER_CONFIGS = {
}