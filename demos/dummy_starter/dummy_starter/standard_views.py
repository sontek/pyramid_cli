from pyramid.response import Response


def hello_world(request):
    return Response('Hello world!')


def route_and_view_attached(request):
    return Response('Hello world!')
