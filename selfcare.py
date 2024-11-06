from win10toast import ToastNotifier
import time
import random

# Initialize the ToastNotifier
toaster = ToastNotifier()

def custom_reminder():
    while True:
        try:
            title = input("\nTitle of Reminder: ")
            msg = input("Message: ")
            minutes = float(input("How Many Minutes (0 to cancel): "))

            if minutes == 0:
                print("Reminder canceled.\n")
                break

            seconds = minutes * 60
            print("\nReminder Set Successfully!\n")
            time.sleep(seconds)
            toaster.show_toast(title, msg, duration=10, threaded=False)

            while toaster.notification_active():
                time.sleep(0.1)
        except ValueError:
            print("Please enter a valid number for minutes.")

def workday_reminder():
    positive_phrases = [
    "You're doing great!",
    "Keep up the good work!",
    "Remember, it's okay to ask for help.",
    "You're making amazing progress!",
    "Don't forget to take a break!",
    "Stay positive and productive!",
    "Your efforts are paying off!",
    "You inspire others with your dedication.",
    "Success is a journey, and you're on the right track!",
    "Embrace challenges, they help you grow!",
    "Your hard work is an example for others.",
    "Small steps every day lead to big achievements.",
    "You're capable of reaching new heights!",
    "Persistence is your ally in success.",
    "Always proud of your accomplishments!",
    "You're turning obstacles into opportunities!",
    "Today is another chance to shine!",
    "You have the power to create change.",
    "Every day is progress. Keep going!",
    "Believe in yourself and your potential!"
]
    total_work_minutes = 480
    reminder_interval = 60  # Interval in minutes

    total_work_seconds = total_work_minutes * reminder_interval

    print("Work reminders will pop up every hour for 8 hours with positive phrases.\n")

    start_time = time.time()

    while (time.time() - start_time) < total_work_seconds:
        title = "Work Reminder"
        msg = random.choice(positive_phrases)

        toaster.show_toast(title, msg, duration=10, threaded=False)

        time.sleep(reminder_interval * 60)  # Wait for next interval

        while toaster.notification_active():
            time.sleep(0.1)

    print("The work reminder session is over.")

if __name__ == "__main__":
    choice = input("Choose reminder type:\n1. Custom Reminder\n2. Work Day Reminder\nEnter your choice (1/2): ")

    if choice == '1':
        custom_reminder()
    elif choice == '2':
        workday_reminder()
    else:
        print("Invalid choice! Please enter 1 or 2.")