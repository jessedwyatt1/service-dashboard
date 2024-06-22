from flask import Flask, render_template, send_from_directory
import subprocess
import os

app = Flask(__name__)

def check_services():
    try:
        result = subprocess.run(['/host/check_services.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip().split('\n')
        error_output = result.stderr.decode('utf-8').strip()

        print(f"Script output: {output}")
        print(f"Error output: {error_output}")

        services = {}
        for line in output:
            print(f"Processing line: {line}")
            if ':' in line:
                name, status = line.split(':')
                print(f"Service: {name}, Status: {status}")
                services[name] = status
            else:
                services[line] = 'unknown'
        print(f"Services: {services}")
        return services
    except Exception as e:
        print(f"Exception occurred: {e}")
        return {"error": str(e)}

@app.route('/')
def index():
    services = check_services()
    return render_template('index.html', services=services)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
