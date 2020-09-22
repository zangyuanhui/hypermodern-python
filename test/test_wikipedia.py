from hypermodern_test import wikipedia


def test_random_page_uses_given_language(mock_request_get):
    wikipedia.random_page(language="de")
    args, _ = mock_request_get.call_args
    assert "de.wikipedia.org" in args[0]
