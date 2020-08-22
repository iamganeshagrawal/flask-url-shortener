from urlshort import create_app

def test_shorten(client):
    # Testing Home Page
    response = client.get('/')
    #Checking Shorten word is avaibale on page or not
    assert b'Shorten' in response.data