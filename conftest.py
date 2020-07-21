from fixture.application import Application
import pytest


@pytest.fixture(scope="session")  # фикстура запуска браузера создается 1 на всю сессию
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
