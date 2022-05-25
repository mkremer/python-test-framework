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
