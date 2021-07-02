from model.contact import Contact


def test_phones_on_home_page(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name='newFirstname',
                                   last_name='newLastname',
                                   address='newAddress',
                                   homephone='new9994443322',
                                   email1='newtestemail@testdomain.com'))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name='newFirstname',
                                   last_name='newLastname',
                                   address='newAddress',
                                   homephone='9994443322',
                                   email='newtestemail@testdomain.com'))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone




