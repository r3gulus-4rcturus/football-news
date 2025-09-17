"""
Lab 01 - Spiral Poligon Bergradasi

Program ini menggambar spiral yang tersusun dari n-sisi (poligon)
dengan panjang garis yang bertambah setiap langkah, serta gradasi warna
dari warna awal (r1,g1,b1) ke warna akhir (r2,g2,b2).
"""

import turtle

# --- Konfigurasi awal turtle ----
turtle.shape('turtle')
turtle.title('Lab 01')
turtle.speed(0)
turtle.setup(width=750, height=750)
turtle.colormode(255)

# === Menerima input dari user ---

n = int(turtle.textinput("Lab 01", "The number of polygon sides for the spiral: "))

# TODO: membuat text input untuk r1,g1,b1 dan r2,g2,b2.
r1 = int(turtle.textinput("Lab 01", "The red value for the first color (between 0-255): "))
g1 = int(turtle.textinput("Lab 01","The green value for the first color (between 0-255): "))
b1 = int(turtle.textinput("Lab 01","The blue value for the first color (between 0-255): "))
r2 = int(turtle.textinput("Lab 01","The red value for the second color (between 0-255): "))
g2 = int(turtle.textinput("Lab 01","The green value for the second color (between 0-255): "))
b2 = int(turtle.textinput("Lab 01","The blue value for the second color (between 0-255): "))

# --- Parameter Spiral ---

# TODO: Mengisi nilai dari variable berdasarkan ketentuan soal
layer = 50          # jumlah putaran pada spiral
line_length = 0     # panjang garis saat ini, akan bertambah setiap iterasi
# --- Nilai warna RGB saat ini ---
# note: Nilai dari r, g, dan b akan berubah dari warna pertama (r1,g1,b1) hingga akhirnya menjadi warna akhir (r2,g2,b2)

# TODO: mengisi nilai r, g, b dengan variabel yang tepat
r = r1
g = g1
b = b1

# --- Besaran perubahan warna per layer ---

# TODO: Hitung nilai increment (pertambahan warna per layer)r_inc = (r2 - r1) / layer

r_inc = (r2 - r1) / layer
g_inc = (g2 - g1) / layer
b_inc = (b2 - b1) / layer

# TODO: Menggambar spiral

for i in range(layer):

    turtle.color(round(r),round(g),round(b)) # Mengatur warna garis
    
    # Menggambar polygon
    for j in range(n):
        turtle.forward(line_length)
        turtle.left(360/n)

        line_length += 1 # Mengupdate panjang line

    # Menambahkan nilai increment pada nilai warna saat ini
    r += r_inc
    g += g_inc
    b += b_inc

# Klik layar jendela untuk keluar
turtle.exitonclick()