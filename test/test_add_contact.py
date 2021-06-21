# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(first_name='testFirstname',
                               last_name='testLastname',
                               address='testAddress',
                               phone='9994443322',
                               email='testemail@testdomain.com'))
    app.session.logout()