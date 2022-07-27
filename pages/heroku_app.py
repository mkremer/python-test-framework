from pylenium.driver import Pylenium


class Herokuapp:
    def __init__(self, py: Pylenium):
        self.py = py
        self.herokuapp_url = 'https://the-internet.herokuapp.com/'

    def visit_the_internet(self):
        """
        Visits the-internet Heroku webpage
        """
        self.py.visit(self.herokuapp_url)
        self.py.url() == 'https://the-internet.herokuapp.com/'

    def click_on_link(self, link):
        """
        Takes a string for a link and clicks
        """
        self.py.get(f"a[href='/{link}']").click()

