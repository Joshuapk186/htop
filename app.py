from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Joshua PK Kurian"  # Replace with your actual name
    username = os.environ.get('USER') or os.environ.get('USERNAME') or 'Unknown User'
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = str(e)

    response = f"""
    <html>
    <body>
        <h1>System Info</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre><strong>Top Output:</strong>\n{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
