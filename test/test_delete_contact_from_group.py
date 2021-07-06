import random
from model.contact import Contact

def test_delete_contact_from_group(app, db, check_ui):
    groups = app.group.get_group_list()
    contacts_from_group = []
    while not contacts_from_group:
        group_for_check = random.choice(groups)
        contacts_from_group = app.contact.get_contact_list_from_group(group_for_check)
    contact_for_delete = random.choice(contacts_from_group)
    app.contact.delete_contact_from_group(contact_for_delete, group_for_check)
    assert contact_for_delete in db.get_contacts_not_in_group(group_for_check)
    if check_ui:
        new_contacts = db.get_contact_list()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
