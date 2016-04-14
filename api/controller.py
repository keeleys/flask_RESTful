#!/usr/bin python
# -*- coding: utf-8 -*-
# Created by tianjun

from flask import Flask, jsonify, abort, request, make_response, url_for

from api import app
from api.auth import auth

_url = '/todo/api/v1.0'

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    }
]


@app.route("/")
def index():
    return "<a href='/todo/api/v1.0/tasks'>/todo/api/v1.0/tasks</a>"


@app.route(_url + '/tasks', methods=['GET'])
@auth.login_required  # 必须放在route下面,否则不生效
def get_tasks():
    return jsonify({'tasks': map(make_public_task, tasks), 'len': len(tasks)})


@app.route(_url + '/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': make_public_task(task[0])})


@app.route(_url + '/tasks', methods=['POST'])
def add_task():
    if not request.json or not 'title' in request.json:
        abort(400)

    id = 0 if len(tasks) == 0 else tasks[-1]['id'] + 1
    task = {
        'id': id,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': make_public_task(task)}), 201


@app.route(_url + '/tasks/<int:task_id>', methods=['PUT'])
def upload_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task = task[0]
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': make_public_task(task)})


@app.route(_url + '/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    print task

    tasks.remove(task[0])
    return jsonify({'result': True})


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": 'not found'}), 404)
