import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
import math
import logging

# Logging configuration
logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def Add(self, request, context):
        result = request.number1 + request.number2
        logging.info(f"Add: {request.number1} + {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Subtract(self, request, context):
        result = request.number1 - request.number2
        logging.info(f"Subtract: {request.number1} - {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Multiply(self, request, context):
        result = request.number1 * request.number2
        logging.info(f"Multiply: {request.number1} * {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Divide(self, request, context):
        if request.number2 == 0:
            logging.warning(f"Divide by zero: {request.number1} / {request.number2}")
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Cannot divide by zero")
        result = request.number1 / request.number2
        logging.info(f"Divide: {request.number1} / {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Modulus(self, request, context):
        if request.number2 == 0:
            logging.warning(f"Modulus by zero: {request.number1} % {request.number2}")
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Cannot modulus by zero")
        result = request.number1 % request.number2
        logging.info(f"Modulus: {request.number1} % {request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Power(self, request, context):
        result = math.pow(request.number1, request.number2)
        logging.info(f"Power: {request.number1}^{request.number2} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def SquareRoot(self, request, context):
        if request.number < 0:
            logging.warning(f"SquareRoot invalid input: {request.number}")
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Cannot take sqrt of negative number")
        result = math.sqrt(request.number)
        logging.info(f"SquareRoot: √{request.number} = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Log(self, request, context):
        if request.number <= 0:
            logging.warning(f"Log invalid input: {request.number}")
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Log only for positive numbers")
        result = math.log(request.number)
        logging.info(f"Log: log({request.number}) = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Sin(self, request, context):
        result = math.sin(request.number)
        logging.info(f"Sin: sin({request.number}) = {result}")
        return calculator_pb2.CalcResponse(result=result)

    def Cos(self, request, context):
        result = math.cos(request.number)
        logging.info(f"Cos: cos({request.number}) = {result}")
        return calculator_pb2.CalcResponse(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("🚀 GRPC Calculator Server Running on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
