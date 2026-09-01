# GitHub Gists API Service

This is a small Flask app that calls the GitHub API and shows the public gists of a given user.
For example, going to `/octocat` will show a list of gists for the GitHub user **octocat**.

---

## How to run locally

1. Make sure you have Python 3.10 or newer installed.

2. Create a virtual environment and install the required packages:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   python -m pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   python app.py
   ```

4. Open your browser and go to <http://127.0.0.1:8080/octocat>

## How to run tests

This project uses pytest for testing. Run the tests with:

```bash
pytest
```

## How to run with Docker

Build the image:

```bash
docker build -t gist-api .
```

Run the container:

```bash
docker run -p 8080:8080 gist-api
```

Then open your browser and go to <http://127.0.0.1:8080/octocat>

## Files in this repo

- `app.py` → Flask app code
- `test_app.py` → basic test for the `/octocat` endpoint
- `requirements.txt` → Python dependencies
- `Dockerfile` → to build the container
- `.dockerignore` → keeps the venv and other local files out of the image
- `.gitignore` → keeps the venv and cache folders out of git
- `.github/workflows/flaskapp.yml` → runs the tests and builds the image on push
