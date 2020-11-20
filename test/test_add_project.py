import random
import string


def test_add_project(app):
    app.session.login("administrator", "root")
    project_name = create_project_name("name", 20)
    old_project_list = app.project.get_project_list()
    app.project.add_new_project(project_name)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project_name)
    assert sorted(old_project_list) == sorted(new_project_list)


def create_project_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    s = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    # clear_string = ' '.join([t for t in s.split(' ') if t])  # delete all unnecessary additional spaces
    return s




