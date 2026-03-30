from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,
                           bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250,
                             bg="white",
                             highlightthickness=0)
        self.content = self.canvas.create_text(150, 125, width=270,
                                               text="All questions are here!",
                                               fill=THEME_COLOR,
                                               font=("Arial", 18, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.false_button = Button(image=false_image, highlightthickness=0,
                                   command=self.false_call)
        self.false_button.grid(column=1, row=2)

        self.true_button = Button(image=true_image, highlightthickness=0,
                                  command=self.true_call)
        self.true_button.grid(column=0, row=2)

        self.score_label = Label(text="Score: 0", fg="white",
                                 bg=THEME_COLOR,
                                 font=("Arial", 10, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            questions = self.quiz.next_question()
            self.canvas.itemconfig(self.content, text=questions)
        else:
            self.canvas.itemconfig(self.content,
                                   text="You have reached at the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_call(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_call(self):
        is_ok = self.quiz.check_answer("false")
        self.give_feedback(is_ok)

    def give_feedback(self, is_ok):
        if is_ok:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
