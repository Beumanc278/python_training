import jsonpickle
from model.group import Group
import os.path
import getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == '-f':
        f = a

testdata = [Group(name=name, header=header, footer=footer)
                for name in ['', Group.generate_random_group_field('name', 10)]
                for header in ['', Group.generate_random_group_field('header', 20)]
                for footer in ['', Group.generate_random_group_field('footer', 20)]]

file = os.path.join(os.path.dirname(__file__), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))