from pages.alerts_frames_windows.alerts_page import AlertsPage


class TestAlerts:
    page_link = 'https://demoqa.com/alerts'

    def test_see_alert(self, driver):
        alerts_page = AlertsPage(driver, self.page_link)
        alerts_page.open()

        alert_text = alerts_page.check_see_alert()
        assert alert_text == "You clicked a button", "Alert didn't show up"

    def test_alert_appear_after_5_second(self, driver):
        alerts_page = AlertsPage(driver, self.page_link)
        alerts_page.open()

        alert_text = alerts_page.check_alert_appear_5_sec()
        assert alert_text == "This alert appeared after 5 seconds", "Alert didn't show up"

    def test_confirm_alert(self, driver):
        alerts_page = AlertsPage(driver, self.page_link)
        alerts_page.open()

        alert_text = alerts_page.check_confirm_alert()
        assert alert_text == "You selected Ok", "Alert didn't show up"

    def test_prompt_alert(self, driver):
        alerts_page = AlertsPage(driver, self.page_link)
        alerts_page.open()

        text, alert_text = alerts_page.check_prompt_alert()
        assert alert_text == f"You entered {text}", "Alert didn't show up"
