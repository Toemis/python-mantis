from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, href=None):
        self.id = id
        self.name = name
        self.href = href

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.name, self.href)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.name is None or other.name is None or self.name == other.name)

    #    def __lt__(self, other):
    #        return self.id < other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
