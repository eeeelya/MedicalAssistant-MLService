from service.calculations import options
from service.serializers import RequestSerializer

OPTIONS = {
    "segmentation": options.segmentation,
}

def results(data):
    try:
        request_data = RequestSerializer(**data.form)
    except ValueError as err:
        error = f"Bad request! Error - {err}"
        return

    try:
        variant = OPTIONS[request_data.option]
    except KeyError as error:
        error = f"Key {error} doesn't exists!"

    result = variant(request_data)


def records():
    pass
