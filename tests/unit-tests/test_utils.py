import pytest
from pytest_mock import MockFixture

from donna.utils import make_directory


class TestUtils:
    @pytest.mark.parametrize("is_directory_present", [True, False])
    def test_make_directory(self, is_directory_present, mocker: MockFixture):
        # Arrange
        isdir_mock = mocker.patch("donna.utils.isdir")
        mkdir_mock = mocker.patch("donna.utils.mkdir")
        isdir_mock.return_value = is_directory_present
        path = "some/random/path"

        # Act
        make_directory(path)

        # Assert
        if is_directory_present:
            mkdir_mock.assert_not_called()
        else:
            mkdir_mock.assert_called_once_with(path)
