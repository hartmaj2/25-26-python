import tkinter as tk
import random

Question = tuple[str, str]  # (country, capital)

QUESTIONS: list[Question] = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Italy", "Rome"),
    ("Spain", "Madrid"),
    ("Portugal", "Lisbon"),
    ("Poland", "Warsaw"),
    ("Czechia", "Prague"),
    ("Austria", "Vienna"),
]

ALL_CAPITALS = [capital for _, capital in QUESTIONS]


class App(tk.Frame):
    TIME_LIMIT_S = 10

    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        self.pack(padx=20, pady=20)

        # State
        self.correct: str = ""
        self.score: int = 0
        self.time_left: int = self.TIME_LIMIT_S
        self.timer_job: str | None = None
        self.locked: bool = False  # prevents multiple answers

        self._build_ui()
        self._next_question()

    def _build_ui(self) -> None:
        top = tk.Frame(self)
        top.pack(fill="x", pady=(0, 10))

        self.score_label = tk.Label(top, text="Points: 0", anchor="w")
        self.score_label.pack(side="left")

        self.timer_label = tk.Label(top, text=f"Time: {self.TIME_LIMIT_S}", anchor="e")
        self.timer_label.pack(side="right")

        self.question_label = tk.Label(self, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.buttons: list[tk.Button] = []
        for i in range(4):
            btn = tk.Button(self, width=22, command=lambda idx=i: self._answer(idx))
            btn.pack(pady=2)
            self.buttons.append(btn)

        self.feedback = tk.Label(self, text="")
        self.feedback.pack(pady=10)

    # -------- quiz flow --------

    def _next_question(self) -> None:
        self._cancel_timer()

        country, self.correct = random.choice(QUESTIONS)
        choices = random.sample(ALL_CAPITALS, k=4)
        if self.correct not in choices:
            choices[random.randrange(4)] = self.correct
        random.shuffle(choices)

        self.question_label.config(text=f"Capital of {country}?")
        for btn, text in zip(self.buttons, choices):
            btn.config(text=text, state="normal")

        self.feedback.config(text="")
        self.locked = False

        self.time_left = self.TIME_LIMIT_S
        self._render_hud()
        self._tick()

    def _answer(self, index: int) -> None:
        if self.locked:
            return
        self.locked = True
        self._cancel_timer()
        self._disable_buttons()

        chosen = str(self.buttons[index]["text"])
        if chosen == self.correct:
            self.score += 1
            self.feedback.config(text="Correct ✔")
        else:
            self.feedback.config(text=f"Wrong ✘  (correct: {self.correct})")

        self._render_hud()
        self.after(900, self._next_question)

    def _timeout(self) -> None:
        if self.locked:
            return
        self.locked = True
        self._disable_buttons()
        self.feedback.config(text=f"Time ✘  (correct: {self.correct})")
        self.after(900, self._next_question)

    # -------- timer --------

    def _tick(self) -> None:
        self.timer_label.config(text=f"Time: {self.time_left}")
        if self.time_left <= 0:
            self.timer_job = None
            self._timeout()
            return

        self.time_left -= 1
        self.timer_job = self.after(1000, self._tick)

    def _cancel_timer(self) -> None:
        if self.timer_job is not None:
            try:
                self.after_cancel(self.timer_job)
            except tk.TclError:
                pass
            self.timer_job = None

    # -------- helpers --------

    def _disable_buttons(self) -> None:
        for btn in self.buttons:
            btn.config(state="disabled")

    def _render_hud(self) -> None:
        self.score_label.config(text=f"Points: {self.score}")
        self.timer_label.config(text=f"Time: {self.time_left}")


def main() -> None:
    root = tk.Tk()
    root.title("Country Quiz (Timer + Points)")
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()