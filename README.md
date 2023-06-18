# CyberSec Projects Showcase

This repository contains a collection of cybersecurity projects aimed at exploring various concepts and techniques. The projects focus on packet sniffing, Vigenère cipher encryption and decryption, and a secure server/client implementation.

## Packet Sniffing

The packet sniffing program allows you to capture and analyze network packets based on IP addresses and port numbers. It includes a filtering mechanism to display packets that match specific criteria. The sender component of this program spoofs its IP address to explore network security vulnerabilities further.

## Vigenère Cipher

The Vigenère cipher implementation consists of three programs:

- `vigenere_encrypt.py`: This program encrypts plain text using the Vigenère cipher. It requires a secret code as input.
- `vigenere_decrypt.py`: With the secret code, this program decrypts the cipher text back to plain text.
- `vigenere_crack.py`: Given a hint word with a higher number of letters than the code word, this program attempts to crack the Vigenère cipher by performing frequency analysis and pattern recognition.

## Secure Server/Client

The secure server/client project focuses on establishing a secure communication channel using asymmetric encryption. The implementation involves the following steps:

1. Key Generation:
   - A private key and a public key are generated for the server.
   - These keys ensure secure communication between the server and clients.

2. Session Key Establishment:
   - On the client's side, a session key is generated.
   - The session key is encrypted using the server's public key and sent to the server.
   - The server decrypts the received session key using its private key.

3. Encrypted Communication:
   - For the rest of the session, the session key is used to encrypt the communication between the client and server.
   - This encryption ensures the confidentiality and integrity of the transmitted data.

Additionally, the client can send requests to the server to retrieve file information.

## Getting Started

To get started with the projects in this repository, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/cybersec-projects-showcase.git
   ```

2. Navigate to the respective project directories:
   - Packet Sniffing: `cd packet_sniffing`
   - Vigenère Cipher: `cd vigenere_cipher`
   - Secure Server/Client: `cd secure_server_client`

3. Follow the instructions provided in each project's directory to run and interact with the programs.

---

Feel free to modify the README file as needed, add installation instructions, or provide any additional information that might be useful for users exploring your cybersecurity projects.
