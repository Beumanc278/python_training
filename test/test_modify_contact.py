# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(first_name='modifiedFirstname',
                                             last_name='modifiedLastname',
                                             address='modifiedAddress',
                                             phone='mod9994443322',
                                             email='modtestemail@testdomain.com'))