from datetime import datetime


def send_report_to_admin_panel(user, action, status):
    current_date = datetime.now()
    return f"[{current_date}] {user=}, {action=} -> {status=}"

print(send_report_to_admin_panel("John", "typing", "online"))
