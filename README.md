# 🛡️ IDS-Dashboard: Real-Time Python Intrusion Detection System

A modular, real-time Intrusion Detection System (IDS) with a live GUI dashboard. Built using Python, it detects common cyberattack patterns like SQL Injection, XSS, Command Injection, and Brute-force login attempts. Alerts are displayed in a scrollable GUI built with Tkinter.

---

## 📌 Project Objective

To simulate a basic real-time IDS that:
- Receives and inspects messages over a network socket
- Detects potential attack patterns using regex
- Displays alerts instantly in a clean, readable GUI
- Tracks repeated login failures to simulate brute-force detection

---

## 🧱 Project Structure

IDS-Dashboard/
├── ids_server.py ← Main IDS logic (server + GUI + detection)
├── dashboard.py ← Tkinter-based alert GUI
├── client_test.py ← Fake attacker / message sender
├── README.md ← You're reading this!
└── .gitignore ← Ignores cache, logs, etc.

---

## 🚀 How It Works

### 1. `ids_server.py`
- Starts a socket server on port `9999`
- Spawns threads to handle multiple clients
- Checks incoming messages against 3 attack patterns:
  - SQL Injection
  - XSS
  - Command Injection
- Monitors repeated `"login failed"` messages to detect brute-force
- Sends alerts to the dashboard

### 2. `dashboard.py`
- Launches a GUI using `tkinter`
- Shows timestamped alerts
- Keeps track of total alerts triggered

### 3. `client_test.py`
- Connects to the IDS as a simulated attacker
- Lets you manually type test messages
- Sends them to the server over TCP

---

## 🎯 Attack Patterns Detected

| Type         | Trigger Examples |
|--------------|------------------|
| **SQL Injection** | `DROP TABLE`, `SELECT * FROM users`, `--` |
| **XSS**           | `<script>`, `alert(1)`, `onerror=` |
| **Command Injection** | `; ls`, `&& whoami`, `` `rm -rf /` `` |
| **Brute-force Login** | More than 5 "login failed" messages |

---

## 📥 How to Run (Step-by-Step)

### ✅ 1. Open Terminal in the Project Folder

If your folder is at:
D:\arjun\IDS-Dashboard\
Run:
```bash
  cd /d/arjun/IDS-Dashboard
Or right-click the folder and select Git Bash Here
 Start the IDS + Dashboard
python ids_server.py