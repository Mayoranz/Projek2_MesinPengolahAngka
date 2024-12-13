import tkinter as tk
from tkinter import font, messagebox

def proses_angka(event=None):
    input_angka = entry_angka.get()
    if input_angka.lower() == 'selesai':
        tampilkan_hasil()
        return
    try:
        angka.append(float(input_angka))
        entry_angka.delete(0, tk.END)
        update_listbox()
    except ValueError:
        text_hasil.delete(1.0, tk.END)
        text_hasil.insert(tk.END, "Tolong masukkan angka yang valid.")

def update_listbox():
    listbox.delete(0, tk.END)
    for num in angka:
        listbox.insert(tk.END, num) 

def edit_selected():
    try:
        selected_index = listbox.curselection()[0]
        entry_angka.delete(0, tk.END) 
        entry_angka.insert(0, angka[selected_index]) 
    except IndexError:
        messagebox.showwarning("Peringatan", "Silakan pilih angka yang ingin diedit.")

def update_number():
    try:
        selected_index = listbox.curselection()[0]
        new_value = float(entry_angka.get()) 
        angka[selected_index] = new_value
        entry_angka.delete(0, tk.END)  
        update_listbox()  
    except (IndexError, ValueError):
        messagebox.showwarning("Peringatan", "Silakan pilih angka yang ingin diperbarui dan masukkan angka yang valid.")

def tampilkan_hasil():
    if angka:
        angka_bulat = [int(a) if a.is_integer() else a for a in angka]
        hasil = f"""
        Angka yang dimasukkan: {angka_bulat}
        Jumlah angka: {int(sum(angka)) if sum(angka).is_integer() else sum(angka)}
        Rata-rata angka: {int(sum(angka) / len(angka)) if (sum(angka) / len(angka)).is_integer() else (sum(angka) / len(angka))}
        Angka maksimum: {int(max(angka)) if max(angka).is_integer() else max(angka)}
        Angka minimum: {int(min(angka)) if min(angka).is_integer() else min(angka)}
        """
        text_hasil.delete(1.0, tk.END)
        text_hasil.insert(tk.END, hasil)
    else:
        text_hasil.delete(1.0, tk.END)
        text_hasil.insert(tk.END, "Tidak ada angka yang dimasukkan.")

root = tk.Tk()
root.title("Program Pengolahan Angka")
root.configure(bg='lightblue')

angka = []

custom_font = font.Font(family="Helvetica", size=12)

label = tk.Label(root, text="Masukkan angka (dan tekan enter jika sudah):", bg='lightblue', fg='blue', font=custom_font)
label.pack(pady=10)

entry_angka = tk.Entry(root, width=30, font=custom_font)
entry_angka.pack(pady=5)

entry_angka.bind('<Return>', proses_angka)

tombol_selesai = tk.Button(root, text="Selesai", command=tampilkan_hasil, bg='red', fg='white', font=custom_font)
tombol_selesai.pack(pady=10)

text_hasil = tk.Text(root, height=10, width=50, bg='white', fg='black', font=custom_font)
text_hasil.pack(pady=10)

listbox = tk.Listbox(root, height=5, width=30, font=custom_font)
listbox.pack(pady=10)
edit_button = tk.Button(root, text="Edit Angka Terpilih", command=edit_selected, bg='orange', fg='black', font=custom_font)
edit_button.pack(pady=5)
update_button = tk.Button(root, text="Perbarui Angka", command=update_number, bg='green', fg='white', font=custom_font)
update_button.pack(pady= 5)
frame = tk.Frame(root, bg='lightblue')
frame.pack(pady=10)
title_label = tk.Label(frame, text="Program Pengolahan Angka", bg='lightblue', fg='darkblue', font=("Helvetica", 16, "bold"))
title_label.pack(pady=5)

root.mainloop()