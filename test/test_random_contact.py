import random

from model.contact import Contact


def test_random_contact(app, db, check_ui):
    contacts = db.get_contact_list_like_on_home_page()
    contact_for_test = random.choice(contacts)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_id(contact_for_test.id)
    assert contact_for_test.first_name == contact_from_edit_page.first_name
    assert contact_for_test.last_name == contact_from_edit_page.last_name
    assert contact_for_test.address == contact_from_edit_page.address
    assert contact_for_test.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_for_test.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    if check_ui:
        assert sorted(contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)