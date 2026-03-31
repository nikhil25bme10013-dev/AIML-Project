import random
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

PLAYER_HP = 30
AI_HP = 30
ROUND = 1

# ---------- Game Logic (unchanged) ----------

def roll_dice(n=2):
    return [random.randint(1, 6) for _ in range(n)]

def score_roll(roll):
    s = sum(roll)
    if roll.count(6) == 2:
        return s + 5
    if roll.count(1) >= 1:
        return s - 3
    return s

def ai_decision(ai_hp, player_hp):
    if ai_hp < player_hp:
        return 3 if random.random() < 0.7 else 2
    return 2 if random.random() < 0.8 else 3

# ---------- GUI Game Class ----------

class DiceBattleGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Dice Battle")
        self.geometry("600x500")

        self.player_hp = 30
        self.ai_hp = 30
        self.round = 1

        # Title
        self.title_label = ctk.CTkLabel(self, text="🎲 AI Dice Battle", font=("Arial", 28, "bold"))
        self.title_label.pack(pady=10)

        # HP Display
        self.hp_label = ctk.CTkLabel(self, text="", font=("Arial", 18))
        self.hp_label.pack(pady=10)

        # Log Box
        self.log_box = ctk.CTkTextbox(self, width=550, height=250)
        self.log_box.pack(pady=10)
        self.log_box.configure(state="disabled")

        # Buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.roll2_btn = ctk.CTkButton(self.button_frame, text="Roll 2 Dice", command=lambda: self.play_round(2))
        self.roll2_btn.grid(row=0, column=0, padx=10)

        self.roll3_btn = ctk.CTkButton(self.button_frame, text="Roll 3 Dice", command=lambda: self.play_round(3))
        self.roll3_btn.grid(row=0, column=1, padx=10)

        self.update_hp()

    # ---------- Helper Methods ----------

    def log(self, text):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", text + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def update_hp(self):
        self.hp_label.configure(
            text=f"Round {self.round} | Your HP: {self.player_hp} | AI HP: {self.ai_hp}"
        )

    # ---------- Game Round ----------

    def play_round(self, player_dice):
        if self.player_hp <= 0 or self.ai_hp <= 0:
            return

        self.log(f"\n--- Round {self.round} ---")

        # Player roll
        p_roll = roll_dice(player_dice)
        p_score = score_roll(p_roll)
        self.log(f"You rolled {p_roll} -> score {p_score}")

        # AI roll
        a_dice = ai_decision(self.ai_hp, self.player_hp)
        a_roll = roll_dice(a_dice)
        a_score = score_roll(a_roll)
        self.log(f"AI rolled {a_roll} -> score {a_score}")

        # Compare scores
        if p_score > a_score:
            damage = p_score - a_score
            self.ai_hp -= damage
            self.log(f"You hit AI for {damage} damage!")
        elif a_score > p_score:
            damage = a_score - p_score
            self.player_hp -= damage
            self.log(f"AI hits you for {damage} damage!")
        else:
            self.log("Tie! No damage.")

        self.round += 1
        self.update_hp()

        # Check game over
        if self.player_hp <= 0 or self.ai_hp <= 0:
            winner = "You win! 🎉" if self.player_hp > 0 else "AI wins! 🤖"
            self.log(f"\n=== Game Over ===\n{winner}")
            self.roll2_btn.configure(state="disabled")
            self.roll3_btn.configure(state="disabled")

# ---------- Run App ----------

if __name__ == "__main__":
    app = DiceBattleGUI()
    app.mainloop()
