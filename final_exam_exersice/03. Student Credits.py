def students_credits(*args):
    my_dict = {}
    total_credits = 0
    result = ''
    for i in args:
        course_name, credits, max_test_points, points = i.split('-')
        points_result = int(points) / int(max_test_points)
        course_credits = points_result * int(credits)
        if course_name not in my_dict:
            my_dict[course_name] = course_credits
            total_credits += course_credits

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: -x[1]))
    if total_credits < 240:
        result += f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma." + '\n'
    else:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits." + '\n'

    for k, v in sorted_dict.items():
        result += f"{k} - {v:.1f}" + '\n'
    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
