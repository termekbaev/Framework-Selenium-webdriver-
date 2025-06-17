class ChromeOptionsConfig:
    def __init__(
        self,
        arguments: list[str],
        page_load_strategy: str = "eager"
    ) -> None:
        self.arguments = arguments
        self.page_load_strategy = page_load_strategy