from model.contact import Contact


testdata = [Contact(first_name=Contact.generate_random_name(10), last_name=Contact.generate_random_name(10),
                    address=Contact.generate_random_address(15), email1=Contact.generate_random_email(10),
                    email2=Contact.generate_random_email(10), email3=Contact.generate_random_email(10),
                    homephone=Contact.generate_random_phone(), workphone=Contact.generate_random_phone(), mobilephone=Contact.generate_random_phone(),
                    secondaryphone=Contact.generate_random_phone())]