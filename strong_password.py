import random
import string

class PasswordManager:
    def __init__(self):
        self.min_length = 8
        self.suggested_length = 12

    def check_password_strength(self, password):
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        if (has_lower and has_upper and has_digit and has_special and n >= self.min_length):
            return "Strong"
        elif (n >= 6 and (has_lower or has_upper) and has_special):
            return "Moderate"
        else:
            return "Weak"

    def suggest_strong_password(self, length=None):
        if length is None or length < self.min_length:
            length = self.suggested_length

        characters = (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits +
            string.punctuation
        )
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        password += random.choices(characters, k=length - 4)
        random.shuffle(password)
        return ''.join(password)

    def run(self):
        while True:
            user_password = input("Enter your password (or type 'no' to exit): ")
            if user_password.lower() == 'no':
                print("Exiting the program.")
                break
            strength = self.check_password_strength(user_password)
            print(f"Password strength: {strength}")
            if strength != "Strong":
                print("Suggested strong password:", self.suggest_strong_password())

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.run()
