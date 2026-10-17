from task_planner import decompose_task


user_request = (
    "Get the current time, generate a secure password, and explain make workout plan Python after the make a list of buying groceries, ."
)


tasks = decompose_task(user_request)


print("\nTask Plan")
print("---------")

for task in tasks:
    print("-", task)
