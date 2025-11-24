🧮 gRPC Calculator Project

Course: Distributed Systems
Topic: Remote Procedure Calls (RPC) with gRPC
Language: Python 3.8+
Author: Abdel Hady Chakaroun

🚀 Project Overview

This project implements a remote calculator service using gRPC in Python.
It demonstrates how distributed systems communicate through Remote Procedure Calls (RPCs) and exchange data using Protocol Buffers (protobufs).

The project supports basic arithmetic operations, extended mathematical operations, and robust error handling.

🧩 Features
✅ Supported Operations

Addition (+)

Subtraction (−)

Multiplication (×)

Division (÷)

Modulus (%)

Power (^)

Square Root (√)

✅ Additional Functionalities

Logarithm (log)

Sine (sin)

Cosine (cos)

Robust error handling (division by zero, invalid inputs, negative sqrt, etc.)

Logging of all client requests and results in server_log.txt

Clean, modular Python code

Optional asynchronous server using grpc.aio for improved performance (Bonus)

⚙️ Requirements

Python: 3.8 or higher

Dependencies:

pip install grpcio grpcio-tools

🛠️ Project Structure
grpc_calculator/
│
├── calculator.proto         # Service definition
├── calculator_pb2.py        # Auto-generated from proto
├── calculator_pb2_grpc.py   # Auto-generated from proto
├── server.py                # Synchronous server
├── server_async.py          # Asynchronous server (Bonus)
├── client.py
├── server_log.txt           # Logs all requests and results
├── README.md
└── venv/                    # Virtual environment

🧠 How to Run
1️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

2️⃣ Install dependencies
pip install grpcio grpcio-tools

3️⃣ Compile the protobuf file
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

4️⃣ Run the server

Synchronous version:

python server.py


Asynchronous version (Bonus):

python server_async.py


Expected output:

🚀 GRPC Calculator Server Running on port 50051

5️⃣ Run the client (in a new terminal)
python client.py

🖥 Example Interaction
Select operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (×)
4. Division (÷)
5. Power (^)
6. Square Root (√)
7. Modulus (mod)
8. Logarithm (log)
9. Sine (sin)
10. Cosine (cos)
11. Exit

Enter choice: 5
Enter first number: 2
Enter second number: 8
➡️ Result: 256.0

🪵 Logging

All server activity — including requests, results, and errors — is automatically saved in server_log.txt.

Example log entries:

2025-11-23 16:12:01,234 - INFO - Power: 2.0^8.0 = 256.0
2025-11-23 16:12:10,567 - WARNING - Divide by zero: 5.0 / 0.0

✨ Bonus Features

Extended mathematical operations (%, ^, √, log, sin, cos)

Asynchronous server using grpc.aio

Request logging system

Exception-safe input validation

📦 Submission Instructions

Compress the project into a single ZIP archive:

zip -r grpc_calculator.zip *


Then submit the ZIP file via email or the required submission method.

✅ Example Output
🚀 GRPC Calculator Server Running on port 50051
Select operation: 6
Enter number: 25
➡️ Result: 5.0

🧑‍💻 Author

Name: Abdel Hady Chakaroun
University: Lebanese University
Date: 23/11/2025

🧾 License

This project is provided for academic use only as part of the Distributed Systems coursework.
Unauthorized distribution or reuse outside coursework is prohibited.