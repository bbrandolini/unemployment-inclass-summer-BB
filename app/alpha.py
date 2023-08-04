

import os
from dotenv import load_dotenv

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
