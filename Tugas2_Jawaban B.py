def ganjil_genap():
    numbers = []
    print("Masukkan angka: ")
    input_numbers = input()
    numbers = [int(x) for x in input_numbers.split()]

    print("Hasilnya:")
    for num in numbers:
        if num % 2!= 0:
            print(f"{num} = {num**2}")

ganjil_genap()