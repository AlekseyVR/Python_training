from models.contact import Contact
from models.group import Group
import random


def test_remove_contact_from_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(Contact(first_name_contact="RemoveContact"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    available_groups = orm.get_groups_containing_contact(contact)
    if not available_groups:
        groups = orm.get_group_list()
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact.id, group.id, group.name_group)
    else:
        group = random.choice(available_groups)
    app.contact.delete_contact_from_group(group.id, contact.id)
    print("\n", "debug_helper:: ", "group.id: ", group.id, "\n", "contact.id: ", contact.id)
    contact_not_in_group = orm.get_contacts_in_group(group)
    print("\n", "debug_helper:: ", "contact: ", contact, "\n", "contact_not_in_group: ", contact_not_in_group)
    assert contact not in contact_not_in_group
