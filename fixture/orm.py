# -*- coding: utf-8 -*-
from pony.orm import Database, sql_debug, PrimaryKey, Optional, db_session, select

from model.project import Project


class ORMFixture:
    db = Database()

    class ORMProject(db.Entity):
        _table_ = 'mantis_project_table'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='name')
        status = Optional(int, column='status')
        view_state = Optional(int, column='view_state')
        description = Optional(str, column='description')

    def convert_projects_to_model(self, projects):
        l = list(map(lambda p: Project(**{k: str(getattr(p, k)) for k in p._adict_}), projects))
        return l

    @db_session
    def get_project_list(self):
        l = self.convert_projects_to_model(select(p for p in ORMFixture.ORMProject))
        return l

    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host=host, database=database, user=user, password=password, autocommit=True)
        self.db.generate_mapping()
        sql_debug(True)


