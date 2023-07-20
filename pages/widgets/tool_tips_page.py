from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    HOVER_ME_BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    HOVER_ME_BUTTON_HOVER_OVER = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
    HOVER_ME_FIELD = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    HOVER_ME_FIELD_HOVER_OVER = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
    COUNTRY_LINK = (By.XPATH, "//a[normalize-space()='Contrary']")
    COUNTRY_LINK_HOVER_OVER = (By.CSS_SELECTOR, "a[aria-describedby='contraryTextToolTip']")
    SECTION_LINK = (By.XPATH, "//a[normalize-space()='1.10.32']")
    SECTION_LINK_HOVER_OVER = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
    TOOL_TIP_INNERS = (By.CSS_SELECTOR, "div[class='tooltip-inner']")

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.go_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip = self.element_is_visible(self.TOOL_TIP_INNERS)
        tool_tip_text = tool_tip.text
        return tool_tip_text

    def check_tool_tips(self):
        button_tool_tip_text = self.get_text_from_tool_tips(self.HOVER_ME_BUTTON, self.HOVER_ME_BUTTON_HOVER_OVER)
        field_tool_tip_text = self.get_text_from_tool_tips(self.HOVER_ME_FIELD, self.HOVER_ME_FIELD_HOVER_OVER)
        contrary_tool_tip_text = self.get_text_from_tool_tips(self.COUNTRY_LINK, self.COUNTRY_LINK_HOVER_OVER)
        section_tool_tip_text = self.get_text_from_tool_tips(self.SECTION_LINK, self.SECTION_LINK_HOVER_OVER)
        return button_tool_tip_text, field_tool_tip_text, contrary_tool_tip_text, section_tool_tip_text
