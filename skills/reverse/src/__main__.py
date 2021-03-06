
def main(req):
    """
    Scaffolding for error and convention handling
    """
    try:
        result = main_impl(req['payload'])
    # error handling
    except KeyError as e:
        result = {'error': 'Missing required key {0}'.format(e.args[0])}

    return {'payload': result}


def main_impl(payload):

    # get text from payload
    text = payload.get('text', "(silence)")

    # compute output
    return {'text': text[::-1]}
