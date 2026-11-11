import re

def password_complexity(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Strong length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Moderate length (8–11 characters)")
    else:
        feedback.append("❌ Too short (<8 characters)")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✅ Contains digits")
    else:
        feedback.append("❌ Missing digits")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")

    # Final rating
    if score >= 6:
        rating = "🔒 Very Strong"
    elif score >= 4:
        rating = "🔐 Strong"
    elif score >= 2:
        rating = "⚠️ Weak"
    else:
        rating = "❌ Very Weak"

    return rating, feedback


# Example usage
pwd = input("Enter a password to check: ")
rating, details = password_complexity(pwd)

print("\nPassword Rating:", rating)
print("Details:")
for d in details:
    print("-", d)

