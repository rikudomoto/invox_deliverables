from flask_restful import Resource


class InvoxAPI(Resource):
  def test(self):
    return {"result":200}