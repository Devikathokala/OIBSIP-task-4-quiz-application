import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def display_question(self, question, options):
        print(question)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        return user_answer
    
    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            q = question['question']
            options = question['options']
            correct_answer = question['answer']
            
            user_answer = self.display_question(q, options)
            
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                user_answer = options[int(user_answer) - 1]
                if user_answer == correct_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer is: {correct_answer}\n")
            else:
                print("Invalid input. Skipping this question.\n")
        
        print(f"Quiz finished! Your score is: {self.score} out of {len(self.questions)}")


# Sample quiz questions
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Rome", "Berlin"],
        'answer': "Paris"
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Mercury", "Mars", "Venus", "Jupiter"],
        'answer': "Mars"
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'options': ["Jane Austen", "Charles Dickens", "William Shakespeare", "Leo Tolstoy"],
        'answer': "William Shakespeare"
    }
]

# Create Quiz instance and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()
