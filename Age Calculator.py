import tkinter as tk
from datetime import datetime, timedelta

class AgeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Age Calculator")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        
        tk.Label(master, text="Enter DOB (DD-MM-YYYY)", font=("Arial", 14)).pack(pady=10)
        self.entry = tk.Entry(master, font=("Arial", 14), justify='center')
        self.entry.pack(pady=5)

        self.result = tk.Label(master, text="", font=("Arial", 12), justify='left')
        self.result.pack(pady=10)

        tk.Button(master, text="Calculate", font=("Arial", 12), command=self.calculate).pack()

    def calculate(self):
        dob_str = self.entry.get()
        try:
            dob = datetime.strptime(dob_str, "%d-%m-%Y")
            today = datetime.today()

            years = today.year - dob.year
            months = today.month - dob.month
            days = today.day - dob.day

            if days < 0:
                months -= 1
                prev_month = today.replace(day=1) - timedelta(days=1)
                days += prev_month.day

            if months < 0:
                years -= 1
                months += 12

            next_birthday = dob.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            remaining = next_birthday - today

            zodiac = self.get_zodiac(dob.day, dob.month)
            weekday = dob.strftime('%A')

            text = (
                f"Age: {years} years, {months} months, {days} days\n\n"
                f"Day of Birth: {weekday}\n"
                f"Zodiac Sign: {zodiac}\n\n"
                f"Next Birthday: in {remaining.days} days"
            )
            self.result.config(text=text)
        except:
            self.result.config(text="Invalid date format. Use DD-MM-YYYY")

    def get_zodiac(self, day, month):
        zodiacs = [
            ((20, 1), "Capricorn"), ((19, 2), "Aquarius"), ((20, 3), "Pisces"),
            ((20, 4), "Aries"), ((21, 5), "Taurus"), ((21, 6), "Gemini"),
            ((23, 7), "Cancer"), ((23, 8), "Leo"), ((23, 9), "Virgo"),
            ((23, 10), "Libra"), ((22, 11), "Scorpio"), ((22, 12), "Sagittarius"),
            ((31, 12), "Capricorn")
        ]
        for (d, m), sign in zodiacs:
            if (day, month) <= (d, m):
                return sign
        return "Capricorn"

if __name__ == '__main__':
    root = tk.Tk()
    app = AgeApp(root)
    root.mainloop()
