from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .codewars_kata import CodewarsKata
from .config import Config
import threading


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
        username_input.send_keys(Config.git_username)
        password_input.send_keys(Config.git_password + Keys.RETURN)

    def verify_loggedin_to_codewars(self):
        browser = self.browser
        try:
            browser.find_element_by_name('authorize').click()
            return True
        except Exception:
            return True

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
        katas = self.get_katas_from_solutions(solutions)
        self.thread_katas(katas)

    def get_katas_from_solutions(self, solutions):
        katas = []
        for solution in solutions:
            kata = CodewarsKata(solution)
            katas.append(kata)
        return katas

    def thread_katas(self, katas):
        threads = []
        for kata in katas:
            t = threading.Thread(target=self.thread_create_solution, args=(kata,))
            threads.append(t)
            t.start()

    def thread_create_solution(self, kata):
        was_created = kata.create_solution()
        if was_created:
            print(kata.name + " was created")
            kata.create_readme()
        else:
            print(kata.name + " not Created")

