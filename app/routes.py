from views import PollsList


def init_routes(app):
    app.router.add_route('GET', '/', PollsList, name='polls')
    return app
