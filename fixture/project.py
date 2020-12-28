# -*- coding: utf-8 -*-
from fixture.common import WebDriverHelper


class ProjectHelper(WebDriverHelper):
    def add(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_all(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def del_byid(self,  project_id):
        wd = self.app.wd
        self.open_projects_page()
        self.open_byid(project_id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_name("_confirmed")
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def open_byid(self, project_id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"a[href='manage_proj_edit_page.php?project_id={project_id}']").click()

    def fill_all(self, project):
        self.fill_field("name", project.name)
        self.fill_field("status", project.status)
        self.fill_field("view_state", project.view_state)
        self.fill_field("description", project.description)

    def open_projects_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/mantisbt-1.2.20/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
