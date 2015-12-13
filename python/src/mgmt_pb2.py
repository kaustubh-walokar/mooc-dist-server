# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mgmt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mgmt.proto',
  package='',
  serialized_pb=_b('\n\nmgmt.proto\"\x1d\n\tHeartbeat\x12\x10\n\x08time_ref\x18\x02 \x02(\x03\"\xc3\x01\n\x07Network\x12\x14\n\x0c\x66rom_node_id\x18\x01 \x02(\x05\x12\x12\n\nto_node_id\x18\x02 \x02(\x05\x12&\n\x06\x61\x63tion\x18\x03 \x02(\x0e\x32\x16.Network.NetworkAction\"f\n\rNetworkAction\x12\x0c\n\x08NODEJOIN\x10\x01\x12\r\n\tNODELEAVE\x10\x02\x12\x0c\n\x08NODEDEAD\x10\x03\x12\r\n\tCREATEMAP\x10\x37\x12\x0c\n\x08\x41NNOUNCE\x10\x38\x12\r\n\x08SHUTDOWN\x10\xe7\x07\"\xba\x02\n\x0eLeaderElection\x12\x16\n\x0elast_log_index\x18\x01 \x02(\x05\x12\x0f\n\x07term_id\x18\x02 \x02(\x05\x12\x14\n\x0c\x63\x61ndidate_id\x18\x03 \x02(\x05\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12+\n\x06\x61\x63tion\x18\x05 \x02(\x0e\x32\x1b.LeaderElection.ElectAction\x12\x13\n\x07\x65xpires\x18\x06 \x01(\x03:\x02-1\x12\x10\n\x04hops\x18\x07 \x01(\x05:\x02-1\"\x86\x01\n\x0b\x45lectAction\x12\x13\n\x0f\x44\x45\x43LAREELECTION\x10\x01\x12\x0c\n\x08NOMINATE\x10\x02\x12\x0b\n\x07\x41\x42STAIN\x10\x03\x12\x11\n\rDECLAREWINNER\x10\x04\x12\x0f\n\x0b\x44\x45\x43LAREVOID\x10\x05\x12\x12\n\x0eWHOISTHELEADER\x10\x06\x12\x0f\n\x0bTHELEADERIS\x10\x07\"\x80\x02\n\x0cVotingBallot\x12\x11\n\tballot_id\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x02(\t\x12/\n\rballot_format\x18\x03 \x02(\x0e\x32\x18.VotingBallot.BallotType\x12\x13\n\x0b\x65xpires_sec\x18\x06 \x01(\x03\x12\x15\n\rmargin_to_win\x18\x07 \x01(\x05\x12\x14\n\x08max_hops\x18\x08 \x01(\x05:\x02-1\"\\\n\nBallotType\x12\x12\n\x0eSIMPLEMAJORITY\x10\x01\x12\x1b\n\x17TIMECONSTRAINEDMAJORITY\x10\x02\x12\n\n\x06RANKED\x10\x03\x12\x11\n\rINSTANTRUNOFF\x10\x04\"O\n\nVotingCast\x12\r\n\x05voter\x18\x01 \x02(\t\x12\x11\n\tballot_id\x18\x02 \x02(\t\x12\x11\n\tcandidate\x18\n \x01(\x05\x12\x0c\n\x04rank\x18\x0b \x01(\x05\"\x90\x01\n\x0cVotingStatus\x12\x11\n\tballot_id\x18\x01 \x02(\t\x12(\n\x06status\x18\x02 \x02(\x0e\x32\x18.VotingStatus.VoteStatus\x12\x0e\n\x06winner\x18\x03 \x01(\x05\"3\n\nVoteStatus\x12\x13\n\x0f\x42\x41LLOTABANDONED\x10\x01\x12\x10\n\x0c\x42\x41LLOTWINNER\x10\x02\"=\n\x0bVectorClock\x12\x0f\n\x07node_id\x18\x01 \x02(\x05\x12\x0f\n\x07version\x18\x02 \x02(\x05\x12\x0c\n\x04time\x18\x03 \x02(\x03\"p\n\nMgmtHeader\x12\x12\n\noriginator\x18\x02 \x02(\x05\x12\x14\n\x0csecurityCode\x18\x03 \x02(\x05\x12\x0c\n\x04time\x18\x04 \x02(\x03\x12\x1a\n\x04path\x18\x07 \x03(\x0b\x32\x0c.VectorClock\x12\x0e\n\x06toNode\x18\x08 \x01(\x05\"\xe8\x01\n\nManagement\x12\x1b\n\x06header\x18\x01 \x02(\x0b\x32\x0b.MgmtHeader\x12\x17\n\x05graph\x18\x02 \x01(\x0b\x32\x08.Network\x12\x18\n\x04\x62\x65\x61t\x18\x03 \x01(\x0b\x32\n.Heartbeat\x12!\n\x08\x65lection\x18\x04 \x01(\x0b\x32\x0f.LeaderElection\x12#\n\x0cvote_declare\x18\x07 \x01(\x0b\x32\r.VotingBallot\x12\x1e\n\tvote_cast\x18\x08 \x01(\x0b\x32\x0b.VotingCast\x12\"\n\x0bvote_status\x18\t \x01(\x0b\x32\r.VotingStatus\"\xd1\x03\n\rClientMessage\x12\r\n\x05msgId\x18\x01 \x01(\t\x12\x10\n\x08senderId\x18\x02 \x01(\x05\x12\x12\n\nreceiverId\x18\x03 \x01(\x05\x12\x19\n\x07\x64\x65tails\x18\x04 \x01(\x0b\x32\x08.Details\x12\x35\n\rfunctionality\x18\x05 \x01(\x0e\x32\x1e.ClientMessage.Functionalities\x12/\n\x0bmessageType\x18\x06 \x01(\x0e\x32\x1a.ClientMessage.MessageType\x12/\n\x0brequestType\x18\x07 \x01(\x0e\x32\x1a.ClientMessage.RequestType\x12 \n\x11\x62roadcastInternal\x18\x08 \x01(\x08:\x05\x66\x61lse\"\'\n\x0bMessageType\x12\x0b\n\x07REQUEST\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\" \n\x0bRequestType\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01\"j\n\x0f\x46unctionalities\x12\x0c\n\x08GETSUSER\x10\x01\x12\x18\n\x14GETCOURSEDESCRIPTION\x10\x02\x12\x0b\n\x07\x41\x44\x44USER\x10\x03\x12\r\n\tADDCOURSE\x10\x04\x12\x13\n\x0f\x41\x44\x44\x43OURSETOUSER\x10\x05\"T\n\x07\x44\x65tails\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x11\n\tcourse_id\x18\x03 \x01(\x05\x12\x13\n\x0b\x63ourse_name\x18\x04 \x01(\tB\r\n\tpoke.coreH\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_NETWORK_NETWORKACTION = _descriptor.EnumDescriptor(
  name='NetworkAction',
  full_name='Network.NetworkAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NODEJOIN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODELEAVE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODEDEAD', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATEMAP', index=3, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANNOUNCE', index=4, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=5, number=999,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=139,
  serialized_end=241,
)
_sym_db.RegisterEnumDescriptor(_NETWORK_NETWORKACTION)

_LEADERELECTION_ELECTACTION = _descriptor.EnumDescriptor(
  name='ElectAction',
  full_name='LeaderElection.ElectAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DECLAREELECTION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOMINATE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABSTAIN', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLAREWINNER', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLAREVOID', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHOISTHELEADER', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THELEADERIS', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=424,
  serialized_end=558,
)
_sym_db.RegisterEnumDescriptor(_LEADERELECTION_ELECTACTION)

_VOTINGBALLOT_BALLOTTYPE = _descriptor.EnumDescriptor(
  name='BallotType',
  full_name='VotingBallot.BallotType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIMPLEMAJORITY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMECONSTRAINEDMAJORITY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTANTRUNOFF', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=725,
  serialized_end=817,
)
_sym_db.RegisterEnumDescriptor(_VOTINGBALLOT_BALLOTTYPE)

_VOTINGSTATUS_VOTESTATUS = _descriptor.EnumDescriptor(
  name='VoteStatus',
  full_name='VotingStatus.VoteStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BALLOTABANDONED', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALLOTWINNER', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=994,
  serialized_end=1045,
)
_sym_db.RegisterEnumDescriptor(_VOTINGSTATUS_VOTESTATUS)

_CLIENTMESSAGE_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='ClientMessage.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1744,
  serialized_end=1783,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMESSAGE_MESSAGETYPE)

_CLIENTMESSAGE_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='ClientMessage.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1785,
  serialized_end=1817,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMESSAGE_REQUESTTYPE)

_CLIENTMESSAGE_FUNCTIONALITIES = _descriptor.EnumDescriptor(
  name='Functionalities',
  full_name='ClientMessage.Functionalities',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GETSUSER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GETCOURSEDESCRIPTION', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDUSER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDCOURSE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDCOURSETOUSER', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1819,
  serialized_end=1925,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMESSAGE_FUNCTIONALITIES)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_ref', full_name='Heartbeat.time_ref', index=0,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=43,
)


_NETWORK = _descriptor.Descriptor(
  name='Network',
  full_name='Network',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_node_id', full_name='Network.from_node_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_node_id', full_name='Network.to_node_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='Network.action', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORK_NETWORKACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=241,
)


_LEADERELECTION = _descriptor.Descriptor(
  name='LeaderElection',
  full_name='LeaderElection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_log_index', full_name='LeaderElection.last_log_index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='term_id', full_name='LeaderElection.term_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candidate_id', full_name='LeaderElection.candidate_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='LeaderElection.desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='LeaderElection.action', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expires', full_name='LeaderElection.expires', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hops', full_name='LeaderElection.hops', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEADERELECTION_ELECTACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=558,
)


_VOTINGBALLOT = _descriptor.Descriptor(
  name='VotingBallot',
  full_name='VotingBallot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ballot_id', full_name='VotingBallot.ballot_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='VotingBallot.desc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ballot_format', full_name='VotingBallot.ballot_format', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expires_sec', full_name='VotingBallot.expires_sec', index=3,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='margin_to_win', full_name='VotingBallot.margin_to_win', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_hops', full_name='VotingBallot.max_hops', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VOTINGBALLOT_BALLOTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=817,
)


_VOTINGCAST = _descriptor.Descriptor(
  name='VotingCast',
  full_name='VotingCast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voter', full_name='VotingCast.voter', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ballot_id', full_name='VotingCast.ballot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candidate', full_name='VotingCast.candidate', index=2,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='VotingCast.rank', index=3,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=898,
)


_VOTINGSTATUS = _descriptor.Descriptor(
  name='VotingStatus',
  full_name='VotingStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ballot_id', full_name='VotingStatus.ballot_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='VotingStatus.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='winner', full_name='VotingStatus.winner', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VOTINGSTATUS_VOTESTATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=1045,
)


_VECTORCLOCK = _descriptor.Descriptor(
  name='VectorClock',
  full_name='VectorClock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='VectorClock.node_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='VectorClock.version', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='VectorClock.time', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1047,
  serialized_end=1108,
)


_MGMTHEADER = _descriptor.Descriptor(
  name='MgmtHeader',
  full_name='MgmtHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='originator', full_name='MgmtHeader.originator', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='securityCode', full_name='MgmtHeader.securityCode', index=1,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='MgmtHeader.time', index=2,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='MgmtHeader.path', index=3,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toNode', full_name='MgmtHeader.toNode', index=4,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1110,
  serialized_end=1222,
)


_MANAGEMENT = _descriptor.Descriptor(
  name='Management',
  full_name='Management',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Management.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph', full_name='Management.graph', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beat', full_name='Management.beat', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='election', full_name='Management.election', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vote_declare', full_name='Management.vote_declare', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vote_cast', full_name='Management.vote_cast', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vote_status', full_name='Management.vote_status', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1225,
  serialized_end=1457,
)


_CLIENTMESSAGE = _descriptor.Descriptor(
  name='ClientMessage',
  full_name='ClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgId', full_name='ClientMessage.msgId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='senderId', full_name='ClientMessage.senderId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiverId', full_name='ClientMessage.receiverId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='details', full_name='ClientMessage.details', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functionality', full_name='ClientMessage.functionality', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messageType', full_name='ClientMessage.messageType', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requestType', full_name='ClientMessage.requestType', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broadcastInternal', full_name='ClientMessage.broadcastInternal', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTMESSAGE_MESSAGETYPE,
    _CLIENTMESSAGE_REQUESTTYPE,
    _CLIENTMESSAGE_FUNCTIONALITIES,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1460,
  serialized_end=1925,
)


_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='Details.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='Details.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='course_id', full_name='Details.course_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='course_name', full_name='Details.course_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1927,
  serialized_end=2011,
)

_NETWORK.fields_by_name['action'].enum_type = _NETWORK_NETWORKACTION
_NETWORK_NETWORKACTION.containing_type = _NETWORK
_LEADERELECTION.fields_by_name['action'].enum_type = _LEADERELECTION_ELECTACTION
_LEADERELECTION_ELECTACTION.containing_type = _LEADERELECTION
_VOTINGBALLOT.fields_by_name['ballot_format'].enum_type = _VOTINGBALLOT_BALLOTTYPE
_VOTINGBALLOT_BALLOTTYPE.containing_type = _VOTINGBALLOT
_VOTINGSTATUS.fields_by_name['status'].enum_type = _VOTINGSTATUS_VOTESTATUS
_VOTINGSTATUS_VOTESTATUS.containing_type = _VOTINGSTATUS
_MGMTHEADER.fields_by_name['path'].message_type = _VECTORCLOCK
_MANAGEMENT.fields_by_name['header'].message_type = _MGMTHEADER
_MANAGEMENT.fields_by_name['graph'].message_type = _NETWORK
_MANAGEMENT.fields_by_name['beat'].message_type = _HEARTBEAT
_MANAGEMENT.fields_by_name['election'].message_type = _LEADERELECTION
_MANAGEMENT.fields_by_name['vote_declare'].message_type = _VOTINGBALLOT
_MANAGEMENT.fields_by_name['vote_cast'].message_type = _VOTINGCAST
_MANAGEMENT.fields_by_name['vote_status'].message_type = _VOTINGSTATUS
_CLIENTMESSAGE.fields_by_name['details'].message_type = _DETAILS
_CLIENTMESSAGE.fields_by_name['functionality'].enum_type = _CLIENTMESSAGE_FUNCTIONALITIES
_CLIENTMESSAGE.fields_by_name['messageType'].enum_type = _CLIENTMESSAGE_MESSAGETYPE
_CLIENTMESSAGE.fields_by_name['requestType'].enum_type = _CLIENTMESSAGE_REQUESTTYPE
_CLIENTMESSAGE_MESSAGETYPE.containing_type = _CLIENTMESSAGE
_CLIENTMESSAGE_REQUESTTYPE.containing_type = _CLIENTMESSAGE
_CLIENTMESSAGE_FUNCTIONALITIES.containing_type = _CLIENTMESSAGE
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['Network'] = _NETWORK
DESCRIPTOR.message_types_by_name['LeaderElection'] = _LEADERELECTION
DESCRIPTOR.message_types_by_name['VotingBallot'] = _VOTINGBALLOT
DESCRIPTOR.message_types_by_name['VotingCast'] = _VOTINGCAST
DESCRIPTOR.message_types_by_name['VotingStatus'] = _VOTINGSTATUS
DESCRIPTOR.message_types_by_name['VectorClock'] = _VECTORCLOCK
DESCRIPTOR.message_types_by_name['MgmtHeader'] = _MGMTHEADER
DESCRIPTOR.message_types_by_name['Management'] = _MANAGEMENT
DESCRIPTOR.message_types_by_name['ClientMessage'] = _CLIENTMESSAGE
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEAT,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:Heartbeat)
  ))
_sym_db.RegisterMessage(Heartbeat)

Network = _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), dict(
  DESCRIPTOR = _NETWORK,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:Network)
  ))
_sym_db.RegisterMessage(Network)

LeaderElection = _reflection.GeneratedProtocolMessageType('LeaderElection', (_message.Message,), dict(
  DESCRIPTOR = _LEADERELECTION,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:LeaderElection)
  ))
_sym_db.RegisterMessage(LeaderElection)

VotingBallot = _reflection.GeneratedProtocolMessageType('VotingBallot', (_message.Message,), dict(
  DESCRIPTOR = _VOTINGBALLOT,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:VotingBallot)
  ))
_sym_db.RegisterMessage(VotingBallot)

VotingCast = _reflection.GeneratedProtocolMessageType('VotingCast', (_message.Message,), dict(
  DESCRIPTOR = _VOTINGCAST,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:VotingCast)
  ))
_sym_db.RegisterMessage(VotingCast)

VotingStatus = _reflection.GeneratedProtocolMessageType('VotingStatus', (_message.Message,), dict(
  DESCRIPTOR = _VOTINGSTATUS,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:VotingStatus)
  ))
_sym_db.RegisterMessage(VotingStatus)

VectorClock = _reflection.GeneratedProtocolMessageType('VectorClock', (_message.Message,), dict(
  DESCRIPTOR = _VECTORCLOCK,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:VectorClock)
  ))
_sym_db.RegisterMessage(VectorClock)

MgmtHeader = _reflection.GeneratedProtocolMessageType('MgmtHeader', (_message.Message,), dict(
  DESCRIPTOR = _MGMTHEADER,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:MgmtHeader)
  ))
_sym_db.RegisterMessage(MgmtHeader)

Management = _reflection.GeneratedProtocolMessageType('Management', (_message.Message,), dict(
  DESCRIPTOR = _MANAGEMENT,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:Management)
  ))
_sym_db.RegisterMessage(Management)

ClientMessage = _reflection.GeneratedProtocolMessageType('ClientMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMESSAGE,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:ClientMessage)
  ))
_sym_db.RegisterMessage(ClientMessage)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), dict(
  DESCRIPTOR = _DETAILS,
  __module__ = 'mgmt_pb2'
  # @@protoc_insertion_point(class_scope:Details)
  ))
_sym_db.RegisterMessage(Details)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\tpoke.coreH\001'))
# @@protoc_insertion_point(module_scope)
