"""
Function for returning data to the logfile
"""
import os
import datetime

def log_action(session, quiz_location, action_type, parameters):
    """Output actions to the logfile
    @session: ID value for the current session of the experiment
    @quiz_location: Used to identify Question start and question number for the action
    @action_type: Used to identify the type of action performed
    @parameters: Extra information about the action (such as answer or correctness)
    """

    # Should the logfile not exist, create it
    if not os.path.exists("logfile.csv"):
        create_log_file()

    # Write input to logfile
    with open("logfile.csv", "a") as file:
        file.write(f"\n{session}, {datetime.datetime.now()}, {quiz_location}, {action_type}, ")

        for param in parameters:
            file.write(f"{param}; ")

    file.close()

def create_log_file():
    """Function to create the logfile should it not exist"""
    with open("logfile.csv", "w") as file:
        file.write("Session, Timestamp, Quiz_location, Action_type, parameters")

    file.close()

# For testing purposes
# log_action(123, "QUESTION_2", "HOVER", ["answer=B"])
