# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: myproject/service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='myproject/service.proto',
  package='myservice',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17myproject/service.proto\x12\tmyservice\"\x19\n\tMyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nMyResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2D\n\tMyService\x12\x37\n\x08MyMethod\x12\x14.myservice.MyRequest\x1a\x15.myservice.MyResponseb\x06proto3'
)




_MYREQUEST = _descriptor.Descriptor(
  name='MyRequest',
  full_name='myservice.MyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='myservice.MyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=63,
)


_MYRESPONSE = _descriptor.Descriptor(
  name='MyResponse',
  full_name='myservice.MyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='myservice.MyResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['MyRequest'] = _MYREQUEST
DESCRIPTOR.message_types_by_name['MyResponse'] = _MYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MyRequest = _reflection.GeneratedProtocolMessageType('MyRequest', (_message.Message,), {
  'DESCRIPTOR' : _MYREQUEST,
  '__module__' : 'myproject.service_pb2'
  # @@protoc_insertion_point(class_scope:myservice.MyRequest)
  })
_sym_db.RegisterMessage(MyRequest)

MyResponse = _reflection.GeneratedProtocolMessageType('MyResponse', (_message.Message,), {
  'DESCRIPTOR' : _MYRESPONSE,
  '__module__' : 'myproject.service_pb2'
  # @@protoc_insertion_point(class_scope:myservice.MyResponse)
  })
_sym_db.RegisterMessage(MyResponse)



_MYSERVICE = _descriptor.ServiceDescriptor(
  name='MyService',
  full_name='myservice.MyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=96,
  serialized_end=164,
  methods=[
  _descriptor.MethodDescriptor(
    name='MyMethod',
    full_name='myservice.MyService.MyMethod',
    index=0,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MYSERVICE)

DESCRIPTOR.services_by_name['MyService'] = _MYSERVICE

# @@protoc_insertion_point(module_scope)
