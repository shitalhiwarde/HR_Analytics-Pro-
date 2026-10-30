from hr_chatbot import ask_hr_ai

question = "How many employees left the company and what is the attrition rate?"

answer = ask_hr_ai(question)

print("HR AI Answer:")
print(answer)