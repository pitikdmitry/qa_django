def add_new(x):
    str_1 = '\n'
    x += str_1
    return x


def app(environ, start_response):
    data = []
    query_string = environ.get("QUERY_STRING")
    data = query_string.split("&")
    data = list(map(add_new, data))
    data = list(map(lambda x: bytes(x, 'utf-8'), data))
    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    return iter(data)
