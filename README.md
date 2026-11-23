# Backend deployment on Render

This folder contains the Flask backend prepared for Render's native Python runtime.

## Deploy

1. Upload this folder to a Git repository (or place its contents in the backend directory of your existing repository).
2. In Render, create a **Web Service** and connect that repository. If the backend is in a subfolder, set **Root Directory** to that folder.
3. Set **Build Command** to `pip install -r requirements.txt`.
4. Set **Start Command** to `gunicorn ap:app`.
5. In the Render service's **Environment** settings, add:
   - `SUPABASE_URL` — your Supabase project URL.
   - `SUPABASE_PUBLISHABLE_KEY` — your Supabase publishable key.
6. Deploy. Visit `/health` to check that the service is running.

Do not upload a real `.env` file or commit secret keys. `.env.example` only shows the required variable names and formats.

The `/` route reads the `users` table and displays each row's `email`. Ensure the table exists and its Supabase Row Level Security policies allow the intended access. The health endpoint does not check Supabase connectivity.

## Run locally

Create a virtual environment, install `requirements.txt`, set the two environment variables (or copy `.env.example` to `.env` and fill in real values), then run `python ap.py`.
