import bottle
from bottle import request, route
import json
from utils.db_helper import add_new_team, add_new_startup


@route('/new_team', method="POST")
def create_team():
    json_data = request.params.data
    add_new_team(json_data)
    return json.loads(json_data)


@route('/new_startup', method="POST")
def create_team():
    json_data = request.params.data
    # print(json_data)
    add_new_startup(json_data)
    return json.loads(json_data)


def main():
    app = bottle.app()
    bottle.run(app=app, port=8081)


if __name__ == "__main__":
    main()
