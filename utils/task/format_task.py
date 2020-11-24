

class Tasks():
    def __init__(self):
        pass

    def format_task(self, post):
        tags = post['tags']
        remind = post['remind']
        if tags == "":
            tags = ""
        else:
            tags = f"<u>Теги:</u> {tags}"

        if remind == "":
            remind = ""
        else:
            remind = f"<u>Напоминание:</u> {tags}"

        date = post["date_create"]
        msg = f"<b>Задача</b>\n\n " \
              f"{post['task']}\n" \
              f"<u>Категория:</u> {post['category']}\n" \
              f"{tags}\n" \
              f"{remind}\n" \
              f"<u>Создана:</u> {date}"
        return msg
