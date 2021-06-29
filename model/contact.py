from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, address=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None,
                 homephone=None, workphone=None, mobilephone=None, secondaryphone=None,
                 email1=None, email2=None, email3=None,
                 id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.id = id

    def __repr__(self):
        return f"{self.id}: {self.first_name}, {self.last_name}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
                self.first_name == other.first_name and \
                self.last_name == other.last_name

    def id_or_max(self, gr):
        return int(gr.id) if gr.id else maxsize
