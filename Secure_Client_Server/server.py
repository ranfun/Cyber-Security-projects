# I have used cryptidy library in python for symmetric and assymetric encryption and decryption.

import socket
import sys
import csv
from cryptidy import asymmetric_encryption, symmetric_encryption

# Read the game data file and create a dictionary with game_id as keys and the corresponding data as values
with open(sys.argv[2], "r") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    data = {}
    for row in reader:
        data[row["game_id"]] = row

# Load server's private key
with open(sys.argv[3], "r") as key_file:
    private_key = key_file.read()

# Create a socket and bind it to the specified port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", int(sys.argv[1])))
    s.listen()

    print("server started")

    while True:
        # Wait for a client to connect
        conn, addr = s.accept()

        with conn:
            print("Connected by", addr)

            # Receive encrypted session key from client
            encrypted_session_key = conn.recv(1024)
            timestamp, session_key = asymmetric_encryption.decrypt_message(encrypted_session_key, private_key)

            while True:
                # Wait for an encrypted request from the client
                encrypted_request = conn.recv(1024).decode()

                # If the request is empty or the client has disconnected, break out of the loop
                if not encrypted_request:
                    break

                # Decrypt request with session key and parse to get the game_id and field
                try:
                    timestamp, request = symmetric_encryption.decrypt_message(encrypted_request, session_key)
                    request=request.decode()
                    if request == "quit":
                        # Disconnect the client and wait for a new client to connect
                        conn.close()
                        break
                    game_id, field = request.split(",")
                except:
                    # If the decryption fails, send "unknown" back to the client
                    conn.sendall(symmetric_encryption.encrypt_message("unknown".encode(), session_key))
                    continue

                # Check if the game_id is in the data dictionary
                if game_id in data and field in fieldnames:
                    # Get the value for the requested field from the data dictionary
                    value = data[game_id][field]
                    # print(value)
                    value=value.encode()
                    # Encrypt the value with session key and send it back to the client
                    # print(symmetric_encryption.encrypt_message(value, session_key))
                    encrypted_value=symmetric_encryption.encrypt_message(value, session_key)
                    conn.sendall(encrypted_value)
                    # Print the game_id and field to the server console
                    print(game_id, field)
                else:
                    # If the game_id is not in the data dictionary, send "unknown" back to the client
                    conn.sendall(symmetric_encryption.encrypt_message("unknown".encode(), session_key))