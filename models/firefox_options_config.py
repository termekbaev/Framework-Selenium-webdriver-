class FirefoxOptionsConfig:
    def __init__(
        self,
        arguments: list[str],
        preferences: dict,
        page_load_strategy: str = "eager",
        window_size: str = "1920,1080"
    ) -> None:
        self.arguments = arguments
        self.preferences = preferences
        self.page_load_strategy = page_load_strategy
        self.window_size = window_size