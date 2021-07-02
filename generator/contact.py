import jsonpickle
from model.contact import Contact
import os.path
import getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "f", ["file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

f = 'data/contacts.json'

for o, a in opts:
    if o == "-f":
        f = a

testdata = [Contact(first_name=Contact.generate_random_name(10), last_name=Contact.generate_random_name(10),
                    address=Contact.generate_random_address(15), email1=Contact.generate_random_email(10),
                    email2=Contact.generate_random_email(10), email3=Contact.generate_random_email(10),
                    homephone=Contact.generate_random_phone(), workphone=Contact.generate_random_phone(), mobilephone=Contact.generate_random_phone(),
                    secondaryphone=Contact.generate_random_phone()) for i in range(5)]

file = os.path.join(os.path.dirname(__file__), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))