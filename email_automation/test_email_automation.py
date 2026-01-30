from email_automation import load_template, format_email

def test_template_loading():
    template = load_template("welcome_email")
    assert template is not None
    assert "{username}" in template

def test_email_formatting():
    content = format_email(
        "Hello {name}",
        {"name": "User"}
    )
    assert content == "Hello User"
