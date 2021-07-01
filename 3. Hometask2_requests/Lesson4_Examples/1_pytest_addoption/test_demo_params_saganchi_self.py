import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 500])
def test_url_status(url, code, method):
    url = url + f"/status/{code}"
    response = method(url)
    assert response.status_code == code
