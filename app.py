from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_settings', methods=['POST'])
def get_settings():
    instance_id = request.form.get('instanceId')
    api_token = request.form.get('apiToken')

    if not instance_id or not api_token:
        return jsonify({'error': 'Please provide Instance ID and API Token!'}), 400

    url = f"https://api.green-api.com/waInstance{instance_id}/getSettings/{api_token}"
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_state_instance', methods=['POST'])
def get_state_instance():
    instance_id = request.form.get('instanceId')
    api_token = request.form.get('apiToken')

    if not instance_id or not api_token:
        return jsonify({'error': 'Please provide Instance ID and API Token!'}), 400

    url = f"https://api.green-api.com/waInstance{instance_id}/getStateInstance/{api_token}"
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    instance_id = request.form.get('instanceId')
    api_token = request.form.get('apiToken')
    chat_id = request.form.get('chatIdMessage')
    message = request.form.get('message')

    if not instance_id or not api_token or not chat_id or not message:
        return jsonify({'error': 'Please fill all fields for sending a message!'}), 400

    url = f"https://api.green-api.com/waInstance{instance_id}/sendMessage/{api_token}"
    payload = {
        'chatId': f"{chat_id}@c.us",
        'message': message
    }

    try:
        response = requests.post(url, json=payload)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send_file', methods=['POST'])
def send_file():
    instance_id = request.form.get('instanceId')
    api_token = request.form.get('apiToken')
    chat_id = request.form.get('chatIdFile')
    file_url = request.form.get('fileUrl')

    if not instance_id or not api_token or not chat_id or not file_url:
        return jsonify({'error': 'Please fill all fields for sending a file!'}), 400

    url = f"https://api.green-api.com/waInstance{instance_id}/sendFileByUrl/{api_token}"
    payload = {
        'chatId': f"{chat_id}@c.us",
        'urlFile': file_url,
        'fileName': file_url.split('/')[-1]  # URL
    }

    try:
        response = requests.post(url, json=payload)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
