import tkinter as tk

def check_vowels():
    text = entry.get().lower()
    vowels = "aeiou"
    found = [letter for letter in text if letter in vowels]

    if text == "":
        result.config(
            text="Please enter a word!",
            fg="#D63384"
        )
    elif found:
        result.config(
            text="Vowels Found: " + ", ".join(found),
            fg="#8E4585"
        )
        count.config(
            text=f"Total Vowels: {len(found)}"
        )
    else:
        result.config(
            text="No vowels found!",
            fg="#D63384"
        )
        count.config(text="Total Vowels: 0")


def clear_all():
    entry.delete(0, tk.END)
    result.config(
        text="Your result will appear here",
        fg="#777777"
    )
    count.config(text="")
    entry.focus()


def exit_app():
    root.destroy()


# Main Window
root = tk.Tk()
root.title("Vowels Checker")
root.geometry("500x480")
root.resizable(False, False)
root.configure(bg="#FFF0F5")

# Heading
heading = tk.Label(
    root,
    text="VOWELS CHECKER",
    font=("Arial", 24, "bold"),
    bg="#FFF0F5",
    fg="#C0448F"
)
heading.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Enter a word or sentence below",
    font=("Arial", 11),
    bg="#FFF0F5",
    fg="#777777"
)
subtitle.pack(pady=5)

# Input Label
input_label = tk.Label(
    root,
    text="Enter Your Text",
    font=("Arial", 12, "bold"),
    bg="#FFF0F5",
    fg="#704078"
)
input_label.pack(pady=(15, 5))

# Input Box
entry = tk.Entry(
    root,
    font=("Arial", 15),
    width=28,
    justify="center",
    bg="white",
    fg="#444444",
    relief="flat",
    bd=5
)
entry.pack(ipady=10, pady=5)
entry.focus()

# Check Button
check_button = tk.Button(
    root,
    text="CHECK VOWELS",
    command=check_vowels,
    font=("Arial", 12, "bold"),
    bg="#D85A9E",
    fg="white",
    activebackground="#B83D82",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=20,
    pady=8
)
check_button.pack(pady=(15, 8))

# Clear Button
clear_button = tk.Button(
    root,
    text="CLEAR",
    command=clear_all,
    font=("Arial", 11, "bold"),
    bg="#E5D5E9",
    fg="#704078",
    activebackground="#D3B9DB",
    relief="flat",
    cursor="hand2",
    width=20,
    pady=7
)
clear_button.pack(pady=5)

# Result Box
result = tk.Label(
    root,
    text="Your result will appear here",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#777777",
    width=38,
    height=2,
    relief="flat"
)
result.pack(pady=(18, 5))

# Vowel Count
count = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#FFF0F5",
    fg="#8E4585"
)
count.pack(pady=5)

# Exit Button
exit_button = tk.Button(
    root,
    text="EXIT",
    command=exit_app,
    font=("Arial", 10, "bold"),
    bg="#B85C7A",
    fg="white",
    activebackground="#963D5C",
    relief="flat",
    cursor="hand2",
    width=12,
    pady=5
)
exit_button.pack(pady=5)

# Start Application
root.mainloop()
