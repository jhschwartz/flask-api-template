from flask import jsonify, redirect, url_for
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from app import my_api, mongo
from bson.json_util import dumps

parser = reqparse.RequestParser()
parser.add_argument('todo_name')
parser.add_argument('address')

class TodoList(Resource):
	def get(self):
		todoList = mongo.db.todos.find()
		return dumps(todoList)

	# adds new todo
	def post(self):
		args = parser.parse_args()
		entry = mongo.db.todos.insert({
			'todo_name': args['todo_name'],
			'address': args['address']
		})
		return dumps(entry)

class Todos(Resource):
	def get(self, todo_name):
		todo = mongo.db.todos.find_one_or_404({'todo_name': todo_name})
		return dumps(todo)

	# edits address field of a todo
	def put(self, todo_name):
		args = parser.parse_args()
		mongo.db.todos.update_one({
			'todo_name': todo_name
		},{
			'$set': {
				'address': args['address']
			}
		}, upsert=False)
		return 0

my_api.add_resource(TodoList, '/api/v1.0/todos')
my_api.add_resource(Todos, '/api/v1.0/todos/<string:todo_name>')