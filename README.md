# 🏦 CLOUDBANKX - Secure Banking System

A modern, professional banking application built with Flask where users can register, login, and manage multiple bank accounts with transfers, deposits, and withdrawals.

## ✨ Features

### Authentication System
- **User Registration** - Create new accounts with email validation
- **Secure Login** - Session-based authentication with password verification
- **Flash Messages** - Real-time feedback for all user actions (success/error)
- **Session Management** - Persistent sessions for logged-in users
- **Logout** - Secure session termination

### Banking Features (After Login)
- **Multiple Accounts** - Checking, Savings, Investment accounts per user
- **View Balances** - Real-time account balance display
- **Money Transfer** - Transfer funds between own accounts
- **Deposits** - Add money to accounts
- **Withdrawals** - Withdraw money from accounts
- **Transaction History** - Complete record of all transactions with timestamps
- **User Profile** - View account information and settings

### Security Features
- Session-based authentication
- Password validation (min 6 characters)
- Login-required access to banking features
- Secure logout functionality

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. Navigate to the project directory:
```bash
cd Banking
```

2. Install Flask if not already installed:
```bash
pip install flask
```

### Running the Application

```bash
python app.py
```

The app will start at `http://127.0.0.1:5000`

## 📝 Usage Guide

### 1. Create an Account (Sign Up)
- Go to http://127.0.0.1:5000/signup
- Enter username (min 3 characters)
- Enter valid email address
- Enter password (min 6 characters)
- Confirm password
- Click "Create Account"
- You'll see a success message and be redirected to login

### 2. Login
- Go to http://127.0.0.1:5000/ (or login page)
- Enter your username
- Enter your password
- Click "Login"
- Success message displays and you're taken to the banking dashboard

### 3. Use Banking Features

#### View Dashboard
- **URL**: `/dashboard`
- Shows total balance across all accounts
- Quick action buttons for common operations
- Overview of all your accounts

#### View All Accounts
- **URL**: `/accounts`
- See all your accounts (Checking, Savings, Investment)
- Check individual account numbers and balances
- Quick links to transfer, deposit, or withdraw

#### View Account Details
- **URL**: `/account/<account_type>`
- See account-specific balance
- View complete transaction history
- Perform account-specific operations

#### Transfer Money
- **URL**: `/transfer`
- Select source and destination accounts
- Enter amount to transfer
- Complete the transaction
- See confirmation with transaction details

#### Deposit Money
- **URL**: `/deposit`
- Select account to deposit into
- Enter deposit amount
- Confirm deposit
- View transaction confirmation

#### Withdraw Money
- **URL**: `/withdraw`
- Select account to withdraw from
- Enter withdrawal amount
- Confirm withdrawal
- View transaction confirmation

#### Profile & Settings
- **URL**: `/profile`
- View your profile information
- See account creation date
- Access logout button

#### Logout
- **URL**: `/logout`
- Securely logs you out
- Clears your session
- Returns to login page

## 📁 Project Structure

```
Banking/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── users.json                  # User credentials (auto-generated)
├── accounts.json              # User bank accounts (auto-generated)
├── transactions.json          # Transaction history (auto-generated)
│
├── Templates/
│   ├── login.html             # Login page with flash messages
│   ├── signup.html            # Registration page with validation
│   ├──dashboard.html # Main dashboard after login
│   ├── accounts.html          # All accounts overview
│   ├── NRI.html               # For NRI user supports
│   ├── corporate.html         
│   ├── contact.html           # Deposit form
│   ├── personal_banking.html  #User account summary
│   ├── transaction.html  # Transaction confirmation
│   ├── profile.html           # User profile page
│   ├── home.html            
│   └── dashboard.html         # Legacy dashboard
│
└── static/
    └── style.css              # Modern, responsive styling
```

## 🔐 Test Credentials

After creating an account, use those credentials to login. 

**Example:**
- Username: `testuser`
- Email: `test@example.com`
- Password: `password123`

## 💾 Data Storage

The application stores data in JSON files:

- **users.json** - User accounts and passwords
- **accounts.json** - Bank accounts and balances
- **transactions.json** - Transaction records

These files are auto-generated when users register.

## 🎨 UI/UX Features

- **Modern Design** - Purple gradient theme with smooth animations
- **Responsive Layout** - Works on desktop, tablet, and mobile
- **Flash Messages** - Visual feedback for all actions (success/error)
- **Intuitive Navigation** - Easy access to all banking features
- **Interactive Elements** - Hover effects and smooth transitions
- **Professional Styling** - Card-based layouts with consistent spacing

## 🔄 User Flow

```
Login Page
    ↓
[Create Account?] → Signup Page → Validation → Create Account → Back to Login
    ↓ (No)
[Valid Credentials?] → Dashboard
    ↓ (Yes)
┌─────────────────────────────────────┐
│ Banking Dashboard                   │
│ - View Accounts                     │
│ - Transfer Money                    │
│ - Deposit                           │
│ - Withdraw                          │
│ - View Transaction History          │
│ - Profile Settings                  │
│ - Logout                            │
└─────────────────────────────────────┘
```

## ⚙️ Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS Templates
- **Data Storage**: JSON files
- **Authentication**: Flask Sessions
- **Styling**: Custom CSS with gradients and animations

## 🚨 Error Handling

The application provides clear error messages for:
- Missing or invalid login credentials
- Duplicate usernames
- Invalid email formats
- Password mismatch
- Insufficient balance
- Invalid amounts
- Missing form fields

## 📋 Features in Detail

### Session Management
- Automatically logs in users after successful authentication
- Maintains session state across pages
- Protects banking features with login checks
- Secure logout functionality

### Input Validation
- Username length validation (min 3 chars)
- Email format validation
- Password strength validation (min 6 chars)
- Password confirmation matching
- Amount validation for transactions

### Data Persistence
- User data saved in users.json
- Account data saved in accounts.json
- All transactions logged in transactions.json
- Data persists across application restarts

## 🎯 Next Steps

To extend this application, consider:
- Database integration (SQLite, PostgreSQL)
- Password hashing (werkzeug.security)
- Two-factor authentication
- Transaction filters and search
- Bill payments
- Loan management
- Investment portfolio tracking
- Mobile app version

## 📞 Support

For issues or questions, check:
- User validation messages in forms
- Flash messages after actions
- Terminal output for Flask errors
- JSON files for data integrity

---

**Made with ❤️ | CLOUDBANKX | 2026**
