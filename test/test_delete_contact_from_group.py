import random
from model.contact import Contact
from data.groups import testdata as group_testdata
from data.contacts import testdata as contact_testdata


def test_delete_contact_from_group(app, db, check_ui):
    if not app.contact.get_contact_list_from_group():
        list(map(lambda contact: app.contact.create(contact), contact_testdata))
    if not app.group.get_group_list():
        list(map(lambda group: app.group.create(group), group_testdata))
    groups = list(filter(lambda x: x.name != "", app.group.get_group_list()))
    contacts_from_group = []
    while not contacts_from_group and groups:
        group_for_check = random.choice(groups)
        contacts_from_group = db.get_contacts_in_group(group_for_check)
        groups.remove(group_for_check)
    if not contacts_from_group:
        contact_for_delete = random.choice(app.contact.get_contact_list())
        app.contact.add_contact_to_group(contact_for_delete, group_for_check)
    else:
        contact_for_delete = random.choice(contacts_from_group)
    app.contact.delete_contact_from_group(contact_for_delete, group_for_check)
    assert contact_for_delete in db.get_contacts_not_in_group(group_for_check)
    if check_ui:
        new_contacts = db.get_contact_list()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
