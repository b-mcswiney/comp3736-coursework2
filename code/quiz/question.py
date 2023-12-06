
class Question:
    """Class for storing question data"""
    def __init__(self, question, image_path1, image_path2, correct_choice, choices, graph_type):
        self.question_text = question
        self.image_path1 = image_path1
        self.image_path2 = image_path2
        self.correct_choice = correct_choice
        self.choices = choices
        self.graph = graph_type
