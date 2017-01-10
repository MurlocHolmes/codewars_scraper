from selenium import webdriver
import os
import re
from .config import Config
import requests
from lxml import html
import bs4
import time


class CodewarsKata:
    file_extensions = Config.file_extensions

    def __init__(self, browser):
        self.browser = browser
        self.name = self.find_name()
        self.language = self.find_language()
        self.solution = self.find_solution()
        self.detail_link = self.find_detail_link()
        self.file_name = self.create_file_name()
        self.folder_name = self.create_folder_name()
        self.file_path = self.create_full_file_path()
        self.phantom = None
        self.description = None

    # Creates solution file and directory; returns true if successful
    def create_solution(self):
        if self.create_directory():
            self.create_solution_file()
            return True
        else:
            return False

    # Creates readme file for git repo
    def create_readme(self):
        session = self.go_to_kata_details()
        self.description = self.find_description(session)
        self.create_readme_file()

    def find_name(self):
        return self.browser.find_element_by_tag_name('a').text

    def find_language(self):
        return self.browser.find_element_by_tag_name('h6').text[:-1]

    def find_solution(self):
        return self.browser.find_element_by_tag_name('code').text

    def find_detail_link(self):
        return self.browser.find_element_by_tag_name('a').get_attribute("href")

    def remove_special_characters(self, string):
        return re.sub("[^0-9a-zA-Z ]+", "", string)

    def get_file_extension(self):
        return "." + self.file_extensions[self.language]

    # Takes the Kata name, replaces spaces with underscores and makes it all lowercase
    def create_file_name(self):
        file_name = self.remove_special_characters(self.name)
        file_name = file_name.replace(" ", "_")
        file_name = file_name.lower()
        return file_name

    def create_folder_name(self):
        return self.language + "/" + self.file_name + "/"

    def create_full_file_path(self):
        folder_name = self.create_folder_name()
        file_name = self.file_name + self.get_file_extension()
        return "kata_solutions/" + folder_name

    def create_directory(self):
        try:
            os.makedirs(self.file_path)
            return True
        except FileExistsError:
            print(self.file_path + " already existed, moving to next kata")
            return False

    def create_solution_file(self):
        solution_file = open(self.file_path + self.file_name, "w")
        solution_file.write(self.solution)
        solution_file.close()

    def go_to_kata_details(self):
        details = requests.get(self.detail_link)
        return details

    def find_description(self, session):
        source = bs4.BeautifulSoup(session.text, "html.parser")
        p = re.compile('(?<="description":).*(?=,"activeLanguage)')
        description = p.findall(source.get_text())[0]
        return description

    def create_readme_file(self):
        readme_file = open(self.file_path + "README.md", "w")
        readme_file.write(self.description.replace('\\n','\n'))
        readme_file.close()

