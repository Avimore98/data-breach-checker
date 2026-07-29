import hashlib
import requests
import os
import sys

HIBP_API_KEY = os.environ.get('HIBP_API_KEY', '')
HEADERS = {
    'User-Agent': 'DataBreachChecker-CLI',
    'hibp-api-key': HIBP_API_KEY
}

def print_banner():
    print("=" * 60)
    print("  🛡️  DATA BREACH CHECKER")
    print("=" * 60)
    print()

def check_email_breach(email):
    """Check if email has been in data breaches using Have I Been Pwned API"""
    print(f"\n📧 Checking email: {email}...")
    print("-" * 60)
    
    if not HIBP_API_KEY:
        print("❌ ERROR: HIBP_API_KEY not set!")
        print("   Get free API key from: https://haveibeenpwned.com/API/Key")
        print("   Then run: set HIBP_API_KEY=your_key")
        return
    
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code == 404:
            print("✅ GREAT NEWS!")
            print("   Your email was NOT found in any data breaches.")
            print("   You're safe! 🎉")
            
        elif response.status_code == 200:
            breaches = response.json()
            print(f"⚠️  ALERT! Your email was found in {len(breaches)} breach(es)!\n")
            
            for i, breach in enumerate(breaches, 1):
                print(f"  📌 Breach #{i}: {breach.get('Title', 'Unknown')}")
                print(f"     Domain: {breach.get('Domain', 'N/A')}")
                print(f"     Date: {breach.get('BreachDate', 'N/A')}")
                print(f"     Accounts affected: {breach.get('PwnCount', 0):,}")
                print(f"     Data leaked: {', '.join(breach.get('DataClasses', []))}")
                print()
            
            print("🔐 RECOMMENDED ACTIONS:")
            print("   1. Change passwords on all affected services")
            print("   2. Enable Two-Factor Authentication (2FA)")
            print("   3. Use a unique password for each account")
            print("   4. Consider a password manager (Bitwarden, 1Password)")
            
        elif response.status_code == 401:
            print("❌ Invalid API Key! Please check your HIBP_API_KEY.")
        elif response.status_code == 429:
            print("⏳ Rate limit exceeded. Please wait a minute and try again.")
        else:
            print(f"❌ API Error (Status: {response.status_code})")
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Check your internet connection.")
    except requests.exceptions.ConnectionError:
        print("❌ No internet connection. Please check your network.")
    except Exception as e:
        print(f"❌ Error: {e}")

def check_password_breach(password):
    """Check if password has been in data breaches using k-Anonymity"""
    print(f"\n🔑 Checking password...")
    print("-" * 60)
    print("🔒 Security: Using k-Anonymity - only first 5 chars of hash sent")
    print()
    
    try:
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, headers={'User-Agent': 'DataBreachChecker-CLI'}, timeout=10)
        
        if response.status_code == 200:
            hashes = response.text.splitlines()
            found_count = 0
            
            for h in hashes:
                parts = h.split(':')
                if len(parts) == 2 and parts[0] == suffix:
                    found_count = int(parts[1])
                    break
            
            if found_count > 0:
                print(f"⚠️  DANGER! This password has been exposed {found_count:,} times!")
                print("   It is NOT safe to use. Change it immediately!")
            else:
                print("✅ This password has NOT been found in any known breaches.")
                print("   But make sure it's strong and unique!")
        else:
            print("❌ Unable to check password. Try again later.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print_banner()
    
    print("Choose an option:")
    print("  1. Check Email Breach")
    print("  2. Check Password Breach")
    print("  3. Exit")
    print()
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == '1':
        email = input("\nEnter your email address: ").strip()
        if email:
            check_email_breach(email)
        else:
            print("❌ Email cannot be empty!")
    
    elif choice == '2':
        import getpass
        password = getpass.getpass("\nEnter your password (hidden): ").strip()
        if password:
            check_password_breach(password)
        else:
            print("❌ Password cannot be empty!")
    
    elif choice == '3':
        print("\n👋 Stay safe online!")
        sys.exit(0)
    
    else:
        print("❌ Invalid choice!")

    print("\n" + "=" * 60)

if __name__ == '__main__':
    main()
