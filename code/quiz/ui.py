import uuid
import datetime
from tkinter import Tk, Label, Canvas, StringVar, Radiobutton, Button

from PIL import ImageTk, Image
from action_logging.action_logger import log_action


class QuizUI:
    """User interface for the quiz"""

    def __init__(self, controller) -> None:

        # Define session (lazy solution)
        self.session = uuid.uuid4()
        # Controller for the quiz
        self.controller = controller
        # Setup for window
        self.window = Tk()
        self.window.title("Information Vis coursework 2 Experiment")
        self.window.geometry("1200x700")

        # Create area for questions
        self.canvas = Canvas(self.window, width=1200, height=720)
        self.question_text = self.canvas.create_text(540, 25,
                                                     text="Question here",
                                                     width=680,
                                                     fill="#375362",
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Display graphs

        img1 = ImageTk.PhotoImage(Image.open(self.controller.current_question.image_path1))
        self.image1 = self.canvas.create_image(300, 270, image=img1)
        # self.canvas.grid(column=2, row=2)

        img2 = ImageTk.PhotoImage(Image.open(self.controller.current_question.image_path2))
        self.image2 = self.canvas.create_image(900, 270, image=img2)



        # Create StringVar to store user choice
        self.user_choice = StringVar()

        # Create buttons for answers
        self.answers = self.answer_buttons()
        self.display_answer_btns()

        # Create next button
        next_button = Button(self.window, text="Submit", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # palcing the button on the screen
        next_button.place(x=510, y=650)

        # Run main loop
        self.window.mainloop()

    def display_title(self):
        """To display title"""

        title = Label(self.window, text="Line vs Area charts",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def display_question(self):
        """Function to display the question"""

        text = self.controller.next_question()
        self.canvas.itemconfig(self.question_text, text=text)

    def update_graphs(self):
        global img1
        global img2

        img1 = ImageTk.PhotoImage(Image.open(self.controller.current_question.image_path1))
        self.canvas.itemconfig(self.image1, image=img1)

        img2 = ImageTk.PhotoImage(Image.open(self.controller.current_question.image_path2))
        self.canvas.itemconfig(self.image2, image=img2)

    def answer_buttons(self):
        """Function to create answer buttons"""

        # Empty list to store answer buttons
        answers = []

        # Position of first option
        x_pos = 510

        # Create button for each answer
        while len(answers) < 2:
            radio_btn = Radiobutton(self.window,
                                    text="",
                                    variable=self.user_choice,
                                    value='',
                                    font=("ariel", 14))

            # Add new button to list of answers
            answers.append(radio_btn)

            radio_btn.place(x=x_pos, y=600)

            x_pos = x_pos + 100

        return answers

    def display_answer_btns(self):
        """Display two buttons"""

        val = 0

        # Deselecting all buttons
        self.user_choice.set(None)

        for choice in self.controller.current_question.choices:
            self.answers[val]["text"] = choice
            self.answers[val]["value"] = choice
            val = val + 1

    def next_btn(self):
        """button to submit answer and go to next question"""

        answer = self.user_choice.get()

        # Check if answer is null. If so quit out of sequence
        # WARNING: THIS CHECK DOES NOT WORK
        if answer == "":
            return

        # Check if answer is correct and send result to log file
        if self.controller.check_answer(answer):
            log_action(self.session, f"QUESTION {self.controller.q_numb}", "SUBMIT",
                       [f"answer={answer}", "correct=True", f"graph={self.controller.current_question.graph}"])
        else:
            log_action(self.session, f"QUESTION {self.controller.q_numb}", "SUBMIT",
                       [f"answer={answer}", "correct=False", f"graph={self.controller.current_question.graph}"])

        if self.controller.more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_answer_btns()
            self.update_graphs()

        else:
            self.window.destroy
