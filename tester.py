import complice

# Replace with your auth_token
auth_token = "i8hny6mwdyanrmy6arw9"

api = complice.CompliceAPI(auth_token)

# Test individual functions here
# Example: print(api.get_userinfo())

print(api.get_intentions())
