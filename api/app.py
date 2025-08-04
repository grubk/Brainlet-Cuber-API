from flask import Flask, request, jsonify
import kociemba

app = Flask(__name__)
@app.route('/solve/<cube_position>', methods=['GET'])
def solve_cube_url(cube_position):
    try:
        solution = kociemba.solve(cube_position)
        return jsonify({"solution": solution})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/')
def index():
    return "Welcome to Brainlet Cuber's API. Use GET /solve/<cube_position> to get the solution."

if __name__ == '__main__':
    app.run(debug=True)



