# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import micro_services.ApiGateWay.clients.sheet.sheet_pb2 as sheet__pb2


class SheetAppenderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppendSheet = channel.unary_unary(
                '/SheetWorkerService.SheetAppenderService/AppendSheet',
                request_serializer=sheet__pb2.AppendSheetRequest.SerializeToString,
                response_deserializer=sheet__pb2.AppendSheetResponse.FromString,
                )
        self.AppendRecord = channel.unary_unary(
                '/SheetWorkerService.SheetAppenderService/AppendRecord',
                request_serializer=sheet__pb2.AppendRecordRequest.SerializeToString,
                response_deserializer=sheet__pb2.AppendRecordResponse.FromString,
                )
        self.UpdateRecord = channel.unary_unary(
                '/SheetWorkerService.SheetAppenderService/UpdateRecord',
                request_serializer=sheet__pb2.UpdateRecordRequest.SerializeToString,
                response_deserializer=sheet__pb2.UpdateRecordResponse.FromString,
                )


class SheetAppenderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AppendSheet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppendRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SheetAppenderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AppendSheet': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendSheet,
                    request_deserializer=sheet__pb2.AppendSheetRequest.FromString,
                    response_serializer=sheet__pb2.AppendSheetResponse.SerializeToString,
            ),
            'AppendRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendRecord,
                    request_deserializer=sheet__pb2.AppendRecordRequest.FromString,
                    response_serializer=sheet__pb2.AppendRecordResponse.SerializeToString,
            ),
            'UpdateRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRecord,
                    request_deserializer=sheet__pb2.UpdateRecordRequest.FromString,
                    response_serializer=sheet__pb2.UpdateRecordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SheetWorkerService.SheetAppenderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SheetAppenderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AppendSheet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SheetWorkerService.SheetAppenderService/AppendSheet',
            sheet__pb2.AppendSheetRequest.SerializeToString,
            sheet__pb2.AppendSheetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppendRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SheetWorkerService.SheetAppenderService/AppendRecord',
            sheet__pb2.AppendRecordRequest.SerializeToString,
            sheet__pb2.AppendRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SheetWorkerService.SheetAppenderService/UpdateRecord',
            sheet__pb2.UpdateRecordRequest.SerializeToString,
            sheet__pb2.UpdateRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SheetReaderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadLine = channel.unary_unary(
                '/SheetWorkerService.SheetReaderService/ReadLine',
                request_serializer=sheet__pb2.ReadLineRequest.SerializeToString,
                response_deserializer=sheet__pb2.ReadLineResponse.FromString,
                )
        self.ReadRange = channel.unary_unary(
                '/SheetWorkerService.SheetReaderService/ReadRange',
                request_serializer=sheet__pb2.ReadRangeRequest.SerializeToString,
                response_deserializer=sheet__pb2.ReadRangeResponse.FromString,
                )


class SheetReaderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadLine(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SheetReaderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadLine': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadLine,
                    request_deserializer=sheet__pb2.ReadLineRequest.FromString,
                    response_serializer=sheet__pb2.ReadLineResponse.SerializeToString,
            ),
            'ReadRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadRange,
                    request_deserializer=sheet__pb2.ReadRangeRequest.FromString,
                    response_serializer=sheet__pb2.ReadRangeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SheetWorkerService.SheetReaderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SheetReaderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadLine(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SheetWorkerService.SheetReaderService/ReadLine',
            sheet__pb2.ReadLineRequest.SerializeToString,
            sheet__pb2.ReadLineResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SheetWorkerService.SheetReaderService/ReadRange',
            sheet__pb2.ReadRangeRequest.SerializeToString,
            sheet__pb2.ReadRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
