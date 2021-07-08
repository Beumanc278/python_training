import random

import allure

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        if not db.get_contact_list():
            app.contact.create(Contact(first_name='newFirstname',
                                       last_name='newLastname',
                                       address='newAddress',
                                       homephone='new9994443322',
                                       email1='newtestemail@testdomain.com'))
        old_contacts = db.get_contact_list()
    with allure.step("Given a randomly chosen contact"):
        contact = random.choice(old_contacts)
    with allure.step(f"When I delete the chosen contact {contact} from the contact list"):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then the new contact list is equal to the old list without deleted contact"):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
