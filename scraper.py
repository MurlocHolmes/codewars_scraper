from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from codewars_kata import Codewars_kata
import config


class Scraper:

    def __init__(self):
        self.browser = self.setup_browser()

    def setup_browser(self):
        browser = webdriver.Firefox()
        browser.get('https://www.google.com')
        return browser

    def end_scraper(self):
        self.browser.close()

    def login_to_codewars(self):
        browser = self.browser
        browser.get('https://www.codewars.com/users/preauth/github/signin')
        username_input = browser.find_element_by_id('login_field')
        password_input = browser.find_element_by_id('password')
        username_input.send_keys(config.git_username)
        password_input.send_keys(config.git_password + Keys.RETURN)

    def verify_loggedin_to_codewars(self):
        browser = self.browser
        return browser.find_element_by_class_name('personal-trainer').click()

    def go_to_codewars_solutions(self):
        browser = self.browser
        browser.get('https://www.codewars.com/users/MurlocHolmes/completed_solutions')

    def get_codewars_kata_solutions(self):
        browser = self.browser
        solutions = browser.find_elements_by_class_name('solutions')
        return solutions

    def scrape_codewars_solutions(self):
        self.login_to_codewars()
        self.verify_loggedin_to_codewars()
        self.go_to_codewars_solutions()
        solutions = self.get_codewars_kata_solutions()
        for solution in solutions:
            k = Codewars_kata(solution)
            was_created = k.create_solution()
            if was_created:
                print("Was created")
                k.create_readme()
