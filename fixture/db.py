import re

import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name,
                                          user=user, password=password,
                                          autocommit=True)

    def get_group_list(self):
        output_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                output_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return output_list

    def get_contact_list(self):
        output_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                output_list.append(Contact(first_name=firstname, last_name=lastname, id=str(id),
                                    address=address, homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2,
                                    email1=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return output_list

    def get_contact_list_like_on_home_page(self):
        input_list = self.get_contact_list()
        output_list = []
        for contact in input_list:
            all_phones_from_home_page = list(filter(lambda x: x is not None, map(lambda x: self.empty_row_to_none(x),
                                                                                 map(lambda x: self.clear_phonenumber(x), [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
            all_emails_from_home_page = '\n'.join(list(filter(lambda x: x is not None, map(lambda x: self.empty_row_to_none(x), [contact.email1, contact.email2, contact.email3]))))
            (contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone) = (None, None, None, None)
            (contact.email1, contact.email2, contact.email3) = (None, None, None)
            contact.all_emails_from_home_page = all_emails_from_home_page
            contact.all_phones_from_home_page = all_phones_from_home_page
            output_list.append(contact)
        return output_list

    def empty_row_to_none(self, s):
        return None if not s else s

    @staticmethod
    def clear_phonenumber(s):
        phonenumber = s.replace('00', '0')
        return re.sub("[() -]", '', phonenumber)

    def destroy(self):
        self.connection.close()