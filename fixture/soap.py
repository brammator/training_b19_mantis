# -*- coding: utf-8 -*-
from suds.client import Client

from model.project import Project


class SoapFixture:
    def __init__(self, wsdl, defaultconfig=None):
        self.client = Client(wsdl)
        self.service = self.client.service
        # self.methods = set(self.client.wsdl.services[0].ports[0].methods.keys())
        if defaultconfig is not None:
            self.defaultconfig = defaultconfig

    def get_project_list(self, username=None, password=None):
        if username is None:
            username = self.defaultconfig["webadmin"]["username"]
        if password is None:
            password = self.defaultconfig["webadmin"]["password"]
        projects = [Project(id=str(p.id), name=p.name, view_state=p.view_state.name, status=p.status.name,
                            description=p.description) for p in
                    self.service.mc_projects_get_user_accessible(username, password)]
        return projects
