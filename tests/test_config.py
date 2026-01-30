from config import load_config

def test_config_loading():
    config = load_config()
    assert "downloads_path" in config
    assert "email_settings" in config
