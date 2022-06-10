import pytest
from pytest_mock import MockFixture

from donna.services.screenshot.ss_taker import take_screenshots
from tests.donna_test_base import DonnaTestBase


class TestSSTaker(DonnaTestBase):
    def test_take_screenshots_for_exception(self):
        # Assert
        with pytest.raises(ValueError) as ex:
            take_screenshots(100, 1, "some/random/path")
        assert str(ex.value) == "'interval' should be less than 'duration'"

    def test_take_screenshots(self, mocker: MockFixture):
        # Arrange
        time_mock = mocker.patch("donna.services.screenshot.ss_taker.time")
        sleep_mock = mocker.patch("donna.services.screenshot.ss_taker.sleep")
        make_directory_mock = mocker.patch(
            "donna.services.screenshot.ss_taker.make_directory"
        )
        screenshot_mock = mocker.patch("donna.services.screenshot.ss_taker.screenshot")
        time_mock.side_effect = [(i + 1) for i in range(61)]
        screenshot_mock.return_value = mocker.Mock()
        interval = 30
        path = "some/random/path"

        # Act
        take_screenshots(interval, 1, path)

        # Assert
        make_directory_mock.assert_called_once_with(path)
        screenshot_mock.assert_called()
        sleep_mock.assert_called_with(interval)

    def test_command_take_ss(self, mocker: MockFixture):
        # Arrange
        take_screenshots_mock = mocker.patch("donna.services.screenshot.ss_taker.take_screenshots")
        interval = 30
        duration = 1
        path = "some/random/path"
        donna_command = ["take-ss", "--interval", interval, "--duration", duration, "--path", path]

        # Act
        result = self.cliRunner.invoke(self.entry_point, donna_command)

        # Assert
        take_screenshots_mock.assert_called_once_with(interval, duration, path)
        assert result.output == f"Screenshots are ready at '{path}'.\n"
