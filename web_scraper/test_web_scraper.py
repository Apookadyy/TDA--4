from web_scraper import validate_url, scrape_page

def test_url_validation():
    assert validate_url("https://example.com") is True
    assert validate_url("invalid-url") is False

def test_scrape_output_structure():
    data = scrape_page("https://example.com")
    assert "title" in data
    assert "links" in data
