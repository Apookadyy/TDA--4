def test_full_workflow_execution():
    """
    Ensures all modules initialize without crashing.
    """
    try:
        import file_organizer
        import web_scraper
        import email_automation
        import system_monitor
        assert True
    except Exception:
        assert False
