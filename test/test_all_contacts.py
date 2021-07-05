from model.contact import Contact


def test_all_contacts(app, db, check_ui):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list_like_on_home_page()
    for contact_for_test in contacts_from_home_page:
        db_contact = list(filter(lambda x: x.id == contact_for_test.id, contacts_from_db))[0]
        assert contact_for_test.first_name == db_contact.first_name
        assert contact_for_test.last_name == db_contact.last_name
        assert contact_for_test.address == db_contact.address
        assert contact_for_test.all_phones_from_home_page == db_contact.all_phones_from_home_page
        assert contact_for_test.all_emails_from_home_page == db_contact.all_emails_from_home_page
    if check_ui:
        assert sorted(contacts_from_db, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
