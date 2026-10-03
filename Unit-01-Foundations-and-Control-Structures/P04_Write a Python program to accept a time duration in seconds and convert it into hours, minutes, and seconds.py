seconds = int(input("Enter time duration in seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)

Enter time duration in seconds: 3665
Hours: 1
Minutes: 1
Seconds: 5
