import tkinter.ttk as ttk
import tkinter as tk
import random
import time

class SortVisualizer:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame, width=600, height=300, bg="white")
        self.canvas.pack(pady=10)
        button_frame = tk.Frame(self.frame)
        button_frame.pack()
        self.shuffle_btn = tk.Button(button_frame, text="Shuffle", command=self.shuffle)
        self.shuffle_btn.pack(side=tk.LEFT, padx=5)
        self.sort_btn = tk.Button(button_frame, text="Bubble Sort", command=self.bubble_sort)
        self.sort_btn.pack(side=tk.LEFT, padx=5)
        self.array = []
        self.bar_width = 0
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
            color = "green" if highlight and i in highlight else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_bars(highlight=(j, j + 1))
                    self.frame.update()
                    time.sleep(0.05)
        self.draw_bars()


class StackVisualizer:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame, width=200, height=300, bg="white")
        self.canvas.pack(pady=10)
        button_frame = tk.Frame(self.frame)
        button_frame.pack()
        self.entry = tk.Entry(button_frame, width=10)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.push_btn = tk.Button(button_frame, text="Push", command=self.push)
        self.push_btn.pack(side=tk.LEFT, padx=5)
        self.pop_btn = tk.Button(button_frame, text="Pop", command=self.pop)
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
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue")
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(value))

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
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.sort_tab = tk.Frame(self.notebook)
        self.stack_tab = tk.Frame(self.notebook)

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
