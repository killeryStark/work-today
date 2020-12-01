from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

task_button = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="☀️Сегодня",
                                               callback_data="today"
                                           ),
                                            InlineKeyboardButton(
                                               text="🎛Эзенхауэр",
                                               callback_data="eisenhower"
                                           )
                                       ],
                                        [
                                           InlineKeyboardButton(
                                               text="🗒Заметка",
                                               callback_data="notes"
                                           ),
                                            InlineKeyboardButton(
                                               text="⏰Напоминание",
                                               callback_data="remind"
                                           )
                                       ],
                                       [
                                            InlineKeyboardButton(
                                               text="✅Готово",
                                               callback_data="done"
                                           )
                                       ]
                                   ])

today_button = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="☀️Не Сегодня",
                                               callback_data="not_today"
                                           ),
                                            InlineKeyboardButton(
                                               text="🎛Эзенхауэр",
                                               callback_data="eisenhower"
                                           )
                                       ],
                                        [
                                           InlineKeyboardButton(
                                               text="🗒Заметка",
                                               callback_data="notes"
                                           ),
                                            InlineKeyboardButton(
                                               text="⏰Напоминание",
                                               callback_data="remind"
                                           )
                                       ],
                                       [
                                            InlineKeyboardButton(
                                               text="✅Готово",
                                               callback_data="done"
                                           )
                                       ]
                                   ])

eisenhower_button = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(
                                                     text="Важное Срочное",
                                                     callback_data="eisenhower1"
                                                 ),
                                                 InlineKeyboardButton(
                                                     text="Важное Несрочное",
                                                     callback_data="eisenhower2"
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Неважное Срочное",
                                                     callback_data="eisenhower3"
                                                 ),
                                                 InlineKeyboardButton(
                                                     text="Неважное Несрочное",
                                                     callback_data="eisenhower4"
                                                 )
                                             ]
                                         ])