# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobufs/cache.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protobufs/cache.proto\"\x0e\n\x0c\x45mptyMessage\"#\n\x14\x45mptyMessageresponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\x0bGetResponse\x12\r\n\x05value\x18\x01 \x01(\t\"(\n\nSetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1e\n\x0bSetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x45\n\x0c\x43\x61\x63heService\x12\x35\n\rPingpacientes\x12\r.EmptyMessage\x1a\x15.EmptyMessageresponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cache_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTYMESSAGE']._serialized_start=25
  _globals['_EMPTYMESSAGE']._serialized_end=39
  _globals['_EMPTYMESSAGERESPONSE']._serialized_start=41
  _globals['_EMPTYMESSAGERESPONSE']._serialized_end=76
  _globals['_GETREQUEST']._serialized_start=78
  _globals['_GETREQUEST']._serialized_end=103
  _globals['_GETRESPONSE']._serialized_start=105
  _globals['_GETRESPONSE']._serialized_end=133
  _globals['_SETREQUEST']._serialized_start=135
  _globals['_SETREQUEST']._serialized_end=175
  _globals['_SETRESPONSE']._serialized_start=177
  _globals['_SETRESPONSE']._serialized_end=207
  _globals['_CACHESERVICE']._serialized_start=209
  _globals['_CACHESERVICE']._serialized_end=278
# @@protoc_insertion_point(module_scope)
