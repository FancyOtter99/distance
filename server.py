from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/your_endpoint', methods=['POST'])
def receive_distance():
    data = request.get_json()
    if not data or 'distance_cm' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    distance = data['distance_cm']
    print(f"Received distance: {distance} cm")
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
