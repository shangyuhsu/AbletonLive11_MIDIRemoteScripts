#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MPK249/MPK249.py
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.DrumRackComponent import DrumRackComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder, make_slider
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

from _Framework.DeviceComponent import DeviceComponent
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement

# from _UserScript.DeviceComponent import DeviceComponent
from _Generic.SpecialMixerComponent import SpecialMixerComponent
from _Framework.EncoderElement import EncoderElement

import Live

class MidiMap(MidiMapBase):

    def __init__(self, *a, **k):
        super(MidiMap, self).__init__(*a, **k)
        self.add_button(u'Play', 0, 118, MIDI_CC_TYPE)
        self.add_button(u'Record', 0, 119, MIDI_CC_TYPE)
        self.add_button(u'Stop', 0, 117, MIDI_CC_TYPE)
        self.add_button(u'Loop', 0, 114, MIDI_CC_TYPE)
        self.add_button(u'Forward', 0, 116, MIDI_CC_TYPE)
        self.add_button(u'Backward', 0, 115, MIDI_CC_TYPE)

        # self.add_button(u'Undo', 0, 121, MIDI_NOTE_TYPE)
        # self.add_button(u'Redo', 0, 122, MIDI_NOTE_TYPE)

        # self.add_matrix(u'Sliders', make_slider, 0, [[12,
        #   13,
        #   14,
        #   15,
        #   16,
        #   17,
        #     ]], MIDI_CC_TYPE)
        # self.add_matrix(u'Encoders', make_encoder, 0, [[22,
        #   23,
        #   24,
        #   25,
        #   26,
        #   27,
        #     ]], MIDI_CC_TYPE)

        # self.add_matrix(u'Drum_Pads', make_button, 1, [[81,
        #   83,
        #   84,
        #   86],
        #  [74,
        #   76,
        #   77,
        #   79],
        #  [67,
        #   69,
        #   71,
        #   72],
        #  [60,
        #   62,
        #   64,
        #   65]], MIDI_NOTE_TYPE)

        # self.add_matrix(u'Arm_Buttons', make_button, 0, [[52,
        #   53,
        #   54,
        #   55,
        #   56,
        #   57,
        # ]], MIDI_CC_TYPE)

def Pad(ch, midi_val, toggle=False):
    return ButtonElement(not toggle, MIDI_NOTE_TYPE, ch, midi_val)

def Knob(ch, midi_val):
    return EncoderElement(MIDI_CC_TYPE, ch, midi_val, Live.MidiMap.MapMode.relative_two_compliment)

def Button(ch, midi_val, toggle=True):
    return ButtonElement(not toggle, MIDI_CC_TYPE, ch, midi_val)

# class CustomDeviceComponent(DeviceComponent):
#     def __init__(self, *a, **k):
#          (super(CustomDeviceComponent, self).__init__)(*a, **k)

#          self.device_idx = 0

#     def _device_up_value(self, value):
#         if self.is_enabled():
#             if not self._device_up_button.is_momentary() or value is not 0:
#                 if liveobj_valid(self._device):
#                     num_banks = self._number_of_parameter_banks()
#                     if self._bank_down_button == None:
#                         self._bank_name = ''
#                         self._bank_index = (self._bank_index + 1) % num_banks if self._bank_index != None else 0
#                         self.update()
#         else:
#             pass

#         if self._bank_index == None or (num_banks > self._bank_index + 1):
#             self._bank_name = ''
#             self._bank_index = self._bank_index + 1 if self._bank_index != None else 0
#             self.update()

#     def _device_down_value(self, value):
#         if self.is_enabled():
#             if not self._device_down_button.is_momentary() or value is not 0:
#                 if liveobj_valid(self._device):
#                     if self._bank_index == None or self._bank_index > 0:
#                         self._bank_name = ''
#                         self._bank_index = self._bank_index - 1 if self._bank_index != None else max(0, self._number_of_parameter_banks() - 1)
#                         self.update()

#     def set_device_nav_buttons(self, down, up):
#         self._device_down_button = down
#         self._device_down_button_slot.subject = down

#         self._device_up_button = up
#         self._device_up_button_slot.subject = up
#         self.update()

#     def update_device_selection(self):
#         cur_idx = 0

#         view = self.song().view
#         track_or_chain = view.selected_chain if view.selected_chain else view.selected_track
        
#         devices = track_or_chain.devices

#         # Choose a device to select
#         device_to_select = None
#         if isinstance(track_or_chain, Live.Track.Track):
#             device_to_select = track_or_chain.view.selected_device
#         if not liveobj_valid(device_to_select):
#             if len(track_or_chain.devices) > 0:
#                 device_to_select = track_or_chain.devices[0]
#
#         # Set device
#         if liveobj_valid(device_to_select):
#             appointed_device = device_to_appoint(device_to_select)
#             view.select_device(device_to_select, False)
#             self.song().appointed_device = appointed_device
#             self.set_device(appointed_device)
#         else:
#             self.song().appointed_device = None
#             self.set_device(None)

# def get_idx_device(self):
#     view = self.song().view
#     track_or_chain = view.selected_chain if view.selected_chain else view.selected_track

#     devices = track_or_chain.devices

#     if len(devices) > self.device_idx:
#         return devices[self.device_idx]
#     else:
#         return None

# def device_inc(self):
#     view = self.song().view
#     track_or_chain = view.selected_chain if view.selected_chain else view.selected_track

#     devices = track_or_chain.devices

#     cur_device_idx = self.device_idx + 1
#     while cur_device_idx < len(devices):
#         device = devices[device_idx]
#         if liveobj_valid(device):
#             appointed_device = device_to_appoint(device)
#             view.select_device(device, False)
#             self.song().appointed_device = appointed_device
#             self.set_device(appointed_device)
#             break

#         cur_device_idx +=1

# def device_dec(self):
#     view = self.song().view
#     track_or_chain = view.selected_chain if view.selected_chain else view.selected_track

#     devices = track_or_chain.devices

#     cur_device_idx = self.device_idx -1
#     while cur_device_idx >=0 and cur_device_idx < len(devices):
#         device = devices[device_idx]
#         if liveobj_valid(device):
#             appointed_device = device_to_appoint(device)
#             view.select_device(device, False)
#             self.song().appointed_device = appointed_device
#             self.set_device(appointed_device)
#             break

#         cur_device_idx -=1

# def set_device_idx(self):
#     if self._device:
#         view = self.song().view
#         track_or_chain = view.selected_chain if view.selected_chain else view.selected_track

#         devices = track_or_chain.devices

#         for idx, device in enumerate(devices):
#             if device == self._device:
#                 self.device_idx = idx
#                 return
#     else:
#         self.device_idx = 0


class MPK249(ControlSurface):

    def __init__(self, *a, **k):
        super(MPK249, self).__init__(*a, **k)
        with self.component_guard():
            midimap = MidiMap()

            # drum_rack = DrumRackComponent(name=u'Drum_Rack', is_enabled=False, layer=Layer(pads=midimap[u'Drum_Pads']))
            # drum_rack.set_enabled(True)

            transport = TransportComponent(
                name=u'Transport',
                is_enabled=False,
                layer=Layer(
                    play_button=midimap[u'Play'],
                    record_button=midimap[u'Record'],
                    stop_button=midimap[u'Stop'],
                    loop_button=midimap[u'Loop'], 
                    # undo_button=midimap[u'Undo'],
                    # redo_button=midimap[u'Redo'],
                    seek_forward_button=midimap[u'Forward'],
                    seek_backward_button=midimap[u'Backward']
                )
            )
            transport.set_enabled(True)

            mixer_size = 6
            mixer = SpecialMixerComponent(mixer_size, mixer_size, name=u'Mixer', is_enabled=False)

            master_strip = mixer.master_strip()
            master_strip.set_volume_control(Knob(0, 28))
            master_strip.set_select_button(Pad(2, 127))
            mixer.set_prehear_volume_control(Knob(0, 29))

            # Channels
            for track_idx in range(mixer_size):
                strip = mixer.channel_strip(track_idx)
                
                strip.set_volume_control(SliderElement(MIDI_CC_TYPE, 0, 12 + track_idx))
                strip.set_arm_button(Button(0, 32 + track_idx))
                strip.set_select_button(Pad(4 + track_idx // 4, 124 + track_idx % 4))
                strip.set_mute_button(Button(0, 42 + track_idx))
                strip.set_solo_button(Button(0, 52 + track_idx))
                strip.set_invert_mute_feedback(True)

            # Returns
            for return_idx in range(2):
                strip = mixer.return_strip(return_idx)
                strip.set_select_button(Pad(6, 126 + return_idx))
                strip.set_mute_button(Button(0, 48 + return_idx))
                strip.set_solo_button(Button(0, 58 + return_idx))
                strip.set_invert_mute_feedback(True)

            # Selected strip
            selected_strip = mixer.selected_strip()
            selected_strip.set_volume_control((Knob(0, 22)))
            selected_strip.set_pan_control((Knob(0, 23)))
            selected_strip.set_send_controls((Knob(0, 24), Knob(0, 25)))

            mixer.set_bank_down_button(Pad(7, 126))
            mixer.set_bank_up_button(Pad(7, 127))
            mixer.set_enabled(True)

            # Device
            # layer = Layer(parameter_controls=ButtonMatrixElement(rows=[[Knob(1, 22 + i) for i in range(8)]])) # + [Knob(1, 12 + i) for i in range(8)]]))
            self._device = DeviceComponent(name='Device', is_enabled=False) # layer=layer, is_enabled=False)
            self._device.set_bank_nav_buttons(Pad(0, 123), Pad(0, 124))
            self._device.set_on_off_button(Pad(0, 127))
            self._device.set_parameter_controls(tuple([Knob(2, 22 + i) for i in range(8)]))
            self._device.set_enabled(True)
            self.set_device_component(self._device)
