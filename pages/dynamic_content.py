import pytest
from pylenium.driver import Pylenium


@pytest.mark.parametrize('test_input, expected',
                         [('abtest', '/abtest'),
                          ('add_remove_elements', '/add_remove_elements'),
                          ('basic_auth', '/basic_auth'),
                          ('broken_images', '/broken_images'),
                          ('challenging_dom', '/challenging_dom'),
                          ('checkboxes', '/checkboxes'),
                          ('context_menu', '/context_menu'),
                          ('digest_auth', '/digest_auth'),
                          ('disappearing_elements', '/disappearing_elements'),
                          ('drag_and_drop', '/drag_and_drop'),
                          ('dropdown', '/dropdown'),
                          ('dynamic_content', '/dynamic_content'),
                          ('dynamic_control', '/dynamic_control'),
                          ('dynamic_loading', '/dynamic_loading'),
                          ('context_menu', '/context_menu'),
                          ('entry_ad', '/entry_ad'),
                          ('exit_intent', '/exit_intent'),
                          ('download', '/download'),
                          ('upload', '/upload'),
                          ('floating_menu', '/floating_menu'),
                          ('forgot_password', '/forgot_password'),
                          ('login', '/login'),
                          ('frames', '/frames')]
                         )
class DynamicContent:
    def __init__(self, py: Pylenium):
        self.py = py

    def test_links(self):
        return self

