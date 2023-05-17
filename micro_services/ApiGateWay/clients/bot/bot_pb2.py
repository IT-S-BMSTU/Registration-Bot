# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_types_pb2 as base__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tbot.proto\x1a\x10\x62\x61se_types.proto\".\n\rGetBotRequest\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\x05\x12\r\n\x05owner\x18\x02 \x01(\x05\"G\n\x17UpdateBotTgTokenRequest\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\x05\x12\r\n\x05owner\x18\x02 \x01(\x05\x12\r\n\x05token\x18\x03 \x01(\t\"K\n\x1bUpdateBotGoogleTokenRequest\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\x05\x12\r\n\x05owner\x18\x02 \x01(\x05\x12\r\n\x05token\x18\x03 \x01(\t\"h\n\x10\x43reateBotRequest\x12\x11\n\tfrom_user\x18\x01 \x01(\x05\x12\x10\n\x08tg_token\x18\x02 \x01(\t\x12\x14\n\x0csheets_token\x18\x03 \x01(\t\x12\x19\n\x07journal\x18\x04 \x01(\x0b\x32\x08.Journal\"5\n\x10\x44\x65leteBotRequest\x12\x11\n\tfrom_user\x18\x01 \x01(\x05\x12\x0e\n\x06\x62ot_id\x18\x02 \x01(\x05\"9\n\x12GetQuestionRequest\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\x05\x12\x13\n\x0bquestion_id\x18\x02 \x01(\x05\"Q\n\x11SetAnswersRequest\x12\x12\n\ntg_chat_id\x18\x01 \x01(\x03\x12\x0e\n\x06\x62ot_id\x18\x02 \x01(\x05\x12\x18\n\x07\x61nswers\x18\x03 \x03(\x0b\x32\x07.Answer\"@\n\x11\x43reateBotResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0e\n\x06\x62ot_id\x18\x03 \x01(\x05\x32`\n\tBotGetter\x12&\n\x06GetBot\x12\x0e.GetBotRequest\x1a\x0c.BotResponse\x12+\n\x0bGetQuestion\x12\x13.GetQuestionRequest\x1a\x07.Module2\xa1\x02\n\tBotWorker\x12\x32\n\tCreateBot\x12\x11.CreateBotRequest\x1a\x12.CreateBotResponse\x12-\n\tDeleteBot\x12\x11.DeleteBotRequest\x1a\r.BaseResponse\x12;\n\x10UpdateBotTgToken\x12\x18.UpdateBotTgTokenRequest\x1a\r.BaseResponse\x12\x43\n\x14UpdateBotGoogleToken\x12\x1c.UpdateBotGoogleTokenRequest\x1a\r.BaseResponse\x12/\n\nSetAnswers\x12\x12.SetAnswersRequest\x1a\r.BaseResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETBOTREQUEST._serialized_start=31
  _GETBOTREQUEST._serialized_end=77
  _UPDATEBOTTGTOKENREQUEST._serialized_start=79
  _UPDATEBOTTGTOKENREQUEST._serialized_end=150
  _UPDATEBOTGOOGLETOKENREQUEST._serialized_start=152
  _UPDATEBOTGOOGLETOKENREQUEST._serialized_end=227
  _CREATEBOTREQUEST._serialized_start=229
  _CREATEBOTREQUEST._serialized_end=333
  _DELETEBOTREQUEST._serialized_start=335
  _DELETEBOTREQUEST._serialized_end=388
  _GETQUESTIONREQUEST._serialized_start=390
  _GETQUESTIONREQUEST._serialized_end=447
  _SETANSWERSREQUEST._serialized_start=449
  _SETANSWERSREQUEST._serialized_end=530
  _CREATEBOTRESPONSE._serialized_start=532
  _CREATEBOTRESPONSE._serialized_end=596
  _BOTGETTER._serialized_start=598
  _BOTGETTER._serialized_end=694
  _BOTWORKER._serialized_start=697
  _BOTWORKER._serialized_end=986
# @@protoc_insertion_point(module_scope)
