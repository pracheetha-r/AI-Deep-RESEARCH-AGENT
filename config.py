import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "groq/compound")
MAX_SEARCH_RESULTS = 3

"""One file that loads your .env and makes the settings available to all other files. Instead of loading the key in every file separately, you import it from here.
Why this way: If you ever change a setting (like switching to a different model), you change it in one place — not in 5 different files."""