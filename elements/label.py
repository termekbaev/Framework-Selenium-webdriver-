from elements.base_element import BaseElement

class Label(BaseElement):
    def get_text(self) -> str:
        text = self.find_element().text
        self.logger.info(f"Get text '{text}' from '{self.name}' by locator {self.locator}")
        return text