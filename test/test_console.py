import click.testing
import pytest
import requests

from hypermodern_test import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


# @pytest.fixture
# def mock_request_get(mocker):
#     mock = mocker.patch("requests.get")
#     mock.return_value.__enter__.return_value.json.return_value={
#         "title": "Lorem Ipsum",
#         "extract": "Lorem ipsum dolor sit amet",
#     }
#     return mock


def test_main_succeeds(runner, mock_request_get):
    runner.invoke(console.main)
    args, _ = mock_request_get.call_args
    # assert "Lorem Ipsum" in result.output
    # assert mock_request_get.called
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_request_get):
    mock_request_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner, mock_request_get):
    mock_request_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("hypermodern_test.wikipedia.random_page")


def test_main_uses_specified_languafge(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
