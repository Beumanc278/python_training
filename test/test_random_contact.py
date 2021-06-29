import random


def test_random_contact(app):
    contacts = app.contact.get_contact_list()
    index = random.randrange(len(contacts))
    contact_for_test = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_for_test.first_name == contact_from_edit_page.first_name
    assert contact_for_test.last_name == contact_from_edit_page.last_name
    assert contact_for_test.address == contact_from_edit_page.address
    assert contact_for_test.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_for_test.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
