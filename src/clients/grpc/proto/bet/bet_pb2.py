# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: bet.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tbet.proto\x12\x03\x62\x65t"5\n\x11UpdateBetsRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t"\x14\n\x12UpdateBetsResponse2F\n\x03\x42\x65t\x12?\n\nUpdateBets\x12\x16.bet.UpdateBetsRequest\x1a\x17.bet.UpdateBetsResponse"\x00\x42\x07Z\x05./betb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bet_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z\005./bet"
    _globals["_UPDATEBETSREQUEST"]._serialized_start = 18
    _globals["_UPDATEBETSREQUEST"]._serialized_end = 71
    _globals["_UPDATEBETSRESPONSE"]._serialized_start = 73
    _globals["_UPDATEBETSRESPONSE"]._serialized_end = 93
    _globals["_BET"]._serialized_start = 95
    _globals["_BET"]._serialized_end = 165
# @@protoc_insertion_point(module_scope)
