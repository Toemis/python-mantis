import random
from model.project import Project


def test_del_project(app):
    if not app.project.get_project_list():
        project_name = app.project.create_project_name("name", 20)
        app.project.add_new_project(Project(name=project_name))
    old_project_list = app.project.get_project_list()
    project = random.choice(old_project_list)
    app.project.delete_project(project)
    new_project_list = app.project.get_project_list()
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
