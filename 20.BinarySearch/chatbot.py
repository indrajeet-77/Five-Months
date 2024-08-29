import tkinter as tk
from tkinter import messagebox

# Sample music data
music_data = {
    "happy": ["Happy by Pharrell Williams", "Uptown Funk by Mark Ronson ft. Bruno Mars"],
    "sad": ["Someone Like You by Adele", "Stay With Me by Sam Smith"],
    "energetic": ["Eye of the Tiger by Survivor", "Can't Hold Us by Macklemore & Ryan Lewis"],
    "relaxed": ["Weightless by Marconi Union", "Clair de Lune by Debussy"]
}

class MusicRecommenderBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Recommender Chatbot")

        self.chat_log = tk.Text(root, bd=1, bg="white", width=65, height=20, font=("TimesNew roman", 14), state=tk.DISABLED)
        self.chat_log.grid(row=0, column=0, columnspan=2)

        self.user_input = tk.Entry(root, bd=1, bg="white", width=29, font=("Arial", 14))
        self.user_input.grid(row=1, column=0)

        self.send_button = tk.Button(root, text="Send", command=self.send_message, bg="blue", fg="white", font=("Arial", 14))
        self.send_button.grid(row=1, column=1)

        self.intro_message()

    def intro_message(self):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, "Chatbot: Hi! I'm your music recommender bot. How are you feeling today? (happy, sad, energetic, relaxed)\n\n")
        self.chat_log.config(state=tk.DISABLED)

    def send_message(self):
        user_msg = self.user_input.get().strip()
        if user_msg:
            self.chat_log.config(state=tk.NORMAL)
            self.chat_log.insert(tk.END, f"You: {user_msg}\n")
            self.chat_log.config(state=tk.DISABLED)
            self.user_input.delete(0, tk.END)
            self.get_recommendation(user_msg.lower())

    def get_recommendation(self, mood):
        self.chat_log.config(state=tk.NORMAL)
        if mood in music_data:
            recommendations = "\n".join(music_data[mood])
            self.chat_log.insert(tk.END, f"Chatbot: Based on your mood, I recommend:\n{recommendations}\n\n")
        else:
            self.chat_log.insert(tk.END, "Chatbot: I'm sorry, I don't understand that mood. Please try again with: happy, sad, energetic, or relaxed.\n\n")
        self.chat_log.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    bot = MusicRecommenderBot(root)
    root.mainloop()
