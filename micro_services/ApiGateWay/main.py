
#python -m grpc_tools.protoc -I./protos --python_out=clients/bot --pyi_out=clients/bot --grpc_python_out=clients/bot protos/bot.proto
#python -m grpc_tools.protoc -I./protos --python_out=services/authorizer --grpc_python_out=services/authorizer protos/authorization.proto
#  python -m grpc_tools.protoc -I./protos --python_out=my_types --pyi_out=my_types/ --grpc_python_out=my_types/ protos/base_types.proto
from clients.bot.bot_client import *
if __name__ == "__main__":
    test()
