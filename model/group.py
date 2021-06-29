import random
import string
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self, gr):
        return int(gr.id) if gr.id else maxsize

    @staticmethod
    def generate_random_group_field(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
        return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])