from elements.base_element import BaseElement

class Input(BaseElement):
    def type(self, text: str) -> None:
        self.find_element().send_keys(text)

    def clear_and_type(self, text: str) -> None:
        elem = self.find_element()
        elem.clear()
        elem.send_keys(text)