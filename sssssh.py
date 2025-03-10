while True:
	user = input("Please enter your age (or type 'exit' to quit): ")
	
	if user == "exit":
		print("Goodbye!")
		break
		
	try:
		age = int(user)
		
		if age <=0:
			print("Invalid age. Please enter a non-negative number.")
		elif age <= 12:
			print(f"Age = You are a Child.")
		elif age <= 19:
			print(f"Age = You are a Teen.")
		elif age <= 64:
			print(f"Age = You are a Adult.")
		else:
			print(f"Age = You are a Senior.")
			
	except:
		print("Invalid input. Please enter a valid number or type 'exit' to quit.")