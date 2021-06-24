from model.contact import Contact


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
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name('lastname').send_keys(contact.last_name)
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name('mobile').send_keys(contact.phone)
        wd.find_element_by_name('email').send_keys(contact.email)
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
        self.change_field("mobile", contact.phone)
        self.change_field("email", contact.email)

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
                self.contact_cache.append(Contact(first_name=columns[2].text,
                                                  last_name=columns[1].text,
                                                  id=row.find_element_by_name("selected[]").get_attribute('value')))
            return self.contact_cache
        return list(self.contact_cache)
