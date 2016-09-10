from selenium import webdriver
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        driver = webdriver.Firefox()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        # This allows to effectively go back in the history
        driver.execute_script("window.history.go(-1)")
        driver.close()
