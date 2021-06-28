# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='newFirstname',
                                   last_name='newLastname',
                                   address='newAddress',
                                   phone='new9994443322',
                                   email='newtestemail@testdomain.com'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name='modifiedFirstname',
                      last_name='modifiedLastname')
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
