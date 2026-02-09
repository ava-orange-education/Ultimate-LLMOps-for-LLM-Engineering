# Usage
context = "Our product costs $99/month and includes 24/7 support."
response = "The product is priced at $99 monthly with round-the-clock support."
is_grounded, message = check_groundedness(response, context)
print(message)