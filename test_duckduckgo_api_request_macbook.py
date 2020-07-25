import requests

def test_duckduckgo_instant_answer_search():
    #Arrange your input/target which is the endpoint url
    #Add your endpoint url & query parameters for the Macbook search test
    url = "https://api.duckduckgo.com/?q=Macbook&ia=shopping&format=json"

    #Act on the target behaviour
    #Call the API using the url using requests & parse the response body from json to a python dictionary
    response = requests.get(url)
    body = response.json()

    #Assert expected outcomes
    #Status code, Body(Abstract text/source/url)
    assert response.status_code == 200
    assert "MacBook" in body["AbstractText"]
    assert "Wikipedia" in body["AbstractSource"]
    assert "https://en.wikipedia.org/wiki/MacBook" in body ["AbstractURL"]