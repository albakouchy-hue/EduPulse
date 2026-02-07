def generate_lesson(title: str, level: str):
    return {
        "title": title,
        "level": level,
        "lesson_plan": f"خطة درس ذكي لـ {title} للمستوى {level}"
    }
