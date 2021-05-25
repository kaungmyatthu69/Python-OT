import secrets
print("Printing inter number using secrets mudule >")
passwordrestlink="https://kaung.com/codercrazy/reset="
passwordrestlink+=secrets.token_urlsafe(12)
print("Generating secure URL",passwordrestlink)