# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='newFirstname',
                                             last_name='newLastname',
                                             address='newAddress',
                                             phone='new9994443322',
                                             email='newtestemail@testdomain.com'))
    app.contact.modify_first_contact(Contact(first_name='modifiedFirstname',
                                             last_name='modifiedLastname'))