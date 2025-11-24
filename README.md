# 🧮 gRPC Calculator Project

**Course**: Distributed Systems  
**Topic**: Remote Procedure Calls (RPC) with gRPC  
**Language**: Python 3.8+  
**Author**: Abdel Hady Chakaroun  

---

## 🚀 Project Overview

This project implements a remote calculator service using gRPC in Python.  
It demonstrates how distributed systems communicate through Remote Procedure Calls (RPCs) and exchange data using Protocol Buffers (protobufs).

The calculator supports basic arithmetic operations, extended mathematical functions, and robust error handling.

---

## 🧩 Features

### ✅ Supported Operations
- Addition (+)
- Subtraction (−)
- Multiplication (×)
- Division (÷)
- Modulus (%)
- Power (^)
- Square Root (√)

### ✅ Additional Functionalities
- Logarithm (log)
- Sine (sin)
- Cosine (cos)
- Robust error handling (e.g. divide by zero, invalid inputs, negative sqrt)
- Logging of all client requests and results in `server_log.txt`
- Clean, modular Python code
- Optional asynchronous server using `grpc.aio` (Bonus)

---

## ⚙️ Requirements

- Python 3.8 or higher  
- Dependencies:
  ```bash
  pip install grpcio grpcio-tools
🛠️ Project Structure
Code
grpc_calculator/
│
├── calculator.proto         # Service definition
├── calculator_pb2.py        # Auto-generated from proto
├── calculator_pb2_grpc.py   # Auto-generated from proto
├── server.py                # Synchronous server
├── server_async.py          # Asynchronous server (Bonus)
├── client.py                # gRPC client
├── server_log.txt           # Logs all requests and results
├── README.md
└── venv/                    # Virtual environment (excluded from GitHub)
🧠 How to Run
1️⃣ Create and activate virtual environment
bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
2️⃣ Install dependencies
bash
pip install grpcio grpcio-tools
3️⃣ Compile the protobuf file
bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
4️⃣ Run the server
Synchronous version:

bash
python server.py
Asynchronous version (Bonus):

bash
python server_async.py
Expected output:

Code
🚀 GRPC Calculator Server Running on port 50051
5️⃣ Run the client (in a new terminal)
bash
python client.py
🖥 Example Interaction
Code
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

Code
2025-11-23 16:12:01,234 - INFO - Power: 2.0^8.0 = 256.0
2025-11-23 16:12:10,567 - WARNING - Divide by zero: 5.0 / 0.0
✨ Bonus Features
Extended mathematical operations: %, ^, √, log, sin, cos

Asynchronous server using grpc.aio

Request logging system

Exception-safe input validation

📦 Submission Instructions
Compress the project into a single ZIP archive:

bash
zip -r grpc_calculator.zip *
Then submit the ZIP file via email or the required submission method.

✅ Example Output
Code
🚀 GRPC Calculator Server Running on port 50051
Select operation: 6
Enter number: 25
➡️ Result: 5.0
👨‍💻 Author
Name: Abdel Hady Chakaroun University: Lebanese University Date: 23/11/2025

🧾 License
This project is provided for academic use only as part of the Distributed Systems coursework. Unauthorized distribution or reuse outside coursework is prohibited.

Code

---

🚀 انسخ هيدا الملف وسجّله كـ `README.md` داخل مشروعك، وادفعه على GitHub.  
إذا بدك نضيف فقرة عن Docker Hub أو التجربة الموزعة بين جهازين، فيني أضيفها كمان. تحب؟
عطيني readme شامل كل شي من بعد ما رفعنا و خلصنا ووصلنا على github
أكيد يا هادي 👌، هيدي نسخة شاملة ومرتبة من ملف README.md بعد ما خلّصت المشروع، Docker، Docker Hub، ورفعته على GitHub. بتغطي كل شي: التشغيل، التوثيق، التجربة الموزعة، والـ bonus.

📄 README.md — النسخة النهائية الشاملة
markdown
# 🧮 gRPC Calculator

A distributed calculator application built with Python and gRPC.  
Supports basic and advanced operations via remote procedure calls (RPC), with deployment on Docker and Docker Hub.

---

## 📚 Course Info

- **Course**: Distributed Systems  
- **Topic**: Remote Procedure Calls (RPC) with gRPC  
- **Author**: Abdel Hady Chakaroun  
- **University**: Lebanese University  
- **Date**: 24/11/2025  

---

## 🚀 Project Overview

This project demonstrates how distributed systems communicate using gRPC and Protocol Buffers.  
It includes a client-server architecture, Dockerized containers, and a distributed demo across two laptops.

---

## 🧩 Features

### ✅ Supported Operations
- Addition (+)
- Subtraction (−)
- Multiplication (×)
- Division (÷)
- Modulus (%)
- Power (^)
- Square Root (√)
- Logarithm (log)
- Sine (sin)
- Cosine (cos)

### ✅ Additional Functionalities
- Robust error handling (e.g. divide by zero, invalid inputs, negative sqrt)
- Logging of all client requests and results in `server_log.txt`
- Optional asynchronous server using `grpc.aio` (bonus)
- Clean, modular Python code

---

## ⚙️ Requirements

- Python 3.8+  
- Dependencies:
  ```bash
  pip install grpcio grpcio-tools
🛠️ Project Structure
Code
grpc_calculator/
│
├── calculator.proto         # Service definition
├── calculator_pb2.py        # Auto-generated from proto
├── calculator_pb2_grpc.py   # Auto-generated from proto
├── server.py                # Synchronous server
├── server_async.py          # Asynchronous server (Bonus)
├── client.py                # gRPC client
├── server_log.txt           # Logs all requests and results
├── Dockerfile               # Container setup
├── docker-compose.yml       # Local orchestration
├── README.md
└── .gitignore               # Git exclusions
🧠 How to Run Locally
1️⃣ Create and activate virtual environment
bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
2️⃣ Install dependencies
bash
pip install grpcio grpcio-tools
3️⃣ Compile protobuf
bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
4️⃣ Run server
bash
python server.py
5️⃣ Run client
bash
python client.py
🐳 Run with Docker
Build and run locally
bash
docker-compose build
docker-compose up
Run from Docker Hub
bash
docker run -p 50051:50051 hadychakaroun/grpc-calculator-server:1.0
docker run -it hadychakaroun/grpc-calculator-client:1.0
🌍 Distributed Demo
To demonstrate remote execution across two machines:

Server runs on laptop in Ghazir:

bash
docker run -p 50051:50051 hadychakaroun/grpc-calculator-server:1.0
Client runs on friend's laptop in Beirut:

Edit client.py:

python
channel = grpc.insecure_channel("178.135.23.212:50051")
Run:

bash
docker run -it hadychakaroun/grpc-calculator-client:1.0
🖥 Example Interaction
Code
Select operation:
1. Addition (+)
...
Enter choice: 5
Enter first number: 2
Enter second number: 8
➡️ Result: 256.0
🪵 Logging
All server activity is saved in server_log.txt:

Code
2025-11-23 16:12:01 - INFO - Power: 2.0^8.0 = 256.0
2025-11-23 16:12:10 - WARNING - Divide by zero: 5.0 / 0.0
✨ Bonus Achieved
✅ Dockerized client and server

✅ Published on Docker Hub

✅ Distributed demo across two laptops

✅ Asynchronous server (grpc.aio)

✅ Logging and error handling

✅ Professional documentation and GitHub repo

📦 Submission Instructions
Compress the project:

bash
zip -r grpc_calculator.zip *
Submit via email or platform as required.

🧾 License
This project is provided for academic use only as part of the Distributed Systems coursework. Unauthorized distribution or reuse outside coursework is prohibited.
