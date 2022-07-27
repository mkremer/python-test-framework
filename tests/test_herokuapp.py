

def test_navigate_to_herokuapp(visit_the_internet, py):
    """
    Navigates to the Herokuapp webpage
    """
    assert py.url() == 'https://the-internet.herokuapp.com/'


def test_verify_links_exist(visit_the_internet, herokuapp, py):
    """
    Searches for the existence of clickable links in the Herokuapp webpage
    """
    links = py.get("ul").children()
    for link in links:
        assert link.should().be_clickable()


def test_navigate_to_new_pages(visit_the_internet, herokuapp, py, link_list, test_input, expected):
    """
    Clicks on links in the Herokuapp webpage and verifies that the pages change
    """
    herokuapp.click_on_link(test_input)
    assert py.url().endswith(expected)


dynamic_content_paragraph = "body div[class='row'] div[id='content'] div[id='content'] \
                            div:nth-child(1) div:nth-child(2)"


def test_verify_dynamic_content_changes(visit_the_internet, herokuapp, py):
    """
    Navigates to the Dynamic Content page in the Herokuapp webpage and verifies that
    content changes on refresh
    """
    herokuapp.click_on_link('dynamic_content')
    original = py.get(dynamic_content_paragraph).get_property("innerHTML").strip()
    py.reload()
    refreshed = py.get(dynamic_content_paragraph).get_property("innerHTML").strip()
    assert original != refreshed


def test_verify_hover_content(visit_the_internet, herokuapp, py):
    """
    Navigates to the Hover page in the Herokuapp webpage and verifies that content is
    visible when hovered over
    """
    herokuapp.click_on_link('hovers')
    py.get("body > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > img:nth-child(1)")\
        .hover()
    assert py.get("a[href='/users/2']").should().be_visible()


def test_verify_dropdown_selection(visit_the_internet, herokuapp, py):
    """
    Navigates to the Hover page in the Herokuapp webpage and verifies that dropdown content is
    selectable and present with selected
    """
    herokuapp.click_on_link('dropdown')
    selection = py.get("#dropdown").select_by_text("Option 2")
    assert selection.get_attribute("value") == "2"

