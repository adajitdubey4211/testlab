from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def system_info():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get current IST time
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get 'top' command output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"
    
    # Generate response
    response = f"""
    <h2>Name: Ajit Dubey</h2>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h2>
    <pre>{top_output}</pre>
    """
    
    return response
cd
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
