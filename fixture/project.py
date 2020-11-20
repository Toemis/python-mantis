class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_new_project(self, name):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(name)
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
            name = cells[0].find_element_by_tag_name("a").text
            project_list.append(name)
        return project_list

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "manage_proj_page.php")

