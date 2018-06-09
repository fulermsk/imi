from flask import render_template, Flask, request, jsonify
from StorageClass import Data

values = dict(s_but_start_yes=0,
              s_but_power_on_yes=0,
              s_but_prim_yes=0,
              s_but_caps_yes=0,
              s_but_launch_yes=0,
              s_but_error=0,
              auu_start=0,
              auu_power=0,
              auu_prim=0,
              auu_caps=0,
              auu_launch=0)
STORAGE_OBJECT = Data()
STORAGE_OBJECT.write_file(values)


class Config(object):
    SECRET_KEY = 'asd12u39whkdjshfoiauwy3hrqkwefndslzngag1q'


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/ping/", methods=['POST'])
def ping():
    return jsonify({"answer": 0})


@app.route('/command/<string:cmd>', methods=['GET', 'POST'])
def exec_(cmd):
    if request.method == 'POST':
        if cmd == 'send':
            data = request.get_json()
            if data['packet'][0] == 0x1234:
                STORAGE_OBJECT.data = data['packet']
                STORAGE_OBJECT.status = data['packet'][30]
                values = STORAGE_OBJECT.get_values()
                for u in range(1, 30):
                    if (data["packet"][u] & 1 << values["s_but_start_yes"]) == 1 << values["s_but_start_yes"]:
                        values["auu_start"] = 1
                    if (data["packet"][u] & 1 << values["s_but_power_on_yes"]) == 1 << values["s_but_power_on_yes"]:
                        values["auu_power"] = 1
                    if (data["packet"][u] & 1 << values["s_but_prim_yes"]) == 1 << values["s_but_prim_yes"]:
                        values["auu_prim"] = 1
                    if (data["packet"][u] & 1 << values["s_but_caps_yes"]) == 1 << values["s_but_caps_yes"]:
                        values["auu_caps"] = 1
                    if (data["packet"][u] & 1 << values["s_but_launch_yes"]) == 1 << values["s_but_launch_yes"]:
                        values["auu_launch"] = 1
                    if (data["packet"][u] & 1 << values["s_but_error"]) == 1 << values["s_but_error"]:
                        STORAGE_OBJECT.is_end_work = 1
            STORAGE_OBJECT.write_file(values)
            return jsonify({"answer": 0})
        if cmd == 'reсeive':
            data = request.get_json()
            return jsonify({"answer": 0, "data": STORAGE_OBJECT.data})



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/data/', methods=['GET'])
def get_update():
    data = STORAGE_OBJECT.get_values()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
