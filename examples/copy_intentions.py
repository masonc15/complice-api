import complice
import pyperclip


# Replace with your auth_token
auth_token = "i8hny6mwdyanrmy6arw9"

api = complice.CompliceAPI(auth_token)

intentions = api.get_intentions(strip_goal_num=True)

# create string variable intention_str that is a multiline string with item of intentions on a new line
intention_str = ''
for item in intentions:
    intention_str += item + '\n'

# Copy intention_str to the macOS clipboard
pyperclip.copy(intention_str)
print('Copied intentions to clipboard')
