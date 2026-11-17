import hashlib

# 1. Criptografia por substituição (Cifra de César simples - Aulas 1 a 3)
def criptografar_substituicao(senha):
    dicionario = "bcdefghijklmnopqrstuvwxyza"
    senha_criptografada = ""
    
    for letra in senha:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a")
            senha_criptografada += dicionario[posicao]
        else:
            senha_criptografada += letra
            
    return senha_criptografada

# 2. Geração de Hash (Aulas 4 e 5)
def gerar_hash(senha):
    # Converte a string para bytes e gera o hash SHA-256
    return hashlib.sha256(senha.encode()).hexdigest()

# --- Testando o código ---
senha_original = "Alura2026!"

senha_cifrada = criptografar_substituicao(senha_original)
senha_hash = gerar_hash(senha_original)

print(f"Senha original: {senha_original}")
print(f"Criptografada (Substituição): {senha_cifrada}")
print(f"Hash (SHA-256): {senha_hash}")