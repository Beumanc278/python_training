import allure

from model.contact import Contact


def test_phones_on_home_page(app):
    with allure.step("Given a non-empty contact list"):
        if not app.contact.count():
            app.contact.create(Contact(first_name='newFirstname',
                                       last_name='newLastname',
                                       address='newAddress',
                                       homephone='new9994443322',
                                       email1='newtestemail@testdomain.com'))
    with allure.step("Given a first contact from home page"):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with allure.step("When I compare the contact from edit page with the contact from the home page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    with allure.step("Then the contact from the edit page is equal to the contact from the edit page"):
        assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    with allure.step("Given a non-empty contact list"):
        if not app.contact.count():
            app.contact.create(Contact(first_name='newFirstname',
                                       last_name='newLastname',
                                       address='newAddress',
                                       homephone='9994443322',
                                       email='newtestemail@testdomain.com'))
    with allure.step("Given a first contact from view page"):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
    with allure.step("When I compare the contact from view page with the contact from the home page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    with allure.step("Then the contact from the edit page is equal to the contact from the edit page"):
        assert contact_from_view_page.homephone == contact_from_edit_page.homephone
        assert contact_from_view_page.workphone == contact_from_edit_page.workphone
        assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
        assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone




