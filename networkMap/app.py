from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Network data with the specified structure
network_data = {
    "nodes": [
        {"id": "gateway", "label": "Gateway", "type": "gateway"},
        {"id": "main_switch", "label": "Main Switch", "type": "switch"},
        {"id": "server_switch", "label": "Server Switch", "type": "switch"},
    ] + [
        {"id": f"server{i+1}", "label": f"Server {i+1}", "type": "server"} for i in range(5)
    ] + [
        {"id": f"small_switch1_{i+1}", "label": f"Small Switch 1.{i+1}", "type": "switch"} for i in range(3)
    ] + [
        {"id": f"computer1_{i*4+j+1}", "label": f"Computer 1.{i*4+j+1}", "type": "computer"} for i in range(3) for j in range(4)
    ] + [
        {"id": "small_switch2", "label": "Small Switch 2", "type": "switch"}
    ] + [
        {"id": f"computer2_{i+1}", "label": f"Computer 2.{i+1}", "type": "computer"} for i in range(3)
    ] + [
        {"id": "small_switch3", "label": "Small Switch 3", "type": "switch"}
    ] + [
        {"id": f"computer3_{i+1}", "label": f"Computer 3.{i+1}", "type": "computer"} for i in range(2)
    ],
    "edges": [
        {"from": "gateway", "to": "main_switch"},
        {"from": "main_switch", "to": "server_switch"},
    ] + [
        {"from": "server_switch", "to": f"server{i+1}"} for i in range(5)
    ] + [
        {"from": "main_switch", "to": f"small_switch1_{i+1}"} for i in range(3)
    ] + [
        {"from": f"small_switch1_{i+1}", "to": f"computer1_{i*4+j+1}"} for i in range(3) for j in range(4)
    ] + [
        {"from": "main_switch", "to": "small_switch2"}
    ] + [
        {"from": "small_switch2", "to": f"computer2_{i+1}"} for i in range(3)
    ] + [
        {"from": "small_switch2", "to": "small_switch3"}
    ] + [
        {"from": "small_switch3", "to": f"computer3_{i+1}"} for i in range(2)
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/network')
def network():
    return jsonify(network_data)

if __name__ == '__main__':
    app.run(debug=True)
