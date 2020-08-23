from models.contact import Contact
import random
import string

# для исп константы в тесте изменить импорт на: from data.add_group import constant as testdata
constant = [
    Contact(first_name_contact="name", middle_name_contact="m_name",
            last_name_contact="l_name", nickname_contact="nick",
            title_contact="title", company_contact="company",
            address_contact="address_c", home_contact="address_h",
            mobile_contact="address_m",
            work_contact="work", fax_contact="fax",
            e_mail_contact="email", e_mail_2_contact="email2",
            e_mail_3_contact="email3",
            homepage_contact="HC", birthday="2", birthdmonth="January",
            bYear="1994", aDay="20", aMonth="December", aYear="1995",
            secondary_address="SCR_a",
            secondary_home="SCR_h", notes_contact="SCR_c")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name_contact=random_string("name", 10), middle_name_contact=random_string("m_name", 11),
                    last_name_contact=random_string("l_name", 12), nickname_contact=random_string("nick", 13),
                    title_contact=random_string("title", 14), company_contact=random_string("company", 15),
                    address_contact=random_string("address_c", 16), home_contact=random_string("address_h", 17),
                    mobile_contact=random_string("address_m", 18),
                    work_contact=random_string("work", 19), fax_contact=random_string("fax", 20),
                    e_mail_contact=random_string("email", 21), e_mail_2_contact=random_string("email2", 22),
                    e_mail_3_contact=random_string("email3", 23),
                    homepage_contact=random_string("HC", 24), birthday="2", birthdmonth="January",
                    bYear="1994", aDay="20", aMonth="December", aYear="1995",
                    secondary_address=random_string("SCR_a", 25),
                    secondary_home=random_string("SCR_h", 26), notes_contact=random_string("SCR_c", 27))
            for i in range(2)
            ]
