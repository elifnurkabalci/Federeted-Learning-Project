# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from myproject import service_pb2 as myproject_dot_service__pb2


class MyServiceStub(object):
    """define the service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MyMethod = channel.unary_unary(
                '/myservice.MyService/MyMethod',
                request_serializer=myproject_dot_service__pb2.MyRequest.SerializeToString,
                response_deserializer=myproject_dot_service__pb2.MyResponse.FromString,
                )


class MyServiceServicer(object):
    """define the service
    """

    def MyMethod(self, request, context):
        """define the MyMethod function
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MyMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.MyMethod,
                    request_deserializer=myproject_dot_service__pb2.MyRequest.FromString,
                    response_serializer=myproject_dot_service__pb2.MyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'myservice.MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """define the service
    """

    @staticmethod
    def MyMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/myservice.MyService/MyMethod',
            myproject_dot_service__pb2.MyRequest.SerializeToString,
            myproject_dot_service__pb2.MyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)