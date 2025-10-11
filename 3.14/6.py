

def get_course_info(course):
    sql_query = f"SELECT * FROM courses WHERE course='{course}'"
    return sql_query


if __name__ == '__main__':
    print(get_course_info("Python'; DROP TABLE courses;--"))

