from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class User(Resource):
  """
    Update database with finished game data
  """
  def post(self):
    try:
      userId = request.get_json()["userId"]
    except:
      return {"error": "'userId' not provided"}, 400
    
    try:
      won = request.get_json()["won"]
    except:
      return {"error": "boolean 'won' not provided"}, 400

    response = "Not implemented yet"

    return response, 201
    

# class queue(Resource):
#   def post(self):
#     """ If userid is not in POST form then return 400 Bad Request """
#     # if hasattr(request,'userid'):
#     #   return {'error': 'userid not provided'}, 400
#     try:
#       userid = request.get_json()["userid"]
#     except: 
#       return {"error": "userid not provided"}, 400 
#     """ Enqueue the user and dequeue with matcher function """
#     job = q.enqueue_call(func=matcher,
#               args=(userid,),
#               timeout=30,
#               job_id=str(userid))
#     return {"userid": job.id, "enqueued_at": str(job.enqueued_at)}, 200

# class create(Resource):
#   def post(self):
#     try:
#       userid = request.get_json()["userid"]
#     except: 
#       return {"error": "userid not provided"}, 400 
    
#     x = {
#       "id": userid,
#       "score": 100
#     }

#     json_res = json.dumps(x)

#     r.set(f"user:{userid}", str(json_res))
#     r.sadd("users", f"user:{userid}")
#     return {"message": f"user {userid} created"}, 201

api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port=6000)