import grpc
import asyncio
import math
import logging
import server.calculator_pb2 as calculator_pb2
import server.calculator_pb2_grpc as calculator_pb2_grpc

# إعداد logging
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    async def Add(self, request, context):
        result = request.number1 + request.number2
        logging.info(f"Add: {request.number1} + {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    async def Subtract(self, request, context):
        result = request.number1 - request.number2
        logging.info(f"Subtract: {request.number1} - {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    async def Multiply(self, request, context):
        result = request.number1 * request.number2
        logging.info(f"Multiply: {request.number1} * {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    async def Divide(self, request, context):
        if request.number2 == 0:
            logging.error(f"Divide by zero attempted: {request.number1} / {request.number2}")
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Division by zero is not allowed.")
        result = request.number1 / request.number2
        logging.info(f"Divide: {request.number1} / {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    async def Modulus(self, request, context):
        if request.number2 == 0:
            logging.error(f"Modulus by zero attempted: {request.number1} % {request.number2}")
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Modulus by zero is not allowed.")
        result = request.number1 % request.number2
        logging.info(f"Modulus: {request.number1} % {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    async def Power(self, request, context):
        result = math.pow(request.number1, request.number2)
        logging.info(f"Power: {request.number1}^{request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    async def SquareRoot(self, request, context):
        if request.number1 < 0:
            logging.error(f"SquareRoot: invalid input {request.number1}")
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Cannot compute square root of a negative number.")
        result = math.sqrt(request.number1)
        logging.info(f"SquareRoot: √{request.number1} = {result}")
        return calculator_pb2.CalcResponse(result=result)

async def serve():
    server = grpc.aio.server()
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    print("✅ Async Server started on port 50051")
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
