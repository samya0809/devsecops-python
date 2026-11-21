from app import app, home, health


def test_home_unit():
    with app.test_request_context("/"):
        response = home()

        assert response.get_json()["message"] == "Welcome to DevSecOps Python Application"
        assert response.get_json()["status"] == "Running securely"


def test_health_unit():
    with app.test_request_context("/health"):
        response = health()

        assert response.get_json()["status"] == "healthy"
