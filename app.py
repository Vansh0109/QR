from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load CSV file or connect DB API here
DATA_SOURCE = "seed_packets.csv"
data = pd.read_csv(DATA_SOURCE)

@app.route('/')
def home():
    return "Welcome to the Seed QR Info System!"

@app.route('/seed-info')
def seed_info():
    seed_id = request.args.get('id')
    record = data[data['ID'] == seed_id]
    if record.empty:
        return "Invalid QR Code ID."
    return render_template("seed_template.html", seed=record.iloc[0])

if __name__ == '__main__':
    app.run(debug=True)
