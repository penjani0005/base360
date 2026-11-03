import os
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
if url and key:
    supabase = create_client(url, key)
else:
    class MockTable:
        def table(self, n): return self
        def upsert(self, d): print(f"MOCK {d}"); return self
        def insert(self, d): print(f"MOCK {d}"); return self
        def select(self, *a): return self
        def eq(self, *a): return self
        def execute(self): return type('obj', (), {'data': []})()
    supabase = MockTable()
