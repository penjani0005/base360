\# Base360 AI Interview Automation



Live FastAPI + OpenAI tool-use + Supabase + Twilio



\*\*Status: LIVE at http://127.0.0.1:8000\*\*



\## What it does

\- FastAPI webhook receives candidate data

\- OpenAI function calling extracts / scores interview answers

\- Supabase stores candidates + transcripts

\- Twilio SMS triggers follow-ups



\## Stack

Python 3.11, FastAPI, Uvicorn, OpenAI 3.44, Supabase 2.34, Twilio, Pydantic v2, httpx



\## Run (fixed Python 3.14 Rust error by downgrading to 3.11)

C:\\Users\\USER\\venv\\Scripts\\python.exe -m pip install fastapi uvicorn supabase python-dotenv openai twilio pydantic httpx python-multipart

uvicorn app.main:app --reload



\## Proof

\- Screenshot: Application startup complete

\- GitHub: github.com/penjani0005/base360

\- Builder: Penjani — Lusaka, Zambia (GMT+2), ZamFit Pro (Play Store) + GetBrains



Built for Blacksmith AI Agency interview

