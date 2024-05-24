class Language:
    def __init__(self, DESCRIPTION_TEXT, MESSAGE_TEXT, SUCCESS_TEXT, NEW_VIDEO_TEXT, LOADING_TEXT, LOADING_VIDEO_TEXT, SENDING_TEXT, CLEANING_TEXT, CLEANING_DISABLED_TEXT, COOLDOWN_TEXT, FIRST_LAUNCH_TEXT):
        self.DESCRIPTION_TEXT = DESCRIPTION_TEXT
        self.MESSAGE_TEXT = MESSAGE_TEXT
        self.SUCCESS_TEXT = SUCCESS_TEXT
        self.NEW_VIDEO_TEXT = NEW_VIDEO_TEXT
        self.LOADING_TEXT = LOADING_TEXT
        self.LOADING_VIDEO_TEXT = LOADING_VIDEO_TEXT
        self.SENDING_TEXT = SENDING_TEXT
        self.CLEANING_TEXT = CLEANING_TEXT
        self.CLEANING_DISABLED_TEXT = CLEANING_DISABLED_TEXT
        self.COOLDOWN_TEXT = COOLDOWN_TEXT
        self.FIRST_LAUNCH_TEXT = FIRST_LAUNCH_TEXT

ru = Language(
    DESCRIPTION_TEXT="\n<b>Описание:</b>\n\n<code>%(DESCRIPTION)s</code>",
    MESSAGE_TEXT="<a href='%(URL)s'><b>❗️ Новое видео!</b></a>\n<code>%(NAME)s</code>%(DESCRIPTION)s\n\n📅 %(DATE)s",
    SUCCESS_TEXT="Готово!",
    NEW_VIDEO_TEXT="Изменения в списке видео!",
    LOADING_TEXT="Загрузка видео...",
    LOADING_VIDEO_TEXT='Видео "%(video_name)s" (%(video_id)s) готовится к отправке...',
    SENDING_TEXT="Отправка сообщения...",
    CLEANING_TEXT="Очистка от временных файлов... (для отключения измени переменную DeleteTempFiles)",
    CLEANING_DISABLED_TEXT="Очистка от временных файлов отключена.",
    COOLDOWN_TEXT="Следующая проверка начнется через %s сек.",
    FIRST_LAUNCH_TEXT="Первый запуск, поиск новых видео не будет начат. "
)

en = Language(
    DESCRIPTION_TEXT="\n<b>Description:</b>\n\n<code>%(DESCRIPTION)s</code>",
    MESSAGE_TEXT="<a href='%(URL)s'><b>❗️ New video!</b></a>\n<code>%(NAME)s</code>%(DESCRIPTION)s\n\n📅 %(DATE)s",
    SUCCESS_TEXT="Done!",
    NEW_VIDEO_TEXT="Changes in the video list!",
    LOADING_TEXT="Loading...",
    LOADING_VIDEO_TEXT='Video "%(video_name)s" (%(video_id)s) is being prepared for sending...',
    SENDING_TEXT="Sending message...",
    CLEANING_TEXT="Cleaning temporary files... (to disable, change the DeleteTempFiles variable)",
    CLEANING_DISABLED_TEXT="Cleaning temporary files is disabled.",
    COOLDOWN_TEXT="Next check will start in %s seconds.",
    FIRST_LAUNCH_TEXT="First launch, no search for new videos will be initiated. "
)