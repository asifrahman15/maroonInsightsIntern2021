from flask import Flask, request, jsonify, Response
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
  return Response('''<h1>Use the below api endpoint format (key and value are case sensitive)</h1>\n<h1>http://127.0.0.1:5000/apifetch/collection/key/value/</h1>''')

@app.route('/apifetch/<colOpt>/<key>/<value>/', methods=['GET'])
def apiFetch(colOpt, key, value):
  client = MongoClient(f'''mongodb+srv://Rahman:rahman12345@rahmanmaroonintern.lmf10.mongodb.net/myFirstDatabase?retryWrites=true&w=majority''')
  Database1 = client.Database1
  colOpt = colOpt.capitalize()
  if colOpt == 'Students':
    collection = Database1.Students
  elif colOpt == 'Exams':
    collection = Database1.Exams
  else:
    return jsonify('Sorry, Please Check the collection Name....')
  
  try:
    fetchedData = list(collection.find({key : value}, {'_id':False}))
    return jsonify(fetchedData[0])
  except:
    return jsonify('Sorry, Unable to find the data....')

if __name__ == '__main__':
  app.run(debug = False)