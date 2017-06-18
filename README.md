# flask-api-template

This is a template for a simple flask api using flask-restful and MongoDB.

Prereqs:
- Python 2.7+
- Virtual Env
- Mongo
- Pymongo

To get started in Terminal:
1. `git clone https://github.com/jhschwartz/flask-api-template.git`
2. `cd flask-api-template`
3. `vitualenv flask`
4. `source flask/bin/activate`
5. `pip install -r requirements.txt`
6. `chmod a+x run.py`
7. `./run.py`
8. Make api calls (ex: `curl http://localhost:5000/api/v1.0/cafes`)
9. Make your own api, in `app/api/api.py` or by creating api files in `app/api` (remember to import new files in `app/api/__init__.py`)
