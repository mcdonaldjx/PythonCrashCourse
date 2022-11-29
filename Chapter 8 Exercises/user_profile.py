#Created 11/29/2022 by Jared
#Exercise 8-13- User Profile: Start with a copy of user_profile.py on page 148. Build a profile of yourself by calling build_profile(), using your first and last name and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info
user_profile = build_profile('jared', 'm', location='texas', favorite_color='red', field='computer science')
print(user_profile)
