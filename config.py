import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21993419")

API_HASH = os.environ.get("API_HASH", "92315b2cb9d11132dbb9d12d6fd3c0d4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6909596174:AAHS1FS0LIIUMPmUx8bBhBFTA0yAf8T5S88") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://surya2519990:feQJjOemwKKsIBti@cluster0.atjrk5v.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/db84ff24539bd7e4049d4.png")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6500361116').split()]

PORT = os.environ.get("PORT", "8080")
