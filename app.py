from flask import Flask, request, jsonify
from points_manager import PointsManager

app = Flask(__name__)
manager = PointsManager()

@app.route('/add', methods=['POST'])
def add_points():
    data = request.json
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']
    
    manager.add_points(payer, points, timestamp)
    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    data = request.json
    points_to_spend = data['points']
    
    try:
        spent_points = manager.spend_points(points_to_spend)
        return jsonify(spent_points), 200
    except ValueError as e:
        return str(e), 400

@app.route('/balance', methods=['GET'])
def get_balance():
    balance = manager.get_balance()
    return jsonify(balance), 200

if __name__ == '__main__':
    app.run(port=8000)
