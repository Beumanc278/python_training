import random
from data.contacts import testdata as contact_testdata
from data.groups import testdata as group_testdata
from model.contact import Contact

def test_add_contact_into_group(app, db, check_ui):
    if not app.contact.get_contact_list_from_group():
        list(map(lambda contact: app.contact.create(contact), contact_testdata))
    if not app.group.get_group_list():
        list(map(lambda group: app.group.create(group), group_testdata))
    contacts = app.contact.get_contact_list_from_group()
    groups = app.group.get_group_list()
    contact_for_add = random.choice(contacts)
    group_for_add = random.choice(groups)
    app.contact.add_contact_to_group(contact_for_add, group_for_add)
    assert contact_for_add in db.get_contacts_in_group(group_for_add)
    if check_ui:
        new_contacts = db.get_contact_list()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
