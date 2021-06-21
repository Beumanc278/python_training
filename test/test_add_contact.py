# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(first_name='testFirstname',
                               last_name='testLastname',
                               address='testAddress',
                               phone='9994443322',
                               email='testemail@testdomain.com'))
    app.session.logout()
