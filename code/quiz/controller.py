from quiz.question import Question


class QuizController:
    """manages Quiz state and questions"""

    def __init__(self, questions):
        self.q_numb = 0
        self.questions = questions
        self.current_question = None

    def more_questions(self):
        """check if there are more questions"""

        return self.q_numb < len(self.questions)

    def next_question(self):
        """Proceed to next question"""

        self.current_question = self.questions[self.q_numb]
        self.q_numb = self.q_numb + 1

        text = self.current_question.question_text
        return f"{self.q_numb}: {text}"

    def check_answer(self, answer):
        """Check user answer"""

        return answer == self.current_question.correct_choice
