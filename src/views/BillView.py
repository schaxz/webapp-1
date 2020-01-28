#/src/views/BillView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BillModel import BillModel, BillSchema

bill_api = Blueprint('bill_api', __name__)
bill_schema = BillSchema()

@bill_api.route('/', methods=['POST'])
@auth.login_required
def create():
  """
  Create Bill Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = bill_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = BillModel(data)
  post.save()
  data = bill_schema.dump(post).data
  return custom_response(data, 201)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

@auth.verify_password
def authenticate(username, password):
    if username and password:
        user_object = UserModel.get_user_by_email(username)
        authorized_boolean = user_object.check_hash(password)
        if not authorized_boolean:
            return False
        else:
            ser_user = user_schema.dump(user_object)
            return custom_response(ser_user, 200)
    return False
