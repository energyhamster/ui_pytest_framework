from config import BASE_URL
from pages.alerts_frames_windows.frames_page import FramesPage


class TestFrames:
    page_link = BASE_URL + '/frames'

    def test_frames(self, driver):
        frames_page = FramesPage(driver, self.page_link)
        frames_page.open()

        result_frame1 = frames_page.check_frame("frame1")
        result_frame2 = frames_page.check_frame("frame2")

        assert result_frame1 == ["This is a sample page", "500px", "350px"], "The frame does not exist"
        assert result_frame2 == ["This is a sample page", "100px", "100px"], "The frame does not exist"
