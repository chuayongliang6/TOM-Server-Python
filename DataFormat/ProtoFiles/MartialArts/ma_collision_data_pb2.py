# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ma_collision_data.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ma_vector_pb2 as ma__vector__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17ma_collision_data.proto\x1a\x0fma_vector.proto\"\xb6\x01\n\x0fMaCollisionData\x12\x1b\n\x08velocity\x18\x01 \x01(\x0b\x32\t.MaVector\x12\"\n\x0f\x63ollision_point\x18\x02 \x01(\x0b\x32\t.MaVector\x12\x1f\n\x0cpad_position\x18\x03 \x01(\x0b\x32\t.MaVector\x12\x1d\n\x12\x64istance_to_target\x18\x04 \x01(\x02:\x01\x30\x12\x10\n\x05\x61ngle\x18\x05 \x01(\x02:\x01\x30\x12\x10\n\x04hand\x18\x06 \x01(\x05:\x02-1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ma_collision_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MACOLLISIONDATA']._serialized_start=45
  _globals['_MACOLLISIONDATA']._serialized_end=227
# @@protoc_insertion_point(module_scope)
