# =============================================================
# DAY 01 - Functions, Parameters & Arguments
# 30-Day Python| Data Engineering Track
# =============================================================

# ── 1. BASIC FUNCTION (No Parameters) ────────────────────────
# A function with no input, just returns a fixed greeting
def greet_me():
    return "Hello,there....! Good Morning"
print(greet_me())

# ── 2. PERSONALIZED GREETINGS (3 Formatting Styles) ──────────

# Style 1: String Concatenation (old way, avoid in production)
def string_greet(name):
    return "Hello,"+name+"! How are you?"
print(string_greet("Dinaya"))

# Style 2: .format() method (cleaner than concatenation)
def format_greet(name):
    return "Welcome to the team,{}!" .format(name)
print(format_greet("lachlyn"))

# Style 3: f-string (modern, preferred in Python 3.6+)
def mparameter_greet(time_of_day,name):
    return f"Good{time_of_day},{name}!Have a great day."
print(mparameter_greet("morning","Nina"))

# ── 3. USER INPUT INSIDE A FUNCTION ──────────────────────────
# Takes live input from the user during runtime
def user_greet():
    user_name=input("Name:")
    return f"it's good to see you,{user_name}"
print(user_greet())

# ── 4. BASIC MATH FUNCTIONS ───────────────────────────────────
# Simple single-purpose functions — each does one operation only
# This is called the Single Responsibility Principle (SRP)

def product(a, b):
    return a*b
print(product(7,10))

# Default parameter — if d is not passed, it uses 10
def mul(c, d=10):
    return c*d
print(mul(9))      # Uses default d=10 → Output: 90
print(mul(10,8))   # Overrides default → Output: 80

def add(q,w):
    return q+w

def sub(e,r):
    return e-r

def div(t,y):
    return t//y

def pow(u,i):
    return u**i
print(add(7,13))
print(sub(21,5))
print(div(18,6))
print(pow(2,5))

# ── 5. MATH ROUTER (Dispatcher Pattern) ───────────────────────
# Routes user input to the correct math function
# This pattern is used in real data pipelines and API handlers
def math_router(l,m,operation):
    if (operation=="add"):
        return add(l,m)
    elif (operation=="sub"):
        return sub(l,m)
    elif (operation=="mul"):
        return mul(l,m)
    elif (operation=="div"):
        return div(l,m)
    elif (operation=="pow"):
        return pow(l,m)
    else:
        return "Error:Not a math op"
operation=input("operation:")
print(math_router(4,3,operation))
    
# ── 6. GENERATE SCHEMA (Dictionary Return) ────────────────────
# Simulates generating a database table schema
# In real DE work, this pattern is used in metadata management    
def generate_schema(table_name,columns):
    return {
        "table":table_name,
        "columns":columns,
        "column_count":len(columns)
    }
table_name="users"
columns=["name","ph.no","Govt.ID","Email"]
print(generate_schema(table_name,columns))

# ── 7. FIRST AND LAST ELEMENT ─────────────────────────────────
# Returns the first and last item from any list
# index[0] = first item, index[-1] = last item (negative indexing)
def get_first_and_last(data):
    return data[0],data[-1]
my_list=[10,20,30,40,50,60]
print(get_first_and_last(my_list))

# ── 8. FILTER EVEN NUMBERS ────────────────────────────────────
# Loops through a list and collects only even numbers
# num % 2 == 0 means no remainder when divided by 2 → even
def get_even(numbers):
    evens=[]
    for num in numbers:
        if num%2==0:
            evens.append(num)
    return evens
integers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(get_even(integers))

# ── 9. AVERAGE CALCULATOR ─────────────────────────────────────
# Calculates the average of a list of numbers
# Guard clause at the start prevents division by zero

def get_average(numbers):
    if len(numbers)==0: 
        return 0               # Edge case: empty list protection
    t_sum=sum(numbers)
    count=len(numbers)
    return t_sum/count
grades=[100,95,67,78,91,89]
print(get_average(grades))

# ── 10. BATCH DATA ─────────────────────────────────────────────
# Splits a large list into smaller fixed-size chunks (batches)
# Used heavily in: ETL pipelines, API rate limiting, ML training
# range(start, stop, step) — step here is the batch size
def batch_data(data,batch_size):
    batches=[]
    for i in range(0,len(data),batch_size):
        batches.append(data[i:i+batch_size])
    return batches
cookie=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(batch_data(cookie,4))

# ── 11. SLIDING WINDOW ─────────────────────────────────────────
# Moves a fixed-size window across a list, one step at a time
# Used in: time-series analysis, stream processing, moving averages
# len(data) - window_size + 1 ensures we don't go out of bounds
def sliding_window(data,window_size):
    sub=[]
    for i in range(len(data)-window_size+1):
        sub.append(data[i:i+window_size])
    return sub
tot=[21,22,23,24,25,26,27,28,29,30]
print(sliding_window(tot,3))

# ── 12. CREATE USER + BUILD DATABASE ──────────────────────────
# Function creates a single user dictionary (like a DB record)
def create_user(user_id,name,role):
    return{
        "user":user_id,
        "fullname":name,
        "role":role
    }# zip() combines multiple lists element by element
# This simulates inserting multiple rows into a database table
user_ids = ["101", "102", "103"]
names = ["sita", "geetha", "sheela"]
roles = ["sister", "mother", "daughter"]
database = []
for uid, n, r in zip(user_ids, names, roles):
    user_dict = create_user(uid, n, r)
    database.append(user_dict)
print(database)

# ── 13. CALCULATE STATS ────────────────────────────────────────
# Returns min, max and average of a list in one dictionary
# Guard clause handles empty list — avoids crashes on bad input
# min() and max() are Python built-ins — no loop needed
def calculate_stats(numbers):
    if not numbers:
        return {"min": None, "max": None, "avg": 0}
    minimum=min(numbers)
    maximum=max(numbers)
    average=get_average(numbers)
    return{
        "min":minimum,
        "max":maximum,
        "avg":average
    }
data=[10,20,30,40,50,60,70,80,90,100]
print(calculate_stats(data))

# ── 14. COUNT FREQUENCIES ─────────────────────────────────────
# Counts how many times each item appears in a list
# dict.get(key, default) — returns 0 if key doesn't exist yet
# This pattern is used in log analysis and data profiling in DE
def count_frequencies(items):
    dict={}
    for i in items:
        dict[i]=dict.get(i,0)+1
    return dict
counts=['apple','banana','mango','guava','orange','mango','apple']
print(count_frequencies(counts))

# ── 15. MERGE CONFIGS ─────────────────────────────────────────
# Merges two config dictionaries — user settings override defaults
# .copy() creates a new dict so original is not modified
# .update() adds/overwrites keys from config2 into new_config
# Real DE use case: merging default pipeline configs with env-specific ones
def merge_configs(config1,config2):
    new_config=config1.copy()
    new_config.update(config2)
    return new_config
default_settings = {
    "theme": "light",
    "font_size": 12,
    "show_notifications": True
}
user_settings = {
    "theme": "dark",        # Shared key: should overwrite "light"
    "font_size": 14,       # Shared key: should overwrite 12
    "username": "coder_42" # Unique key: should be added
}
result = merge_configs(default_settings, user_settings)
print(result)

# ── 16. INVERT MAPPING ────────────────────────────────────────
# Flips a dictionary where values are lists into item → group
# Outer loop: goes through each group
# Inner loop: goes through each item in that group's list
# Real DE use: inverting category mappings, tag lookups, label encoding
def invert_mapping(mapping):
    inverted = {}
    for group, items in mapping.items():
        for item in items:
            inverted[item] = group
    return inverted
original = {
    "group_a": [1, 2],
    "group_b": [3]
}
print(invert_mapping(original))

# ── 17. CLEAN TEXT ────────────────────────────────────────────
# Cleans raw text by lowercasing and removing special characters
# .strip() removes leading/trailing whitespace
# .lower() converts everything to lowercase
# re.sub() replaces anything that is NOT a-z, 0-9, or space with ''
# Real DE use: cleaning text columns before NLP or loading into DB
import re
def clean_text(text):
    text=text.strip().lower()
    clean_string = re.sub(r'[^a-z0-9 ]', '', text)
    return clean_string
word="i love playingCRICKET !@# 2026 %% &&"
print(clean_text(word))

# ── 18. CLEAN CURRENCY (Simple Replace Method) ────────────────
# Removes $ and , from currency strings and converts to float
# .replace() is simpler and more readable than regex for this case
# Real DE use: cleaning financial data before calculations or DB insert
def clean_currency(value_str):
    value_str=re.sub(r'[^a-z0-9 .]', '', value_str)
    value=float(value_str)
    return value
amount="$1234.5678"
print(clean_currency(amount))


def clean_currency(value_str):
    # Replace the $ and the , with nothing (an empty string)
    cleaned_str = value_str.replace("$", "").replace(",", "")
    return float(cleaned_str)
amount = "$1,234.5678"
print(clean_currency(amount))

# ── 19. FILL MISSING VALUES ───────────────────────────────────
# Replaces None values in a list of dictionaries with a fill value
# Outer loop: goes through each row (dictionary)
# Inner loop: checks every key-value pair in the row
# None check: if value is None, replace it with fill_value
# Real DE use: handling NULL values in API responses or CSV imports
def fill_missing_values(data_list,fill_value):
    for row in data_list:
        for key, value in row.items():
            if value is None:
                row[key] = fill_value
    return data_list
messy_api_data = [
    {"user": "alice", "age": 28, "status": "active"},
    {"user": "bob", "age": None, "status": "pending"},
    {"user": "charlie", "age": 35, "status": None}
]
cleaned_data = fill_missing_values(messy_api_data, "UNKNOWN")
for item in cleaned_data:
    print(item)

# ── 20. STANDARDIZE DATES ─────────────────────────────────────
# Converts dates from MM/DD/YYYY format to YYYY-MM-DD (ISO standard)
# strptime() = parses a string into a datetime object using a format
# strftime() = formats a datetime object back into a string
# %m=month, %d=day, %Y=4-digit year
# Real DE use: normalizing date formats before loading into databases
from datetime import datetime
def standardize_dates(date_list):
    clean_dates = []
    for date_str in date_list:
        parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
        new_date_str = parsed_date.strftime("%Y-%m-%d")
        clean_dates.append(new_date_str)
    return clean_dates
messy_dates = ["12/31/2023", "01/15/2024", "07/04/2024"]
print(standardize_dates(messy_dates))
