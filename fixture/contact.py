class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_create_contact_page(self):
        wd = self.app.wd
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

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//a[contains(@href, "edit")]').click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name('lastname').send_keys(contact.last_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name('mobile').send_keys(contact.phone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name('email').send_keys(contact.email)
        wd.find_element_by_xpath('//input[@type="submit"]').click()
        self.app.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//input[@type="button" and @value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
