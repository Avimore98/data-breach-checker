# data-breach-checker
Full-stack security web app built with Python/Flask that checks email and password exposure in known data breaches using the k-Anonymity model, with a custom website-safety scoring engine and companion CLI tool.

 # Overview

Data Breach Checker is designed to give users a clear, actionable picture of their digital security — checking whether their email or password has been exposed in known data breaches, scoring the safety of websites before they enter personal information, and offering practical security guidance, all from a single dashboard.

Features
Email Breach Check
Screenshot:
<a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20155350.png">Screenshot 1</a>
<a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20155555.png">Screenshot 2</a>
<a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20155632.png">Screenshot 3</a>
<a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20155701.png">Screenshot 4</a>
                      
Users enter their email address to instantly check if it has appeared in known data breaches. Results display which breaches the email was found in, along with the breach date and type of data leaked — without ever revealing actual passwords.

Password Check
screenshot: 
<a href="https://github.com/Avimore98/data-breach-checker/commit/b377e54d37b3ef0e37b8249ef5db2d0f851db91b.png">Screenshot 5</a>
Users enter a password to check if it has been exposed in known data breaches, with a live strength meter and improvement tips (e.g., adding uppercase letters). The password is never sent or stored — only its hash is securely checked using the **k-Anonymity model**.

Advanced CLI Tool (Web-based)
screenshot:
<a href="https://github.com/Avimore98/data-breach-checker/commit/f34d6869f6353e30870adb56d034959d7270734f.png">Screenshot 6</a>
Enables bulk scanning of multiple emails and passwords at once (comma-separated), replicating the standalone CLI tool's functionality directly in the browser. Displays real-time, terminal-style output showing breach results for each entry scanned.

 Password Generator
 screenshot:
 <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20172510.png">Screenshot 7</a>
Generates strong, random passwords with customizable length and character options (uppercase, numbers, symbols) to help users create secure credentials. Includes a strength indicator and one-click copy functionality.

 Breach Library
 screenshot:
  <a href="https://github.com/Avimore98/data-breach-checker/commit/54ef833df1ee27b527d3477c8c80ffc87a609b8c.png">Screenshot 8</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20172908.png">Screenshot 9</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20172954.png">Screenshot 10</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173017.png">Screenshot 11</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173052.png">Screenshot 12</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173110.png">Screenshot 13</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173132.png">Screenshot 14</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173159.png">Screenshot 15</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173223.png">Screenshot 16</a>
A scrollable timeline showcasing major real-world data breaches (Exactis, Apollo, Canva, LinkedIn, Yahoo, and more) with dates, affected account counts, and exposed data types. Gives users context on the scale and severity of historical breaches for security awareness.

 Security Tips
  screenshot:
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173819.png">Screenshot 17</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173916.png">Screenshot 18</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20173941.png">Screenshot 19</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20174023.png">Screenshot 20</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20174045.png">Screenshot 21</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20174103.png">Screenshot 22</a>
  <a href="https://github.com/Avimore98/data-breach-checker/blob/main/Screenshot%202026-07-29%20174119.png">Screenshot 23</a>
  
A checklist of the top 10 cybersecurity best practices — including using unique passwords, enabling Two-Factor Authentication (2FA), using a password manager, and avoiding suspicious links — to help users strengthen their overall online security habits.

 Website Safety Checker
screenshot:
 <a href="https://github.com/Avimore98/data-breach-checker/commit/b3bf19b87615379ec7f380d2ce6ae70654bdc6bb.png">Screenshot 24</a>
 
Analyzes any URL for safety by checking HTTPS usage, domain reputation, phishing keywords, IP address usage, and suspicious domain extensions, then generates a 0–100 safety score. Warns users before entering personal information on risky or suspicious websites.

AI Security Assistant
An interactive chatbot that answers user questions about cybersecurity, data breaches, and online safety in real time. Provides personalized guidance and quick explanations to help users better understand and respond to security threats.

 Security Score Dashboard
Calculates an overall security score (0–100) based on the user's breach exposure and password strength, along with actionable recommendations to improve it.


Companion CLI Tool

A standalone command-line version (`cli_checker.py`) for checking email and password breaches directly via the Have I Been Pwned API, with clean terminal output and actionable security recommendations.


python cli_checker.py

Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| APIs | Have I Been Pwned, Pwned Passwords (k-Anonymity) |
| Deployment | WSGI-ready (e.g. PythonAnywhere) |

---

 Project Structure

```
data-breach-checker/
├── app.py              → Main Flask backend — handles email/password/website check routes and breach library endpoint
                           <a href="https://github.com/Avimore98/data-breach-checker/commit/19032fec7b738d875c2fb32ffb3c9e9b317a5d79</a>

├── cli_checker.py       → Standalone command-line tool for breach checking via Have I Been Pwned API
                             <a href="https://github.com/Avimore98/data-breach-checker/blob/main/cli_checker.py"</a>
├── static/
│    └── style.css        → Frontend styling — layout, colors, responsive design for dashboard, forms, and result cards
├── templates/              <a href="https://github.com/Avimore98/data-breach-checker/blob/main/style.css"</a>

│   └── index.html        → Main HTML page rendered by Flask
├── wsgi.py               → WSGI entry point for production deployment (PythonAnywhere, Gunicorn, etc.)
                          <a href="https://github.com/Avimore98/data-breach-checker/commit/aea624fa5cc24526694c1542b70731ee045b3c78"</a>
├── START_SERVER.bat      → Windows shortcut to launch the Flask server locally
├── .gitignore            → Specifies files/folders Git should ignore (cache, env files, etc.)
├── README.md             → Project documentation
└── screenshots/          → App screenshots used in this README
```
 Getting Started

Prerequisites
- Python 3.x installed
- `pip` package manager

Installation

```bash
# Clone the repository
https://github.com/Avimore98/data-breach-checker/edit/main/README.md
cd data-breach-checker

# Install dependencies
pip install flask requests

# Run the app
python app.py
```

Then open your browser and go to: `http://localhost:5000`

 Windows Quick Start
Double-click `START_SERVER.bat` to launch the server automatically. *(Note: this script uses a local file path — for portable setup on other machines, use the `pip install` + `python app.py` method above.)*

 Security & Privacy Design
- Passwords are never sent in plain text or stored — only irreversible hash prefixes are checked (k-Anonymity)
- No sensitive user data is logged or retained
- Email breach results are generated using a deterministic algorithm based on real breach metadata (not a live per-account HIBP lookup, since that endpoint requires a paid API key)


Why I Built This

To apply my interest in cybersecurity practically — building a tool that demonstrates real breach-detection concepts, secure password checking using k-Anonymity, and phishing-style URL analysis, rather than just following tutorials.


 Contact
Avinash More
avinashmore6949@gmail.com
https://www.linkedin.com/in/avinash-more

