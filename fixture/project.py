import random
import string
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_new_project(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    def get_project_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_manage_projects_page()
        project_list = []
        table = wd.find_element_by_xpath("//table[3]")
        rows = table.find_elements_by_tag_name("tr")
        for element in rows[2:]:  # start with 3d element
            cells = element.find_elements_by_tag_name("td")
            href = cells[0].find_element_by_tag_name("a").get_attribute('href')
            name = cells[0].find_element_by_tag_name("a").text
            id = href.split("=")[1]
            project_list.append(Project(id=id, name=name))
        return project_list

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "manage_proj_page.php")

    def create_project_name(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        s = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
        # clear_string = ' '.join([t for t in s.split(' ') if t])  # delete all unnecessary additional spaces
        return s

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_page(project)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.implicitly_wait(2)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()


    def open_project_page(self, project):
        wd = self.app.wd
        wd.get(self.app.base_url + "manage_proj_edit_page.php?project_id=%s" % project.id)




