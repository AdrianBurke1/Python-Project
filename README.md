Self-Care Reminder Project
This project is a self-care reminder application developed in Python. It utilizes the win10toast package to display Windows toast notifications for periodic self-care reminders. The application offers two types of reminders: Custom Reminder and Workday Reminder, which are designed to help users stay on track with their self-care practices throughout the day.
Features
1. Custom Reminder
The Custom Reminder feature allows users to set a specific reminder message that will trigger after a specified number of minutes. Users can define:
* Title: The title of the reminder.
* Message: A custom message for the notification.
* Time Interval: The duration (in minutes) after which the reminder will appear.
2. Workday Reminder
The Workday Reminder feature provides positive messages at regular intervals throughout the workday. By default:
* The total workday is set to 8 hours (480 minutes).
* Reminders appear every 60 minutes (1 hour) with random encouraging phrases to help maintain productivity and positivity.
Example Positive Phrases:
* "You're doing great!"
* "Keep up the good work!"
* "Remember, it's okay to ask for help."
* "Stay positive and productive!"
Installation
Prerequisites
* Python 3.x installed on your machine.
* win10toast package for Windows notifications.
Setup
1. Clone the repository or download the project files.
2. Navigate to the project folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install the required package:bash Copy code   pip install win10toast
5.   
Using .gitignore
To exclude specific files and folders from version control, a .gitignore file is provided. Make sure to add virtual environment folders and other generated files you don’t want to commit to the repository.
Usage
1. Run the Application: bash Copy code   python selfcare.py
2.   
3. Choose Reminder Type:
    * Enter 1 for Custom Reminder.
    * Enter 2 for Workday Reminder.
Example Workflow
* For Custom Reminder: You will be prompted to enter a title, message, and duration in minutes. The application will display a toast notification after the specified time.
* For Workday Reminder: The application will display positive messages at one-hour intervals for an 8-hour workday.
Code Structure
* selfcare.py: Contains the main logic for setting reminders.
* win10toast: Handles Windows toast notifications.
* README.md: Documentation for understanding and running the project.
Customization
You can customize the following variables in the selfcare.py file:
* total_work_minutes: Adjusts the length of the workday.
* reminder_interval: Changes the interval between reminders in the workday reminder feature.
Dependencies
* win10toast: For displaying toast notifications in Windows.
Install dependencies with:
bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License. See the LICENSE file for details.

This README provides a comprehensive overview of the project, installation, usage, and customization options. Let me know if you'd like to add or adjust any details.

