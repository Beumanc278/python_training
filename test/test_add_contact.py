# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest

testdata = [Contact(first_name=Contact.generate_random_name(10), last_name=Contact.generate_random_name(10),
                    address=Contact.generate_random_address(15), email1=Contact.generate_random_email(10),
                    email2=Contact.generate_random_email(10), email3=Contact.generate_random_email(10),
                    homephone=Contact.generate_random_phone(), workphone=Contact.generate_random_phone(), mobilephone=Contact.generate_random_phone(),
                    secondaryphone=Contact.generate_random_phone()) for i in range(5)]

@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
