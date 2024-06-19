#romans

def int_to_roman(num):
    # Mapeamento de valores inteiros para símbolos romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_int(s):
    # Mapeamento de símbolos romanos para valores inteiros
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s):
        int_value = roman_to_int_map[char]
        if int_value < prev_value:
            total -= int_value
        else:
            total += int_value
        prev_value = int_value
    return total

if __name__ == "__main__":
    while True:
        choice = input("Deseja converter um número inteiro para romano (1) ou romano para inteiro (2)? Digite 1 ou 2: ")
        
        if choice == "1":
            num = int(input("Digite um número inteiro: "))
            print(f"O número romano é: {int_to_roman(num)}")
        elif choice == "2":
            roman = input("Digite um número romano: ")
            print(f"O número inteiro é: {roman_to_int(roman)}")
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")
        
        again = input("Deseja fazer outra conversão? (sim/não): ").strip().lower()
        if again != 'sim':
            print("Obrigado utilizar este codigo")
            break
