from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.json.compact = False  # indent the JSON so it's readable in a browser

@app.route("/<username>")
def get_gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    try:
        r = requests.get(url, timeout=10)
    except requests.RequestException:
        return jsonify({"error": f"Could not reach GitHub for user {username}"}), 504
    if r.status_code != 200:
        return jsonify({"error": f"Unable to fetch gists for user {username}"}), r.status_code
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
