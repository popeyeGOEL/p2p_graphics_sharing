# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tasks_pb2 as tasks__pb2


class TaskServiceStub(object):
    """Define a service for handling GPU-related tasks and training sessions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RentAndStartSession = channel.unary_unary(
                '/tasks.TaskService/RentAndStartSession',
                request_serializer=tasks__pb2.RentAndStartSessionRequest.SerializeToString,
                response_deserializer=tasks__pb2.SessionResponse.FromString,
                )
        self.UpdateTraining = channel.unary_unary(
                '/tasks.TaskService/UpdateTraining',
                request_serializer=tasks__pb2.UpdateTrainingRequest.SerializeToString,
                response_deserializer=tasks__pb2.GenericResponse.FromString,
                )
        self.ChangeAggregator = channel.unary_unary(
                '/tasks.TaskService/ChangeAggregator',
                request_serializer=tasks__pb2.ChangeAggregatorRequest.SerializeToString,
                response_deserializer=tasks__pb2.GenericResponse.FromString,
                )
        self.ReleaseGPU = channel.unary_unary(
                '/tasks.TaskService/ReleaseGPU',
                request_serializer=tasks__pb2.ReleaseGPURequest.SerializeToString,
                response_deserializer=tasks__pb2.GenericResponse.FromString,
                )


class TaskServiceServicer(object):
    """Define a service for handling GPU-related tasks and training sessions
    """

    def RentAndStartSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTraining(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeAggregator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseGPU(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RentAndStartSession': grpc.unary_unary_rpc_method_handler(
                    servicer.RentAndStartSession,
                    request_deserializer=tasks__pb2.RentAndStartSessionRequest.FromString,
                    response_serializer=tasks__pb2.SessionResponse.SerializeToString,
            ),
            'UpdateTraining': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTraining,
                    request_deserializer=tasks__pb2.UpdateTrainingRequest.FromString,
                    response_serializer=tasks__pb2.GenericResponse.SerializeToString,
            ),
            'ChangeAggregator': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeAggregator,
                    request_deserializer=tasks__pb2.ChangeAggregatorRequest.FromString,
                    response_serializer=tasks__pb2.GenericResponse.SerializeToString,
            ),
            'ReleaseGPU': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseGPU,
                    request_deserializer=tasks__pb2.ReleaseGPURequest.FromString,
                    response_serializer=tasks__pb2.GenericResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tasks.TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """Define a service for handling GPU-related tasks and training sessions
    """

    @staticmethod
    def RentAndStartSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.TaskService/RentAndStartSession',
            tasks__pb2.RentAndStartSessionRequest.SerializeToString,
            tasks__pb2.SessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTraining(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.TaskService/UpdateTraining',
            tasks__pb2.UpdateTrainingRequest.SerializeToString,
            tasks__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeAggregator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.TaskService/ChangeAggregator',
            tasks__pb2.ChangeAggregatorRequest.SerializeToString,
            tasks__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseGPU(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.TaskService/ReleaseGPU',
            tasks__pb2.ReleaseGPURequest.SerializeToString,
            tasks__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
