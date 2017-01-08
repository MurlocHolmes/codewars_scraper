from selenium import webdriver
import os
import re
import config


class Codewars_kata:
    file_extensions = config.file_extensions

    def __init__(self, browser):
        self.browser = browser
        self.name = self.find_name()
        self.language = self.find_language()
        self.solution = self.find_solution()
        self.detail_link = self.find_detail_link()
        self.file_name = self.create_file_name()
        self.folder_name = self.create_folder_name()
        self.file_path = self.create_full_file_path()
        self.description = None

    def create_solution(self):
        if self.create_directory():
            self.create_solution_file()
            return True
        else:
            return False

    def create_readme(self):
        self.open_new_tab()
        self.go_to_kata_details()
        self.description = self.find_description()
        self.create_readme_file()
        self.close_tab()

    def find_name(self):
        return self.browser.find_element_by_tag_name('a').text

    def find_language(self):
        return self.browser.find_element_by_tag_name('h6').text[:-1]

    def find_solution(self):
        return self.browser.find_element_by_tag_name('code').text

    def find_detail_link(self):
        return self.browser.find_element_by_tag_name('a')

    def find_description(self):
        return self.browser.find_element_by_id("description")

    def remove_special_characters(self, string):
        return re.sub("[^0-9a-zA-Z ]+", "", string)

    def get_file_extension(self):
        return "." + self.file_extensions[self.language]

    def create_file_name(self):
        name = self.remove_special_characters(self.name)
        name_array = name.split()
        file_name = name_array.pop(0).lower()
        for string in name_array:
            file_name += string.capitalize()
        return file_name

    def create_folder_name(self):
        return self.language + "/" + self.file_name + "/"

    def create_full_file_path(self):
        folder_name = self.create_folder_name()
        file_name = self.file_name + self.get_file_extension()
        return folder_name + file_name

    def create_directory(self):
        try:
            os.makedirs(self.folder_name)
            return True
        except FileExistsError:
            print("Folder existed, moving forward")
            return False

    def create_solution_file(self):
        solution_file = open(self.file_path, "w")
        solution_file.write(self.solution)
        solution_file.close()

    def create_readme_file(self):
        readme_file = open(self.folder_name + "README.md", "w")
        readme_file.write(self.description.text)
        readme_file.close()

    def open_new_tab(self):
        self.browser = webdriver.PhantomJS()

    def go_to_kata_details(self):
        self.browser.get(self.detail_link.get_attribute("href"))

    def close_tab(self):
        self.browser.close()
