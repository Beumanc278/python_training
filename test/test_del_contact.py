from random import randrange

from model.contact import Contact


def test_delete_some_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name='newFirstname',
                                   last_name='newLastname',
                                   address='newAddress',
                                   homephone='new9994443322',
                                   email1='newtestemail@testdomain.com'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.pop(index)
    assert old_contacts == new_contacts
