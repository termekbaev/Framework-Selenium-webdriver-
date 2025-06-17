from elements.base_element import BaseElement

class Button(BaseElement):
    def click(self) -> None:
        self.logger.info(f"Clicking element: {self.name} = {self.locator}")
        try:
            self.find_element().click()
        except Exception as e:
            self.logger.error(f"Click failed on {self.locator}: {str(e)}")
            raise