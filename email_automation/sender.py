# email_automation/sender.py

def email_status():
    templates = 8
    emails_sent = 324
    recipients = 156
    open_rate = 68.5
    click_rate = 24.3
    next_campaign = "Tomorrow 9:00 AM" # next scheduled campaign time

    print("\n📧 EMAIL AUTOMATION:")
    print(f"✅ Templates: {templates} configured")

    print("📊 Statistics:")
    print(f"   • Emails Sent: {emails_sent}")
    print(f"   • Recipients: {recipients}")
    print(f"   • Open Rate: {open_rate}%")
    print(f"   • Click Rate: {click_rate}%\n")

    print(f"⏰ Next Campaign: {next_campaign}")

