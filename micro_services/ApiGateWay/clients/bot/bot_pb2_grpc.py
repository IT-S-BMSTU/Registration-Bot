# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import my_types.base_types_pb2 as base__types__pb2
import clients.bot.bot_pb2 as bot__pb2


class BotGetterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBot = channel.unary_unary(
                '/BotGetter/GetBot',
                request_serializer=bot__pb2.GetBotRequest.SerializeToString,
                response_deserializer=base__types__pb2.BotResponse.FromString,
                )
        self.GetQuestion = channel.unary_unary(
                '/BotGetter/GetQuestion',
                request_serializer=bot__pb2.GetQuestionRequest.SerializeToString,
                response_deserializer=base__types__pb2.Module.FromString,
                )
        self.GetAllBots = channel.unary_unary(
                '/BotGetter/GetAllBots',
                request_serializer=bot__pb2.EmptyRequest.SerializeToString,
                response_deserializer=base__types__pb2.BotsResponse.FromString,
                )


class BotGetterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetQuestion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllBots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BotGetterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBot,
                    request_deserializer=bot__pb2.GetBotRequest.FromString,
                    response_serializer=base__types__pb2.BotResponse.SerializeToString,
            ),
            'GetQuestion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQuestion,
                    request_deserializer=bot__pb2.GetQuestionRequest.FromString,
                    response_serializer=base__types__pb2.Module.SerializeToString,
            ),
            'GetAllBots': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllBots,
                    request_deserializer=bot__pb2.EmptyRequest.FromString,
                    response_serializer=base__types__pb2.BotsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BotGetter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BotGetter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotGetter/GetBot',
            bot__pb2.GetBotRequest.SerializeToString,
            base__types__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetQuestion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotGetter/GetQuestion',
            bot__pb2.GetQuestionRequest.SerializeToString,
            base__types__pb2.Module.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllBots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotGetter/GetAllBots',
            bot__pb2.EmptyRequest.SerializeToString,
            base__types__pb2.BotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BotWorkerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBot = channel.unary_unary(
                '/BotWorker/CreateBot',
                request_serializer=bot__pb2.CreateBotRequest.SerializeToString,
                response_deserializer=bot__pb2.CreateBotResponse.FromString,
                )
        self.DeleteBot = channel.unary_unary(
                '/BotWorker/DeleteBot',
                request_serializer=bot__pb2.DeleteBotRequest.SerializeToString,
                response_deserializer=base__types__pb2.BaseResponse.FromString,
                )
        self.UpdateBotTgToken = channel.unary_unary(
                '/BotWorker/UpdateBotTgToken',
                request_serializer=bot__pb2.UpdateBotTgTokenRequest.SerializeToString,
                response_deserializer=base__types__pb2.BaseResponse.FromString,
                )
        self.UpdateBotGoogleToken = channel.unary_unary(
                '/BotWorker/UpdateBotGoogleToken',
                request_serializer=bot__pb2.UpdateBotGoogleTokenRequest.SerializeToString,
                response_deserializer=base__types__pb2.BaseResponse.FromString,
                )
        self.SetAnswers = channel.unary_unary(
                '/BotWorker/SetAnswers',
                request_serializer=bot__pb2.SetAnswersRequest.SerializeToString,
                response_deserializer=base__types__pb2.BaseResponse.FromString,
                )


class BotWorkerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBotTgToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBotGoogleToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAnswers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BotWorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBot': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBot,
                    request_deserializer=bot__pb2.CreateBotRequest.FromString,
                    response_serializer=bot__pb2.CreateBotResponse.SerializeToString,
            ),
            'DeleteBot': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBot,
                    request_deserializer=bot__pb2.DeleteBotRequest.FromString,
                    response_serializer=base__types__pb2.BaseResponse.SerializeToString,
            ),
            'UpdateBotTgToken': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBotTgToken,
                    request_deserializer=bot__pb2.UpdateBotTgTokenRequest.FromString,
                    response_serializer=base__types__pb2.BaseResponse.SerializeToString,
            ),
            'UpdateBotGoogleToken': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBotGoogleToken,
                    request_deserializer=bot__pb2.UpdateBotGoogleTokenRequest.FromString,
                    response_serializer=base__types__pb2.BaseResponse.SerializeToString,
            ),
            'SetAnswers': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAnswers,
                    request_deserializer=bot__pb2.SetAnswersRequest.FromString,
                    response_serializer=base__types__pb2.BaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BotWorker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BotWorker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotWorker/CreateBot',
            bot__pb2.CreateBotRequest.SerializeToString,
            bot__pb2.CreateBotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotWorker/DeleteBot',
            bot__pb2.DeleteBotRequest.SerializeToString,
            base__types__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBotTgToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotWorker/UpdateBotTgToken',
            bot__pb2.UpdateBotTgTokenRequest.SerializeToString,
            base__types__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBotGoogleToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotWorker/UpdateBotGoogleToken',
            bot__pb2.UpdateBotGoogleTokenRequest.SerializeToString,
            base__types__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAnswers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotWorker/SetAnswers',
            bot__pb2.SetAnswersRequest.SerializeToString,
            base__types__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
