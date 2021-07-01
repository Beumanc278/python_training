from model.contact import Contact
import re

class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def open_create_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('edit.php') and wd.find_element_by_name("firstname")):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_create_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath('//img[@alt="Edit"]')[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field("firstname", contact.first_name)
        self.change_field("lastname", contact.last_name)
        self.change_field("address", contact.address)
        self.change_field("home", contact.homephone)
        self.change_field("mobile", contact.mobilephone)
        self.change_field("work", contact.workphone)
        self.change_field("phone2", contact.secondaryphone)
        self.change_field("email", contact.email1)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath('//input[@type="button" and @value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            table_rows = wd.find_elements_by_name("entry")
            for row in table_rows:
                columns = row.find_elements_by_tag_name("td")
                all_phones = columns[5].text.splitlines() if columns[5].text else []
                all_emails = columns[4].text
                self.contact_cache.append(Contact(first_name=columns[2].text,
                                                  last_name=columns[1].text,
                                                  address=columns[3].text,
                                                  id=row.find_element_by_name("selected[]").get_attribute('value'),
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
            return self.contact_cache
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(first_name=firstname, last_name=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email1=email1, email2=email2, email3=email3,
                       address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1) if re.search('H: (.*)', text) else ''
        workphone = re.search('W: (.*)', text).group(1) if re.search('W: (.*)', text) else ''
        mobilephone = re.search("M: (.*)", text).group(1) if re.search('M: (.*)', text) else ''
        secondaryphone = re.search("P: (.*)", text).group(1) if re.search('P: (.*)', text) else ''
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def merge_phones_like_on_home_page(self, contact):
        return list(filter(lambda x: x != '', map(lambda x: self.app.contact.clear_phonenumber(x),
                                                  filter(lambda x: x is not None,
                                                         [contact.homephone, contact.mobilephone,
                                                          contact.workphone,
                                                          contact.secondaryphone]))))

    def merge_emails_like_on_home_page(self, contact):
        return '\n'.join(filter(lambda x: x != '', filter(lambda x: x is not None,
                                                          [contact.email1,
                                                           contact.email2,
                                                           contact.email3])))

    @staticmethod
    def clear_phonenumber(s):
        phonenumber = s.replace('00', '0')
        return re.sub("[() -]", '', phonenumber)