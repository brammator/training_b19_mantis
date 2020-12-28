# -*- coding: utf-8 -*-
import random
import pytest

from model.project import Project


def test_project_add(app, db, logged, data_project_random):
    project = data_project_random
    old_list = db.get_project_list()
    app.project.add(project)
    new_list = db.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

# @pytest.mark.parametrize("x", range(5))
def test_project_del(app, db, logged, x):
    if len(db.get_project_list()) == 0:
        app.project.add(Project.random())
    old_list = db.get_project_list()
    project = random.choice(old_list)
    app.project.del_byid(project.id)
    new_list = db.get_project_list()
    old_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

