from sys import maxsize


class Project:

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s: %s" % (self.id, self.name)

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
