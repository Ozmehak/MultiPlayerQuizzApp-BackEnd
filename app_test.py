from app import app

welcome_message = 'Welcome to the API for our Multiplayer Quizz App!'

def test_api_index():
    with app.test_client() as client:  # type: FlaskClient
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == f'{welcome_message}'

