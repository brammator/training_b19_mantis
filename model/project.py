# -*- coding: utf-8 -*-
from sys import maxsize

from model.common import Entity


class Project(Entity):
    CHOICE_FIELDS = dict(
        status=("development", "release", "stable", "obsolete"),
        view_state=("public", "private")
    )
    TEXT_FIELDS = ("name", "description")

    def __init__(self, id=None, name=None, status=None, view_state=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.view_state = view_state
        self.description = description

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.as_empties() == other.as_empties()

    def id_or_max(self):
        if self.id is None:
            return maxsize
        else:
            return int(self.id)

    def as_empties(self):
        return tuple("" if getattr(self, i) is None else getattr(self, i) for i in ("name", "description"))
