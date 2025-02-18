import tkinter as tk
from tkinter import messagebox

# Definicja polskiego alfabetu
ALFABET = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
DLUGOSC_ALFABETU = len(ALFABET)

# Funkcja szyfrująca
def szyfruj(tekst, klucz):
    zaszyfrowany = ""
    for litera in tekst:
        if litera.lower() in ALFABET:
            indeks = ALFABET.index(litera.lower())
            nowy_indeks = (indeks + klucz) % DLUGOSC_ALFABETU
            nowa_litera = ALFABET[nowy_indeks]
            if litera.isupper():
                nowa_litera = nowa_litera.upper()
            zaszyfrowany += nowa_litera
        else:
            zaszyfrowany += litera  # pozostawienie znaków spoza alfabetu bez zmian
    return zaszyfrowany

# Funkcja deszyfrująca
def deszyfruj(tekst, klucz):
    return szyfruj(tekst, -klucz)

# Funkcja walidująca wprowadzony tekst
def waliduj_tekst(event, pole):
    tekst = pole.get()
    nowy_tekst = "".join([lit for lit in tekst if lit.lower() in ALFABET or lit.isspace()])
    if tekst != nowy_tekst:
        pole.delete(0, tk.END)
        pole.insert(0, nowy_tekst)

# Tworzenie okna
root = tk.Tk()
root.title("Szyfr Cezara")
root.geometry("500x400")

# ---------------- SEKCJA SZYFROWANIA ----------------
tk.Label(root, text="SZYFROWANIE", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Wprowadź tekst:").pack()
pole_tekstowe_szyfruj = tk.Entry(root, width=50)
pole_tekstowe_szyfruj.pack()
pole_tekstowe_szyfruj.bind("<KeyRelease>", lambda event: waliduj_tekst(event, pole_tekstowe_szyfruj))
tk.Label(root, text="Podaj klucz (liczba całkowita):").pack()
pole_kluczowe_szyfruj = tk.Entry(root, width=10)
pole_kluczowe_szyfruj.pack()
tk.Button(root, text="Szyfrowanie", command=lambda: kliknij_szyfruj()).pack(pady=5)
tk.Label(root, text="Zaszyfrowany tekst:").pack()
pole_wyniku_szyfruj = tk.Entry(root, width=50, state="readonly")
pole_wyniku_szyfruj.pack()

# ---------------- SEKCJA DESZYFROWANIA ----------------
tk.Label(root, text="DESZYFROWANIE", font=("Arial", 12, "bold"), pady=10).pack()
tk.Label(root, text="Wprowadź tekst do deszyfracji:").pack()
pole_tekstowe_deszyfruj = tk.Entry(root, width=50)
pole_tekstowe_deszyfruj.pack()
pole_tekstowe_deszyfruj.bind("<KeyRelease>", lambda event: waliduj_tekst(event, pole_tekstowe_deszyfruj))
tk.Label(root, text="Podaj klucz (liczba całkowita):").pack()
pole_kluczowe_deszyfruj = tk.Entry(root, width=10)
pole_kluczowe_deszyfruj.pack()
tk.Button(root, text="Deszyfracja", command=lambda: kliknij_deszyfruj()).pack(pady=5)
tk.Label(root, text="Odszyfrowany tekst:").pack()
pole_wyniku_deszyfruj = tk.Entry(root, width=50, state="readonly")
pole_wyniku_deszyfruj.pack()

# Funkcja obsługująca szyfrowanie
def kliknij_szyfruj():
    try:
        tekst = pole_tekstowe_szyfruj.get()
        klucz = int(pole_kluczowe_szyfruj.get())
        wynik = szyfruj(tekst, klucz)
        pole_wyniku_szyfruj.config(state="normal")
        pole_wyniku_szyfruj.delete(0, tk.END)
        pole_wyniku_szyfruj.insert(0, wynik)
        pole_wyniku_szyfruj.config(state="readonly")
    except ValueError:
        messagebox.showerror("Błąd", "Klucz musi być liczbą całkowitą!")

# Funkcja obsługująca deszyfrowanie
def kliknij_deszyfruj():
    try:
        tekst = pole_tekstowe_deszyfruj.get()
        klucz = int(pole_kluczowe_deszyfruj.get())
        wynik = deszyfruj(tekst, klucz)
        pole_wyniku_deszyfruj.config(state="normal")
        pole_wyniku_deszyfruj.delete(0, tk.END)
        pole_wyniku_deszyfruj.insert(0, wynik)
        pole_wyniku_deszyfruj.config(state="readonly")
    except ValueError:
        messagebox.showerror("Błąd", "Klucz musi być liczbą całkowitą!")

# Uruchomienie aplikacji
root.mainloop()