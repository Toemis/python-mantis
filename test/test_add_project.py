from model.project import Project


def test_add_project(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    project_name = app.project.create_project_name("name", 20)
    project = Project(name=project_name)
    old_project_list = app.soap.get_projects_list(username, password)
    app.project.add_new_project(project)
    new_project_list = app.soap.get_projects_list(username, password)
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)






