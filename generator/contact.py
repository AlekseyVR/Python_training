from models.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
