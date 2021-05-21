
class ContactHelper:
    def __init__(self, app):
        self.app = app
   
    def open_create_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    #для заполнения полей
    def fill_form_contact(self, contact):
        driver = self.app.driver
        # добавляем строковые поля
        #driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.phone_home)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.phone_work)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.homepage)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address2)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.phone2)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)
        # добавляем даты
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bday").send_keys(contact.bday)
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("bmonth").send_keys(contact.bmonth)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        #добавлякм вторые даты
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("aday").send_keys(contact.aday)
        driver.find_element_by_name("amonth").click()
        driver.find_element_by_name("amonth").send_keys(contact.amonth)
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(contact.ayear)

    def create(self, contact):
        driver = self.app.driver
        self.open_create_contact_page()
        self.fill_form_contact(contact)
        self.confirm_add_contact()
        self.return_to_home_page()

    def confirm_add_contact(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def delete_first(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('input[name="selected[]"]').click()
        driver.find_element_by_css_selector('input[value="Delete"]').click()
        driver.switch_to_alert().accept()

    def edit_first(self, contact):
        driver = self.app.driver
        driver.find_element_by_css_selector('img[title="Edit"]').click()
        self.fill_form_contact(contact)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_css_selector('input[name="selected[]"]'))



