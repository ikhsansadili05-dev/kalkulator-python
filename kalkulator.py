def kalkulator():
    print("=== KALKULATOR SEDERHANA ===")
    print("Operasi: + - * /")
    print("Ketik 'keluar' untuk berhenti\n")
    
    while True:
        angka1 = input("Masukkan angka pertama: ")
        if angka1.lower() == 'keluar':
            print("Sampai jumpa!")
            break
        
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = input("Masukkan angka kedua: ")
        
        try:
            a = float(angka1)
            b = float(angka2)
            
            if operator == '+':
                hasil = a + b
            elif operator == '-':
                hasil = a - b
            elif operator == '*':
                hasil = a * b
            elif operator == '/':
                if b == 0:
                    print("Error: Tidak bisa dibagi nol!\n")
                    continue
                hasil = a / b
            else:
                print("Operator tidak valid!\n")
                continue
            
            print("Hasil:", a, operator, b, "=", hasil, "\n")
        
        except ValueError:
            print("Input tidak valid! Masukkan angka.\n")

kalkulator()
