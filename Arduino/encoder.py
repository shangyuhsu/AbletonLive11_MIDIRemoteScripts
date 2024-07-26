from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.elements import EncoderElement as EncoderElementBase
from .util import _LOG
from ableton.v2.control_surface.control import is_internal_parameter
SYSEX_START = 0xF0
SYSEX_END = 0xF7

CC_STATUS = 176
class CustomEncoderElement(EncoderElementBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._last_sent_parameter_message = None

    def notify_parameter_name(self):
        super().notify_parameter_name()
        self._send_parameter_feedback()

    def notify_parameter_value(self):
        super().notify_parameter_value()
        self._send_parameter_feedback()

    def clear_send_cache(self):
        super().clear_send_cache()
        self._last_sent_parameter_message = None

    def _send_parameter_feedback(self):
        ident = self.message_identifier()
        _LOG(f"{ident} | {self.parameter_name}={self.parameter_value}")

        midi_msg = (SYSEX_START,) + tuple(ord(char) for char in self.parameter_name) + (58, 32, ) + tuple(ord(char) for char in self.parameter_value) + (SYSEX_END,)
        _LOG(f"{midi_msg}")

        _LOG(f"{self.parameter} {is_internal_parameter(self.parameter)} {self._block_internal_parameter_feedback}")
        self._send_message(midi_msg)

        # midi_msg = (0xB0 | self._msg_channel,) + (1, ident, self.)
        # _LOG(f"{midi_msg}")

        # self._send_message(midi_msg)
        # if liveobj_valid(self._mapped_object):
        #     self._send_message(make_parameter_message(ident, self.parameter_name, self.parameter_value))
        # else:
        #     self._send_message(make_blank_parameter_message(ident))

    def _send_message(self, message):
        if message != self._last_sent_parameter_message:
            self.send_midi(message)
        self._last_sent_parameter_message = message

    def _parameter_value_changed(self):
        super()._parameter_value_changed()
        _LOG("PARAM VAL CHANGED")
# class RealigningEncoderElement(EncoderElement):

#     def __init__(self, *a, **k):
#         (super().__init__)(*a, **k)
#         self._sysex_header = ENCODER_VALUE_HEADER + (
#          ENCODER_ID_TO_SYSEX_ID[self.message_identifier()],
#          0)
#         self._last_mapped_value = None

#     def realign_value(self):
#         value_to_send = self._last_mapped_value or self._last_received_value or 0
#         self.send_midi(self._sysex_header + (value_to_send, SYSEX_END))

#     def receive_value(self, value):
#         super().receive_value(value)
#         self._last_mapped_value = None

#     def _parameter_value_changed(self):
#         if liveobj_valid(self._mapped_object):
#             self._last_mapped_value = parameter_value_to_midi_value(self._mapped_object)