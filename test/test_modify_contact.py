# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    if not db.get_contact_list():
        app.contact.create(Contact(first_name='newFirstname',
                                   last_name='newLastname',
                                   address='newAddress',
                                   homephone='new9994443322',
                                   email1='newtestemail@testdomain.com'))
    old_contacts = db.get_contact_list()
    new_contact = Contact(first_name='modifiedFirstname',
                      last_name='modifiedLastname')
    contact = random.choice(old_contacts)
    new_contact.id = contact.id
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact)] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
