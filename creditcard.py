import re

def is_valid_credit_card(card_number):
  """
  This function checks if a credit card number is valid based on ABCD Bank's criteria.

  Args:
      card_number: The credit card number to be validated (string).

  Returns:
      "Valid" if the card number is valid, otherwise "Invalid".
  """
  pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?|[56][0-9]{14})$"
  if not re.match(pattern, card_number):
    return "Invalid"
  
  # Check for consecutive repeated digits (4 or more)
  for i in range(1, 10):
    repeated_digit = str(i) * 4
    if repeated_digit in card_number:
      return "Invalid"
  
  # Check for separators other than '-'
  if re.search(r"[^\d-]", card_number):
    return "Invalid"
  
  return "Valid"

# Get the number of test cases
num_tests = int(input())

# Loop through each test case
for _ in range(num_tests):
  card_number = input()
  result = is_valid_credit_card(card_number)
  print(result)
