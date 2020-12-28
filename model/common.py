# -*- coding: utf-8 -*-
import random

from fixture.common import random_string


class Entity:
    CHOICE_FIELDS = dict()
    TEXT_FIELDS = ()

    @classmethod
    def random(cls, i=0):
        kw = {k: random_string(f"{k}_{i}", 20) for k in cls.TEXT_FIELDS}
        kw.update({k: random.choice(v) for k, v in cls.CHOICE_FIELDS.items()})
        p = cls(**kw)
        return p

    def __repr__(self):
        return self.__class__.__name__ + "(" + ";".join(f"{k}:{v}" for k, v in self.__dict__.items()) + ")"
