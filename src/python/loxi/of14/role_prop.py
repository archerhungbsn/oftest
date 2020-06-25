# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
from . import util
import loxi.generic_util

import sys
ofp = sys.modules['loxi.of14']

class role_prop(loxi.OFObject):
    subtypes = {}


    def __init__(self, type=None):
        if type != None:
            self.type = type
        else:
            self.type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = role_prop.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = role_prop()
        obj.type = reader.read("!H")[0]
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("role_prop {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class experimenter(role_prop):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None, exp_type=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        if exp_type != None:
            self.exp_type = exp_type
        else:
            self.exp_type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 4)
        subclass = experimenter.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = experimenter()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        obj.experimenter = reader.read("!L")[0]
        obj.exp_type = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        if self.exp_type != other.exp_type: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("exp_type = ");
                q.text("%#x" % self.exp_type)
            q.breakable()
        q.text('}')

role_prop.subtypes[65535] = experimenter


