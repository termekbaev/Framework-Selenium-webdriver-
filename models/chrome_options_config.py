class ChromeOptionsConfig:
    def __init__(
        self,
        headless: bool = False,
        incognito: bool = True,
        disable_extensions: bool = True,
        lang: str = "en",
        window_size: str = "1920,1080",
        page_load_strategy: str = "eager"
    ) -> None:
        self.headless = headless
        self.incognito = incognito
        self.disable_extensions = disable_extensions
        self.lang = lang
        self.window_size = window_size
        self.page_load_strategy = page_load_strategy