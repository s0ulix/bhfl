import flask
from flask import request, jsonify
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

#@app.route('/bfhl', methods=['POST'])
class bfhl(Resource):
    def post(self):
        data = request.json
        data = data['data']
        alp = []
        num = []
        n = "0123456789"
        for i in data:
            if i[0] in n:
                num.append(i)
            else:
                alp.append(i)

        result = {"is_success": True, "user_id": "girish_kumar_sharma_22022001", "email": "girishsh640@gmail.com",
                  "roll_number": "11909037", "numbers": num, "alphabets": alp}
        return jsonify(result)
'''
def bajaj_api():
    data=request.json
    data=data['data']
    alp=[]
    num=[]
    n="0123456789"
    for i in data:
        if i[0] in n:
            num.append(i)
        else:
            alp.append(i)

    result={"is_success":True,"user_id":"girish_kumar_sharma_22022001","email":"girishsh640@gmail.com","roll_number":"11909037","numbers":num,"alphabets":alp}

    return jsonify(result)'''
api.add_resource(bfhl, '/bfhl')
app.run(debug=True)
