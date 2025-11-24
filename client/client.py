import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        print("\n🧮 Advanced Calculator Client Started\n")

        while True:
            print("""
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
""")

            choice = input("Enter choice: ")

            if choice == "11":
                print("Exiting...")
                break

            try:
                if choice in ["6", "8", "9", "10"]:
                    a = float(input("Enter number: "))
                else:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))

                if choice == "1":
                    response = stub.Add(calculator_pb2.CalcRequest(number1=a, number2=b))
                elif choice == "2":
                    response = stub.Subtract(calculator_pb2.CalcRequest(number1=a, number2=b))
                elif choice == "3":
                    response = stub.Multiply(calculator_pb2.CalcRequest(number1=a, number2=b))
                elif choice == "4":
                    response = stub.Divide(calculator_pb2.CalcRequest(number1=a, number2=b))
                elif choice == "5":
                    response = stub.Power(calculator_pb2.CalcRequest(number1=a, number2=b))
                elif choice == "6":
                    response = stub.SquareRoot(calculator_pb2.SingleRequest(number=a))
                elif choice == "7":
                    response = stub.Modulus(calculator_pb2.CalcRequest(number1=a, number2=b))
                elif choice == "8":
                    response = stub.Log(calculator_pb2.SingleRequest(number=a))
                elif choice == "9":
                    response = stub.Sin(calculator_pb2.SingleRequest(number=a))
                elif choice == "10":
                    response = stub.Cos(calculator_pb2.SingleRequest(number=a))
                else:
                    print("❌ Invalid choice!")
                    continue

                print("➡️ Result:", response.result)

            except grpc.RpcError as e:
                print("❌ Error:", e.details())

if __name__ == "__main__":
    run()
