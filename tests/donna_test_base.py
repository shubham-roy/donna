import pytest
from pytest_mock import MockFixture
from click.testing import CliRunner

from donna.cli import entry_point


# This class is intended to be used as a parent class when testing Donna's commands.
class DonnaTestBase:
    @pytest.fixture(autouse=True)
    def setup(self, mocker: MockFixture):
        self.entry_point = entry_point
        self.cliRunner = CliRunner()
        self.logger_mock = mocker.patch("donna.cli.logger")
        self.make_directory_mock = mocker.patch("donna.cli.make_directory")
        self.join_mock = mocker.patch("donna.cli.join")
        self.isfile_mock = mocker.patch("donna.cli.isfile")
        self.isfile_mock.return_value = False
