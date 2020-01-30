#/src/views/BillView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BillModel import BillModel, BillSchema
from ..models.UserModel import UserModel, UserSchema
from flask_httpauth import HTTPBasicAuth
import re, uuid
from flask_bcrypt import Bcrypt

bill_api = Blueprint('bill_api', __name__)
bill_schema = BillSchema()
auth = HTTPBasicAuth()
bcrypt = Bcrypt()

@bill_api.route('/', methods=['POST'])
# @auth.login_required
def create():
  """
  Create Bill Function
  """
  req_data = request.get_json(force = True)
  print("STARTTTTTT")
  print(req_data)
  email_address_in_auth_header = request.authorization.username
  print(email_address_in_auth_header)
  user_object = UserModel.get_user_by_email(email_address_in_auth_header)
  print(user_object)
  user_id = user_object.id
  print(user_id)
  print(type(str(user_id)))
  bill_data = bill_schema.load(req_data)
  bill_data.update({'owner_id': str(user_id)})
  new_bill_uuid = uuid.uuid4()
  bill_data.update({'id': str(new_bill_uuid)})
  bill_object = BillModel(bill_data)
  bill_object.save()
  bill_schema_dump = bill_schema.dump(bill_object)
  print(bill_schema_dump)
  print("ENDDDDD")
  return custom_response(bill_schema_dump, 201)

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
