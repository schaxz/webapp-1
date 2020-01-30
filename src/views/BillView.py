#/src/views/BillView.py
from flask import request, Blueprint, json, Response
from ..models.BillModel import BillModel, BillSchema
from ..models.UserModel import UserModel, UserSchema
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
import uuid

bill_api = Blueprint('bill_api', __name__)
bill_schema = BillSchema()
auth = HTTPBasicAuth()

@bill_api.route('/', methods=['POST'])
def create():
  """
  Create Bill Function
  """
  req_data = request.get_json(force = True)
  bill_data = bill_schema.load(req_data)
  new_uuid = uuid.uuid4()
  bill_data.update({'id': str(new_uuid)})
  email_address_in_auth_header = request.authorization.username
  user_object = UserModel.get_user_by_email(email_address_in_auth_header)
  user_id = user_object.id
  bill_data.update({'owner_id': user_id})
  bill_object = BillModel(bill_data)
  bill_object.save()
  ser_data = bill_schema.dump(bill_object)
  return custom_response(ser_data, 201)

@bill_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Bills
  """
  email_address_in_auth_header = request.authorization.username
  user_object = UserModel.get_user_by_email(email_address_in_auth_header)
  user_id = user_object.id
  bills = BillModel.get_bills_by_owner_id(user_id)
  data = bill_schema.dump(bills, many = True)
  return custom_response(data, 200)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype = "application/json",
    response = json.dumps(res),
    status = status_code
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
            print(ser_user)
            return custom_response(ser_user, 200)
    return False
