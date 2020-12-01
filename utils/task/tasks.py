import re
from datetime import datetime
from typing import NamedTuple, Optional, List, Dict

import pytz

from handlers.errors import exceptions

class Message(NamedTuple):
    """Структура распаршенного сообщения о новом расходе"""
    amount: int
    category_text: str

class Category(NamedTuple):
    """Структура категории"""
    codename: str
    name: str
    is_base_expense: bool
    aliases: List[str]

class Expense(NamedTuple):
    """Структура добавленного в БД нового расхода"""
    id: Optional[int]
    amount: int
    category_name: str


class Tasks():
    def __init__(self):
        pass

    def format_task(self, post):
        tags = post['tags']
        remind = post['remind']
        today = post['today']
        if tags == "":
            tags = ""
        else:
            tags = f"<u>Теги:</u> {tags}"

        if remind == "":
            remind = ""
        else:
            remind = f"<u>Напоминание:</u> {remind}"

        if today == 1:
            today = "☀️Сегодня"
        else:
            today = ""

        date = post["date_create"]
        msg = f"<b>{post['task']}</b>\n" \
              f"Заметка: {post['notes']}\n" \
              f"{today}\n" \
              f"<u>Категория:</u> {post['category']}\n" \
              f"{tags}\n" \
              f"{remind}\n" \
              f"<u>Создана:</u> {date}\n" \
              f"id{post['_id']}"
        return msg

    def find_task(self, text):
        return text[-24:]

    def _parse_message(self, raw_message: str):
        """Парсит текст пришедшего сообщения о новом расходе."""
        regexp_result = re.match(r"([\d ]+) (.*)", raw_message)
        if not regexp_result or not regexp_result.group(0) \
                or not regexp_result.group(1) or not regexp_result.group(2):
            raise exceptions.NotCorrectMessage(
                "Не могу понять сообщение. Напишите сообщение в формате, "
                "например:\n1500 метро")
        amount = regexp_result.group(1).replace(" ", "")
        category_text = regexp_result.group(2).strip().lower()
        return Message(amount=amount, category_text=category_text)

    def fill_aliases(self, categories,):
        """Заполняет по каждой категории aliases, то есть возможные
        названия этой категории, которые можем писать в тексте сообщения.
        Например, категория «кафе» может быть написана как cafe,
        ресторан и тд."""
        categories_result = []
        for category in categories:
            aliases = category["aliases"]
            aliases = list(filter(None, map(str.strip, aliases)))
            aliases.append(category["codename"])
            aliases.append(category["name"])
            categories_result.append(Category(
                codename=category['codename'],
                name=category['name'],
                is_base_expense=category['is_base_expense'],
                aliases=aliases
            ))
        return categories_result

    def get_category(self, category_name: str, categories):
        """Возвращает категорию по одному из её алиасов."""
        finded = None
        other_category = None
        for category in categories:
            if category.codename == "other":
                other_category = category
            for alias in category.aliases:
                if category_name in alias:
                    finded = category
        if not finded:
            finded = other_category
        return finded

    def get_now_formatted(self):
        """Возвращает сегодняшнюю дату строкой"""
        return self.get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")

    def get_now_datetime(self):
        """Возвращает сегодняшний datetime с учётом времненной зоны Мск."""
        tz = pytz.timezone("Europe/Moscow")
        now = datetime.now(tz)
        return now
