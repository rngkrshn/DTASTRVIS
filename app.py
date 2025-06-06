import tkinter.ttk as ttk
import tkinter as tk
import random

# Color scheme
BG_COLOR = "#282c34"
CANVAS_BG = "#1e1e1e"
BAR_COLOR = "#61afef"
BAR_HIGHLIGHT = "#e06c75"
STACK_COLOR = "#98c379"
STACK_BG = "#1e1e1e"
BTN_BG = "#3e4451"
BTN_FG = "white"

class SortVisualizer:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg=BG_COLOR)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame, width=600, height=300, bg=CANVAS_BG, highlightthickness=0)
        self.canvas.pack(pady=10)
        button_frame = tk.Frame(self.frame, bg=BG_COLOR)
        button_frame.pack()
        self.shuffle_btn = tk.Button(button_frame, text="Shuffle", command=self.shuffle, bg=BTN_BG, fg=BTN_FG)
        self.shuffle_btn.pack(side=tk.LEFT, padx=5)
        self.sort_btn = tk.Button(button_frame, text="Bubble Sort", command=self.bubble_sort, bg=BTN_BG, fg=BTN_FG)
        self.sort_btn.pack(side=tk.LEFT, padx=5)
        self.stop_btn = tk.Button(button_frame, text="Stop", command=self.stop_sort, state=tk.DISABLED, bg=BTN_BG, fg=BTN_FG)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        self.array = []
        self.bar_width = 0
        self.after_id = None
        self.shuffle()

    def shuffle(self):
        self.array = [random.randint(10, 100) for _ in range(30)]
        self.bar_width = 600 // len(self.array)
        self.draw_bars()

    def draw_bars(self, highlight=None):
        self.canvas.delete("all")
        for i, val in enumerate(self.array):
            x0 = i * self.bar_width
            y0 = 300 - val * 2
            x1 = (i + 1) * self.bar_width
            y1 = 300
            color = BAR_HIGHLIGHT if highlight and i in highlight else BAR_COLOR
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

    def bubble_sort(self):
        if self.after_id:
            return
        self.n = len(self.array)
        self.i = 0
        self.j = 0
        self.sort_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.after_id = self.frame.after(0, self._bubble_sort_step)

    def _bubble_sort_step(self):
        if self.i < self.n:
            if self.j < self.n - self.i - 1:
                if self.array[self.j] > self.array[self.j + 1]:
                    self.array[self.j], self.array[self.j + 1] = self.array[self.j + 1], self.array[self.j]
                self.draw_bars(highlight=(self.j, self.j + 1))
                self.j += 1
            else:
                self.j = 0
                self.i += 1
            self.after_id = self.frame.after(50, self._bubble_sort_step)
        else:
            self.stop_sort()

    def stop_sort(self):
        if self.after_id:
            self.frame.after_cancel(self.after_id)
            self.after_id = None
        self.sort_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.draw_bars()


class StackVisualizer:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg=BG_COLOR)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame, width=200, height=300, bg=STACK_BG, highlightthickness=0)
        self.canvas.pack(pady=10)
        button_frame = tk.Frame(self.frame, bg=BG_COLOR)
        button_frame.pack()
        self.entry = tk.Entry(button_frame, width=10)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.push_btn = tk.Button(button_frame, text="Push", command=self.push, bg=BTN_BG, fg=BTN_FG)
        self.push_btn.pack(side=tk.LEFT, padx=5)
        self.pop_btn = tk.Button(button_frame, text="Pop", command=self.pop, bg=BTN_BG, fg=BTN_FG)
        self.pop_btn.pack(side=tk.LEFT, padx=5)
        self.stack = []
        self.draw_stack()

    def draw_stack(self):
        self.canvas.delete("all")
        width = 150
        height = 30
        for i, value in enumerate(reversed(self.stack)):
            x0 = 25
            y0 = 270 - i * height
            x1 = x0 + width
            y1 = y0 + height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=STACK_COLOR, outline="")
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(value), fill=BTN_FG)

    def push(self):
        value = self.entry.get()
        if value:
            self.stack.append(value)
            self.entry.delete(0, tk.END)
            self.draw_stack()

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.draw_stack()


class App:
    def __init__(self, root):
        root.title("DSA Visualizer")
        root.geometry("620x400")
        root.configure(bg=BG_COLOR)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook", background=BG_COLOR)
        style.configure("TNotebook.Tab", background=BTN_BG, foreground=BTN_FG)
        style.map("TNotebook.Tab", background=[("selected", CANVAS_BG)])

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.sort_tab = tk.Frame(self.notebook, bg=BG_COLOR)
        self.stack_tab = tk.Frame(self.notebook, bg=BG_COLOR)

        self.notebook.add(self.sort_tab, text="Sorting")
        self.notebook.add(self.stack_tab, text="Stack")

        self.sort_visualizer = SortVisualizer(self.sort_tab)
        self.stack_visualizer = StackVisualizer(self.stack_tab)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
