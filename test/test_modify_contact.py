# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='newFirstname',
                                   last_name='newLastname',
                                   address='newAddress',
                                   phone='new9994443322',
                                   email='newtestemail@testdomain.com'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name='modifiedFirstname',
                      last_name='modifiedLastname')
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
