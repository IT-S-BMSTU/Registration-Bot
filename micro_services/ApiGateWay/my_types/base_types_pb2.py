# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62\x61se_types.proto\"+\n\x0c\x42\x61seResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"\xb0\x01\n\x0b\x42otResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08tg_token\x18\x02 \x01(\t\x12\x14\n\x0cgoogle_token\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\x05\x12\x15\n\rbot_survey_id\x18\x05 \x01(\x05\x12\x15\n\rstart_message\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\t\x12\x0c\n\x04\x63ode\x18\x08 \x01(\x05\x12\x13\n\x0b\x65nd_message\x18\t \x01(\t\"*\n\x0c\x42otsResponse\x12\x1a\n\x04\x62ots\x18\x01 \x03(\x0b\x32\x0c.BotResponse\"i\n\x06Module\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x13\n\x0b\x61nswer_type\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x18\n\x07\x62uttons\x18\x04 \x03(\x0b\x32\x07.Button\x12\x0f\n\x07next_id\x18\x05 \x01(\x05\"+\n\x06\x41nswer\x12\x11\n\tmodule_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61nswer\x18\x02 \x01(\t\"j\n\x07Journal\x12&\n\x07modules\x18\x01 \x03(\x0b\x32\x15.Journal.ModulesEntry\x1a\x37\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x16\n\x05value\x18\x02 \x01(\x0b\x32\x07.Module:\x02\x38\x01\";\n\x04User\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x03 \x01(\t\")\n\x06\x42utton\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\x0f\n\x07next_id\x18\x02 \x01(\x05\"`\n\x0cUserResponse\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _JOURNAL_MODULESENTRY._options = None
  _JOURNAL_MODULESENTRY._serialized_options = b'8\001'
  _globals['_BASERESPONSE']._serialized_start=20
  _globals['_BASERESPONSE']._serialized_end=63
  _globals['_BOTRESPONSE']._serialized_start=66
  _globals['_BOTRESPONSE']._serialized_end=242
  _globals['_BOTSRESPONSE']._serialized_start=244
  _globals['_BOTSRESPONSE']._serialized_end=286
  _globals['_MODULE']._serialized_start=288
  _globals['_MODULE']._serialized_end=393
  _globals['_ANSWER']._serialized_start=395
  _globals['_ANSWER']._serialized_end=438
  _globals['_JOURNAL']._serialized_start=440
  _globals['_JOURNAL']._serialized_end=546
  _globals['_JOURNAL_MODULESENTRY']._serialized_start=491
  _globals['_JOURNAL_MODULESENTRY']._serialized_end=546
  _globals['_USER']._serialized_start=548
  _globals['_USER']._serialized_end=607
  _globals['_BUTTON']._serialized_start=609
  _globals['_BUTTON']._serialized_end=650
  _globals['_USERRESPONSE']._serialized_start=652
  _globals['_USERRESPONSE']._serialized_end=748
# @@protoc_insertion_point(module_scope)
