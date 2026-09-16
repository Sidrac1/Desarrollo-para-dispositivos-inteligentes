# Requiere: pip install bcrypt
import bcrypt
import time

password = b"Sidrac" # bcrypt requiere bytes, no strings

print("--- EJEMPLO 1: Hasheo básico con bcrypt ---")
# 1. Generar el salt (por defecto usa 12 rondas)
salt = bcrypt.gensalt()
print(f"Salt generado: {salt}") #recordar hacer el efecto del Salt Bae, el chef turco

# 2. Hashear la contraseña
hashed = bcrypt.hashpw(password, salt)
print(f"Hash completo: {hashed}")

# 3. Verificar
is_valid = bcrypt.checkpw(password, hashed)
print(f"¿La contraseña es válida? {is_valid}")


print("\n --- ejemplo2: Entendiendo el factor 'Cost factor' (Rondas) ---")
for rounds in [10,12,14]:
    start_time = time.time()
    #bcrypt.gensalt(rounds=rounds)
    bcrypt.hashpw(password,bcrypt.gensalt(rounds=rounds))
    end_time = time.time()
    print(f"Rondas: {rounds} (2^{rounds}iteraciones) -> Tiempo: {end_time - start_time:.4f}segundos")