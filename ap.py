import os

from dotenv import load_dotenv
from flask import Flask
from postgrest import APIError
from supabase import Client, create_client

load_dotenv()

app = Flask(__name__)


def get_supabase_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
    if not url or not key:
        raise RuntimeError(
            "Set SUPABASE_URL and SUPABASE_PUBLISHABLE_KEY in the environment."
        )
    return create_client(url, key)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def index():
    try:
        response = get_supabase_client().table("users").select("*").execute()
    except APIError as error:
        return f"<p>Error loading users: {error.message}</p>", 500

    users = response.data
    html = "<h1>users</h1><ul>"
    for user in users:
        html += f'<li>{user["email"]}</li>'
    html += "</ul>"
    return html


if __name__ == "__main__":
    app.run(debug=False)
