from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost:801/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client("http://localhost:801/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        test_projects = []
        try:
            soap_projects = client.service.mc_projects_get_user_accessible(username, password)
            for i in soap_projects:
                id = i.id
                name = i.name
                test_projects.append(Project(id=id, name=name))
            return test_projects
        except WebFault:
            return False


