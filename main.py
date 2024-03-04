import hashlib
import random

def sha1_truncated(message, num_bits):
    full_hash = hashlib.sha1(message.encode()).hexdigest()
    hash_int = int(full_hash, 16)
    truncated_hash = hash_int % (1 << num_bits)
    truncated_hash_hex = format(truncated_hash, f'0{num_bits//4}x')
    return truncated_hash_hex

def generate_random_message():
    # Generate a random message of varying lengths
    message_length = random.randint(10, 100)
    return ''.join(chr(random.randint(32, 126)) for _ in range(message_length))

def collision_attack(target_hash, num_bits):
    # Keep track of attempts
    attempts = 0
    seen_hashes = set()

    while True:
        message = generate_random_message()
        truncated_hash = sha1_truncated(message, num_bits)

        if truncated_hash == target_hash:
            return attempts

        # Check for collisions
        if truncated_hash in seen_hashes:
            continue

        seen_hashes.add(truncated_hash)
        attempts += 1

# Test different bit sizes
bit_sizes = [8, 10, 12, 14, 16, 18, 20, 22]

for bit_size in bit_sizes:
    print(f"\nTesting for {bit_size}-bit hashes:")
    total_attempts = 0
    num_samples = 50

    for _ in range(num_samples):
        target_hash = sha1_truncated(generate_random_message(), bit_size)
        attempts = collision_attack(target_hash, bit_size)
        total_attempts += attempts
        print(f"Sample {total_attempts}: {attempts} attempts")

    average_attempts = total_attempts / num_samples
    print(f"Average attempts: {average_attempts}\n")
