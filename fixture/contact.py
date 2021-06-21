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
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
