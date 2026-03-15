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