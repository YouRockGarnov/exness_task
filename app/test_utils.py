from app import get_app

__test_client = get_app().test_client()


def make_get_req_to_server(endpoint):
    return __test_client.get(endpoint)


def make_post_req_to_server(endpoint, **kwargs):
    return __test_client.post(endpoint, **kwargs)