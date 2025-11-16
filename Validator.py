import validators

def validate(url) -> bool:
    res = validators.url(url)
    return res