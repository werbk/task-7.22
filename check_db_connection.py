import mysql.connector
from tests_contract.contact_lib import Contact
from fixture.orm import ORMFixture


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    groups = db.get_contacts_in_groups()
    for group in groups:
        print group
    print len(groups)
finally:
    pass
    #db.destroy()


'''
try:
    cursor = connection.cursor()
    cursor.execute('select id, firstname, middlename, lastname, nickname, title, company, address, home, '
                   'mobile, work, fax, email, email2, email3, homepage, address2, phone2, notes '
                   'from addressbook')
    for row in cursor:
        print (row)

        (id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax,
         email, email2, email3, homepage, address2, phone2, notes) = row

        list.append(Contact(first_name=firstname, last_name=lastname,
                    middle_name=middlename, nickname=nickname,
                    title=title, company_name=company,
                    address_name=address, work=work,
                    fax=fax, home=home,
                    mobile=mobile, email1=email,
                    email2=email2, email3=email3, homepage=homepage,
                    add_year=False, address=address2, phone=phone2,
                    notes=notes))

finally:
    cursor.close()
    print list
    '''