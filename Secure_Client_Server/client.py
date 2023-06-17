# I have used cryptidy library in python for symmetric and assymetric encryption and decryption.

import sys
import socket
from cryptidy import asymmetric_encryption, symmetric_encryption

def main():
    # Get server host and port from user input
    host = sys.argv[1]
    port = int(sys.argv[2])

    # Load client's public key
    with open(sys.argv[3], "r") as key_file:
        public_key = key_file.read()

    # Generate session key
    session_key = symmetric_encryption.generate_key(16)

    # Encrypt it with client's public key
    encrypted_session_key = asymmetric_encryption.encrypt_message(session_key, public_key)

    # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to server...")

        # Send session key to the server
        s.sendall(encrypted_session_key)

        # Prompt user for game information requests
        while True:
            user_input = input("> ").strip()
            if user_input.lower() == "quit":
                # Send quit message to server and exit loop
                encrypted_message = symmetric_encryption.encrypt_message(b"quit", session_key)
                s.sendall(encrypted_message)
                print("Goodbye!")
                break
            else:
                # Parse user input to get game_id and field
                try:
                    game_id, field = user_input.split()
                    request = f"{game_id},{field}"
                except ValueError:
                    print("unknown")
                    continue

                # Encrypt request with session key and send to server
                encrypted_request = symmetric_encryption.encrypt_message(request.encode(), session_key)
                s.sendall(encrypted_request)

                # Receive encrypted response from server
                encrypted_response = s.recv(1024)

                # Decrypt response with session key and print or "unknown" if response is empty
                timestamp, decrypted_response = symmetric_encryption.decrypt_message(encrypted_response, session_key)
                decrypted_response=decrypted_response.decode()
                if decrypted_response:
                    print(decrypted_response)
                else:
                    print("no response")

if __name__ == "__main__":
    main()