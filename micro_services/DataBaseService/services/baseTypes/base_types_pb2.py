# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62\x61se_types.proto\"+\n\x0c\x42\x61seResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"$\n\x03\x42ot\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\tb\x06proto3')



_BASERESPONSE = DESCRIPTOR.message_types_by_name['BaseResponse']
_BOT = DESCRIPTOR.message_types_by_name['Bot']
BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASERESPONSE,
  '__module__' : 'base_types_pb2'
  # @@protoc_insertion_point(class_scope:BaseResponse)
  })
_sym_db.RegisterMessage(BaseResponse)

Bot = _reflection.GeneratedProtocolMessageType('Bot', (_message.Message,), {
  'DESCRIPTOR' : _BOT,
  '__module__' : 'base_types_pb2'
  # @@protoc_insertion_point(class_scope:Bot)
  })
_sym_db.RegisterMessage(Bot)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BASERESPONSE._serialized_start=20
  _BASERESPONSE._serialized_end=63
  _BOT._serialized_start=65
  _BOT._serialized_end=101
# @@protoc_insertion_point(module_scope)
