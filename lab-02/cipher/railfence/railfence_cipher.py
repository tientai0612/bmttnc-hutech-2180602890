class RailFenceCipher:
    
    def init (self):
        pass
    
    def rail_fence_encrypt (self, plain_text, num_rails):
        rails = [[] for _ in range (num_rails)]
        rail_index = 0
        direction = 1 #1: down, -1: up
        for char in plain_text:
            rails[rail_index].append (char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1  # Fix: Increment rail_lengths[rail_index]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            if len(rails[rail_index]) > 0:  # Ensure there are characters left in the rail
                plain_text += rails[rail_index][0]
                rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text