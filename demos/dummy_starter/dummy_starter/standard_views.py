from pyramid.response import Response


def hello_world(request):
    return Response('Hello world!')

class ClassBasedView(object):
    def __init__(request):
        self.request = request

    def awesome_attr(request):
        return Response('Hello moon!')

def route_and_view_attached(request):
    return Response('Hello world!')
