# (generated with --quick)

from typing import Any

click: module
console: module
mock_wikipedia_random_page: Any
pytest: Any
requests: module
runner: Any
test_main_succeeds_in_production_env: Any

def test_main_fails_on_request_error(runner, mock_request_get) -> None: ...
def test_main_prints_message_on_request_error(runner, mock_request_get) -> None: ...
def test_main_succeeds(runner, mock_request_get) -> None: ...
def test_main_uses_specified_languafge(runner, mock_wikipedia_random_page) -> None: ...
