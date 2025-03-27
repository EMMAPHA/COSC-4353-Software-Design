import requests

def get_response(word):
    return requests.get(f"https://agiledeveloper.com/spellcheck?check={word}").text

def parse_response(response):
    return response == 'true'

def is_spelling_correct(word):
    return parse_response(get_response(word))
