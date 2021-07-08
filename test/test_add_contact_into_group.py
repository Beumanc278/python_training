import random

import allure

from data.contacts import testdata as contact_testdata
from data.groups import testdata as group_testdata
from model.contact import Contact

def test_add_contact_into_group(app, db, check_ui):
    with allure.step("Given a non-empty group list and a non-empty contact list"):
        if not app.contact.get_contact_list_from_group():
            list(map(lambda contact: app.contact.create(contact), contact_testdata))
        if not app.group.get_group_list():
            list(map(lambda group: app.group.create(group), group_testdata))
        contacts = app.contact.get_contact_list_from_group()
        groups = app.group.get_group_list()
    with allure.step("Given a random contact and a random group"):
        contact_for_add = random.choice(contacts)
        group_for_add = random.choice(groups)
    with allure.step(f"When I add the randomly chosen contact {contact_for_add} to the randomly chosen group"):
        app.contact.add_contact_to_group(contact_for_add, group_for_add)
    with allure.step("Then the randomly chosen contact is in the chosen group"):
        assert contact_for_add in db.get_contacts_in_group(group_for_add)
        if check_ui:
            new_contacts = db.get_contact_list()
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
