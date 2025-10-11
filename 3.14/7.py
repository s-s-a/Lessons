from string.templatelib import Template


def is_sql_injection(sequence: Template) -> bool|None:
    # print(sequence.strings)
    # print(sequence.interpolations)
    # print(sequence.values)

    for value in sequence.values:
        if "';" in value:
            print("SQL injection found")
            return True

def get_course_info(course: str) -> None:
    sql_query = t"SELECT * FROM courses WHERE course='{course}'"
    
    if not is_sql_injection(sql_query):
        print("Request being processed")


get_course_info("Python'; DROP TABLE courses;--")
