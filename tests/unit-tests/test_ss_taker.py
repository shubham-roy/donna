import pytest
from pytest_mock import MockFixture

from donna.services.screenshot.ss_taker import take_screenshots
from tests.donna_test_base import DonnaTestBase


class TestSSTaker(DonnaTestBase):
    @pytest.fixture(autouse=True)
    def setup_ss_params(self):
        self.interval = 30
        self.duration = 1
        self.path = "some/random/path"

    def test_take_screenshots_for_exception(self):
        # Arrange
        interval = 100

        # Assert
        with pytest.raises(ValueError) as ex:
            take_screenshots(interval, self.duration, self.path)
        assert str(ex.value) == "'interval' should be less than 'duration'"

    def test_take_screenshots(self, mocker: MockFixture):
        # Arrange
        time_mock = mocker.patch("donna.services.screenshot.ss_taker.time")
        sleep_mock = mocker.patch("donna.services.screenshot.ss_taker.sleep")
        make_directory_mock = mocker.patch(
            "donna.services.screenshot.ss_taker.make_directory"
        )
        screenshot_mock = mocker.patch("donna.services.screenshot.ss_taker.screenshot")
        screenshot_mock.return_value = mocker.Mock()
        # time_mock will return one by one the elements of the list. For first call it will return 1, for second call it will return 2 and so on.
        time_mock.side_effect = [
            (i + 1) for i in range(61)
        ]  # 61 is chosen in order to exit while loop inside take_screenshots for given params.

        # Act
        take_screenshots(self.interval, self.duration, self.path)

        # Assert
        make_directory_mock.assert_called_once_with(self.path)
        screenshot_mock.assert_called()
        sleep_mock.assert_called_with(self.interval)

    def test_command_take_ss(self, mocker: MockFixture):
        # Arrange
        take_screenshots_mock = mocker.patch(
            "donna.services.screenshot.ss_taker.take_screenshots"
        )
        donna_command = [
            "take-ss",
            "--interval",
            self.interval,
            "--duration",
            self.duration,
            "--path",
            self.path,
        ]

        # Act
        result = self.cliRunner.invoke(self.entry_point, donna_command)

        # Assert
        take_screenshots_mock.assert_called_once_with(
            self.interval, self.duration, self.path
        )
        assert result.output == f"Screenshots are ready at '{self.path}'.\n"
