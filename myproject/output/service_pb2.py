# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\tmyservice\"\x19\n\tMyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nMyResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2D\n\tMyService\x12\x37\n\x08MyMethod\x12\x14.myservice.MyRequest\x1a\x15.myservice.MyResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MYREQUEST._serialized_start=28
  _MYREQUEST._serialized_end=53
  _MYRESPONSE._serialized_start=55
  _MYRESPONSE._serialized_end=84
  _MYSERVICE._serialized_start=86
  _MYSERVICE._serialized_end=154
# @@protoc_insertion_point(module_scope)
