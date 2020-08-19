from sys import maxsize


class Group:
    def __init__(self, name_group=None, logo_group=None, footer_group=None, id=None):
        self.name_group = name_group
        self.logo_group = logo_group
        self.footer_group = footer_group
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name_group, self.footer_group, self.logo_group)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name_group == other.name_group

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
