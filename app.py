from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from data import load_data, save_data
from datetime import datetime
import random


app = Flask(__name__)
app.secret_key = "bank_secret_key"


# ✅ Secure Login Users (hashed)
users = {
    "admin": generate_password_hash("1234"),
    "user1": generate_password_hash("pass123")
}


# ---------------- HELPER FUNCTIONS ----------------

def parse_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            return None
        return round(amount, 2)
    except ValueError:
        return None


def calculate_analytics(transactions):
    total_deposit = sum(t["amount"] for t in transactions if t["type"] == "Deposit")
    total_withdraw = sum(t["amount"] for t in transactions if t["type"] == "Withdraw")

    return total_deposit, total_withdraw, total_deposit - total_withdraw


def ensure_user_profile(users_data, username):
    """
    Auto-upgrade OLD users.
    Prevents dashboard crash.
    """
    user = users_data[username]

    if "account_number" not in user:
        user.update({
            "name": username,
            "account_number": random.randint(100000000000, 999999999999),
            "account_type": "Savings",
            "branch":"CBX0001234",
            "balance": user.get("balance", 1000.0),
            "transactions": user.get("transactions", [])
        })

        save_data(users_data)

    return user


# ---------------- HOME ----------------

@app.route("/")
def login_page():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html", user=session.get("user"))


# ---------------- LOGIN ----------------

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and check_password_hash(users[username], password):
        session["user"] = username
        return redirect(url_for("dashboard"))

    return "Invalid Username or Password"


# ---------------- SIGNUP ----------------

@app.route("/signup", methods=["GET", "POST"])
def signup_page():

    if request.method == "GET":
        return render_template("signup.html")

    username = request.form["username"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    if password != confirm_password:
        return "Passwords do not match"

    users_data = load_data()

    if username in users_data:
        return "User already exists"

    # ✅ Create FULL bank profile
    users_data[username] = {
        "name": username,
        "account_number": random.randint(100000000000, 999999999999),
        "account_type": "Savings",
        "branch": "CloudBankX Main Branch",
        "ifsc": "CBX0001234",
        "balance": 1000.00,
        "transactions": []
    }

    save_data(users_data)

    # Store hashed password
    users[username] = generate_password_hash(password)

    return redirect(url_for("login_page"))


# ---------------- DASHBOARD (PROFILE) ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login_page"))

    username = session["user"]
    users_data = load_data()

    user_data = ensure_user_profile(users_data, username)

    return render_template(
        "dashboard.html",
        user_data=user_data
    )


# ---------------- PERSONAL BANKING ----------------

@app.route("/personal-banking")
def personal_banking():

    if "user" not in session:
        return redirect(url_for("login_page"))

    username = session["user"]
    users_data = load_data()

    user = ensure_user_profile(users_data, username)

    transactions = user["transactions"]
    balance = user["balance"]

    total_deposit, total_withdraw, net_change = calculate_analytics(transactions)

    return render_template(
        "personal_banking.html",
        user=username,
        balance=balance,
        total_deposit=total_deposit,
        total_withdraw=total_withdraw,
        net_change=net_change,
        transactions=transactions
    )


# ---------------- DEPOSIT ----------------

@app.route("/deposit", methods=["POST"])
def deposit():

    if "user" not in session:
        return redirect(url_for("login_page"))

    username = session["user"]
    amount = parse_amount(request.form["amount"])

    if amount is None:
        return "Invalid amount"

    users_data = load_data()
    user = ensure_user_profile(users_data, username)

    user["balance"] += amount

    user["transactions"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "Deposit",
        "amount": amount,
        "balance": user["balance"]
    })

    save_data(users_data)

    return redirect(url_for("personal_banking"))


# ---------------- WITHDRAW ----------------

@app.route("/withdraw", methods=["POST"])
def withdraw():

    if "user" not in session:
        return redirect(url_for("login_page"))

    username = session["user"]
    amount = parse_amount(request.form["amount"])

    if amount is None:
        return "Invalid amount"

    users_data = load_data()
    user = ensure_user_profile(users_data, username)

    if user["balance"] < amount:
        return "Insufficient Balance"

    user["balance"] -= amount

    user["transactions"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "Withdraw",
        "amount": amount,
        "balance": user["balance"]
    })

    save_data(users_data)

    return redirect(url_for("personal_banking"))


# ---------------- TRANSACTIONS ----------------

@app.route("/transactions")
def transactions():

    if "user" not in session:
        return redirect(url_for("login_page"))

    username = session["user"]
    users_data = load_data()

    user = ensure_user_profile(users_data, username)

    return render_template(
        "transactions.html",
        user=username,
        transactions=user["transactions"]
    )


# ---------------- OTHER PAGES ----------------

@app.route("/corporate")
def corporate():
    return render_template("corporate.html")


@app.route("/nri")
def nri():
    return render_template("nri.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))


# ---------------- RUN ----------------

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=5000, debug=True)
