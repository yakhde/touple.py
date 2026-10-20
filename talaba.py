import tkinter as tk

from colorama import Fore,Style,init
init(autoreset=True)



root = tk.Tk()
root.title("  Bolimni tanlang")
root.geometry("300x250")  # Oyna o'lchami

# Tugma bosilganda bajariladigan funksiya
def tugma_bosildi():
    print("Tugma bosildi!")
    # Yoki oynada matn chiqarish mumkin

# Tugmani yaratish
btn = tk.Button(root, text="Tizimga kirish!", command=tugma_bosildi, bg="green", fg="white", font=("Arial", 12))
btn.pack(pady=50)  # Tugmani oynaga joylashtirish

# Oynani ochiq ushlab turish
root.mainloop()

