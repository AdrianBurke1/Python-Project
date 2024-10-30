from turtle import title
from win10toast import ToastNotifier
import time 

toaster = ToastNotifier()

title = input("\nTitle of Remainder: ")
msg = input("Message: ")
minutes = float(input("How Many Minutes: "))
# # Total workday duration in seconds (8 hours)
# WORKDAY_DURATION = 8 * 60 * 60
# # Break interval in seconds (e.g., every 1 hour)
# BREAK_INTERVAL = 60 * 60

# def remind_to_take_break():
#     notification.notify(
#         title="Time to Take a Break!",
#         message="Remember to stretch, relax your eyes, and drink water.",
#         timeout=10  # Notification stays for 10 seconds
#     )

# def start_reminder():
#     start_time = time.time()  # Record the start time
#     elapsed_time = 0

#     while elapsed_time < WORKDAY_DURATION:
#         time.sleep(BREAK_INTERVAL)  # Wait for the break interval
#         remind_to_take_break()      # Show notification

#         elapsed_time = time.time() - start_time  # Update elapsed time

# if __name__ == "__main__":
#     start_reminder()
