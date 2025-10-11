from string import Template
from datetime import datetime


USER_ACTION_TEMPLATE = Template("[${current_date}] user=${user}, action=${action} -> status=${status}")


def send_report_to_admin_panel(user, action, status):
    current_date = datetime.now()
    return USER_ACTION_TEMPLATE.substitute(
        current_date=current_date,
        user=user,
        action=action,
        status=status
    )


print(send_report_to_admin_panel("John", "typing", "online"))
