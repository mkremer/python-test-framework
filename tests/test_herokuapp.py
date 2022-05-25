herokuapp_url = 'https://the-internet.herokuapp.com/'


def test_navigate_to_herokuapp(py):
    """
    Navigates to the Herokuapp webpage
    """
    py.visit(herokuapp_url)
    assert py.url() == 'https://the-internet.herokuapp.com/'


def test_verify_links_exist(py):
    """
    Searches for the existence of a clickable link in the Herokuapp webpage
    """
    py.visit(herokuapp_url)
    py.get("a[href='/dropdown']").should().be_clickable()


def test_navigate_to_new_page(py):
    """
    Clicks on a link in the Herokuapp webpage and verifies that the page changes
    """
    py.visit(herokuapp_url)
    py.get("a[href='/dropdown']").click()
    assert py.url().endswith("/dropdown")


def test_verify_dynamic_content_changes(py):
    """
    Navigates to the Dynamic Content page in the Herokuapp webpage and verifies that
    content changes on refresh
    """
    py.visit(herokuapp_url)
    py.get("a[href='/dynamic_content']").click()
    original = py.get("body div[class='row'] div[id='content'] div[id='content'] div:nth-child(1) div:nth-child(2)")\
        .get_property("innerHTML")
    py.get("a[href='/dynamic_content?with_content=static']").click()
    refreshed = py.get("body div[class='row'] div[id='content'] div[id='content'] div:nth-child(1) div:nth-child(2)")\
        .get_property("innerHTML")
    assert original != refreshed

