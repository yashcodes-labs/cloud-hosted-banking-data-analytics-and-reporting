# 🚀 CLOUDBANKX - Quick Start Guide

## Installation & Setup (60 seconds)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: **http://127.0.0.1:5000**

---

## 👤 Complete User Journey

### ✅ Step 1: Create Account (Sign Up)
1. Click **"Create one here"** on login page
2. Fill in the form:
   - **Username**: `john_doe` (min 3 characters)
   - **Email**: `john@example.com`
   - **Password**: `SecurePass123` (min 6 characters)
   - **Confirm Password**: `SecurePass123`
3. Click **"Create Account"**
4. ✓ See success message: "Account created successfully! Please login."

### ✅ Step 2: Login to Banking
1. Enter your **Username**: `john_doe`
2. Enter your **Password**: `SecurePass123`
3. Click **"Login"**
4. ✓ See welcome message: "Welcome back, john_doe! 👋"
5. ✓ Redirected to **Banking Dashboard**

### ✅ Step 3: View Your Accounts
You now have 3 accounts automatically created:
- **Checking Account** - ₹5,000
- **Savings Account** - ₹10,000
- **Investment Account** - ₹15,000
- **Total Balance** - ₹30,000

### ✅ Step 4: Transfer Money Between Accounts
1. Click **"Transfer"** (or go to `/transfer`)
2. Select **From Account**: Checking (₹5,000)
3. Select **To Account**: Savings
4. Enter **Amount**: 1000
5. Click **"Complete Transfer"**
6. ✓ See success confirmation with details

### ✅ Step 5: Deposit Money
1. Click **"Deposit"** (or go to `/deposit`)
2. Select **Account**: Checking
3. Enter **Amount**: 2000
4. Click **"Deposit"**
5. ✓ Deposit confirmed and balance updated

### ✅ Step 6: Withdraw Money
1. Click **"Withdraw"** (or go to `/withdraw`)
2. Select **Account**: Savings
3. Enter **Amount**: 500
4. Click **"Withdraw"**
5. ✓ Withdrawal confirmed

### ✅ Step 7: View Transaction History
1. Go to **Accounts** (or `/accounts`)
2. Click **"View Details →"** on any account
3. ✓ See all transactions with timestamps
4. ✓ Shows transaction type (Deposit, Withdrawal, Transfer)
5. ✓ Shows amounts and descriptions

### ✅ Step 8: View Profile
1. Click **"Profile"** in navigation
2. ✓ View your username and email
3. ✓ See member since date
4. Click **"Logout"** to logout

---

## 🧪 Test Scenarios

### Scenario 1: Invalid Credentials
1. Try login with wrong password
2. ✓ Error message: "Invalid username or password"
3. Redirected back to login

### Scenario 2: Duplicate Username
1. Try signup with existing username
2. ✓ Error message: "Username already exists"
3. Redirected back to signup

### Scenario 3: Password Mismatch
1. Enter different passwords in signup
2. ✓ Error message: "Passwords do not match"
3. Redirected back to signup

### Scenario 4: Insufficient Balance
1. Try to withdraw more than account balance
2. ✓ Error message: "Insufficient balance"
3. Stay on withdraw page

### Scenario 5: Invalid Email
1. Enter email without "@" symbol
2. ✓ Error message: "Valid email address is required"
3. Redirected back to signup

---

## 📱 Navigation Guide

### Public Pages (Before Login)
- `/` - Login page
- `/login` - Login page (POST)
- `/signup` - Sign up page

### Protected Pages (After Login)
- `/dashboard` - Main banking dashboard
- `/accounts` - View all accounts
- `/account/<type>` - View specific account (checking/savings/investment)
- `/transfer` - Transfer between accounts
- `/deposit` - Deposit money
- `/withdraw` - Withdraw money
- `/profile` - User profile & settings
- `/logout` - Logout

---

## 💡 Key Features Explained

### Flash Messages
- **Green (Success)**: ✓ Account created, transaction completed
- **Red (Error)**: ✗ Invalid credentials, validation error

### Account Types
1. **Checking** - Day-to-day transactions
2. **Savings** - Save money with interest
3. **Investment** - Long-term growth

### Transaction Tracking
- Every action creates a transaction record
- Includes timestamp, amount, type, and description
- View complete history per account

### Session Management
- Automatically logs you in after login
- Remembers you across page refreshes
- Logs you out when you click logout

---

## 🔐 Security Notes

⚠️ **Development Mode Only**
- This is a development application
- Passwords are stored in plain text (use hashing in production)
- Not suitable for real banking (missing encryption, security measures)

✅ **For Production:**
- Use password hashing (werkzeug.security)
- Use proper database (PostgreSQL, MongoDB)
- Enable HTTPS
- Add 2-factor authentication
- Use proper session management
- Add rate limiting

---

## 🐛 Troubleshooting

### App won't start
```bash
# Make sure Flask is installed
pip install flask

# Run again
python app.py
```

### Port 5000 already in use
```bash
# Use different port
python -c "from app import app; app.run(port=5001)"
```

### Lost session after refresh
- This is normal - login again
- Add database persistence for better session management

### JSON files not created
- They're created automatically on first signup/login
- Check `users.json`, `accounts.json`, `transactions.json`

---

## 📊 Project Statistics

- **Total Pages**: 12 HTML templates
- **Routes**: 25+ Flask routes
- **Features**: 8 core banking features
- **Responsive**: Mobile, tablet, desktop
- **Lines of Code**: 400+ backend + 800+ templates

---

## 🎓 Learning Resources

This project demonstrates:
- ✅ Flask web framework basics
- ✅ Session management and authentication
- ✅ HTML form handling
- ✅ Template inheritance (Jinja2)
- ✅ JSON file handling
- ✅ User input validation
- ✅ Flash messages
- ✅ Responsive CSS design

---

## 📝 File Summary

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with all routes |
| `requirements.txt` | Python dependencies |
| `users.json` | User accounts (auto-created) |
| `accounts.json` | Bank accounts data (auto-created) |
| `transactions.json` | Transaction history (auto-created) |
| `Templates/` | HTML templates for all pages |
| `static/style.css` | CSS styling |

---

## 🎉 You're All Set!

Your banking system is ready to use. Start with creating an account and explore all features!

**Enjoy the CLOUDBANKX experience! 🏦**

---

Need help? Check the detailed README.md file!
