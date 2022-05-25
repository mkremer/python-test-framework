herokuapp_url = 'https://the-internet.herokuapp.com/'


def test_navigate_to_herokuapp(py):
    # navigate to herokuapp
    py.visit(herokuapp_url)
    # assert that we have landed at the herokuapp
    assert py.url() == 'https://the-internet.herokuapp.com/'


def test_verify_links_exist(py):
    # navigate to herokuapp
    py.visit(herokuapp_url)
    # assert that a link exists
    py.get("a[href='/dropdown']").should().be_clickable()


def test_navigate_to_new_page(py):
    # navigate to herokuapp
    py.visit(herokuapp_url)
    # click on a link
    py.get("a[href='/dropdown']").click()
    # assert that page has changed
    assert py.url().endswith("/dropdown")


def test_verify_dynamic_content_changes(py):
    # navigate to herokuapp
    py.visit(herokuapp_url)
    # click on the dynamic content link
    py.get("a[href='/dynamic_content']").click()
    # capture original value of the element
    original = py.get("body div[class='row'] div[id='content'] div[id='content'] div:nth-child(1) div:nth-child(2)")\
        .get_property("innerHTML")
    # click to change content
    py.get("a[href='/dynamic_content?with_content=static']").click()
    # capture refreshed value of the element
    refreshed = py.get("body div[class='row'] div[id='content'] div[id='content'] div:nth-child(1) div:nth-child(2)")\
        .get_property("innerHTML")
    # assert that the original value does not match the refreshed value
    assert original != refreshed

