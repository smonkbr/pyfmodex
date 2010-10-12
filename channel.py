from fmodobject import *
from fmodobject import _dll
from structures import VECTOR
import dsp, dsp_connection, channel_group

class ConeSettings(object):
    def __init__(self, sptr):
        self._sptr = sptr
        self._in = c_float()
        self._out = c_float()
        self._outvol = c_float()
        ckresult(_dll.FMOD_Channel_Get3DConeSettings(self._sptr, byref(self._in), byref(self._out), byref(self._outvol)))

    @property
    def inside_angle(self):
        return self._in.value
    @inside_angle.setter
    def inside_angle(self, angle):
        self._in = c_float(angle)
        self._commit()

    @property
    def outside_angle(self):
        return self._out.value
    @outside_angle.setter
    def outside_angle(self, angle):
        self._out = c_float(angle)
        self._commit()

    @property
    def outside_volume(self):
        return self._outvol.value
    @outside_volume.setter
    def outside_volume(self, vol):
        self._outvol = c_float(vol)
        self._commit()

    def _commit(self):
        ckresult(_dll.FMOD_Channel_Set3DConeSettings(self._sptr, self._in, self._out, self._outvol))

class Channel(FmodObject):
    def add_dsp(self, dsp):
        if not isinstance(dsp, dsp.DSP): raise FmodError("DSP instance is required.")
        c_ptr = c_int()
        ckresult(_dll.FMOD_Channel_AddDSP(self._ptr, dsp._ptr, byref(c_ptr)))
        return dsp_connection.DSPConnection(c_ptr)
    @property
    def _threed_attrs(self):
        pos = Vector()
        vel = Vector()
        ckresult(_dll.FMOD_Channel_Get3DAttributes(self._ptr, byref(pos), byref(vel)))
        return [pos.to_list(), vel.to_list()]
    @_threed_attrs.setter
    def _threed_attrs(self, attrs):
        pos = VECTOR.from_list(attrs[0])
        vel = VECTOR.from_list(attrs[1])
        ckresult(_dll.FMOD_Channel_Set3DAttributes(self._ptr, pos, vel))

    @property
    def position(self):
        return self._threed_attrs0]
    @velocity.setter
    def velocity(self, pos):
        self._threed_attrs = (pos, self._threed_attrs[1])

    @property
    def velocity(self):
        return self._threed_attrs1]
    @velocity.setter
    def velocity(self, vel):
        self._threed_attrs = (self._threed_attrs[0], vel)

    @property
    def cone_orientation(self):
        ori = VECTOR()
        ckresult(_dll.FMOD_Channel_Get3DConeOrientation(self._ptr, byref(ori)))
    return ori.to_list()
    @cone_orientation.setter
    def cone_orientation(self, ori):
        vec = VECTOR.from_list(ori)
    ckresult(_dll.FMOD_Channel_Set3DConeOrientation(self._ptr, vec))

    @property
    def cone_settings(self):
        return ConeSettings(self._ptr)
    
    @property
    def doppler_level(self):
        level = c_float()
        ckresult(_dll.FMOD_Channel_Get3DDopplerLevel(self._ptr, byref(level)))
        return level.value
    @doppler_level.setter
    def doppler_level(self, l):
    ckresult(_dll.FMOD_Channel_Set3DDopplerLevel(self._ptr, l))

    @property
    def _min_max_distance(self):
        min = c_float()
        max = c_float()
        ckresult(_dll.FMOD_Channel_Get3DMinMaxDistance(self._ptr, byref(min), byref(max)))
        return (min.value, max.value)
    @_min_max_distance.setter
    def _min_max_distance(self, dists):
        ckresult(_dll.FMOD_Channel_Set3DMinMaxDistance(self._ptr, dists[0], dists[1]))

    @property
    def min_distance(self):
        return self._min_max_distance[0]
    @min_distance.setter
    def min_distance(self, dist):
        self._min_max_distance = (dist, self._min_max_distance[1])

    @property
    def max_distance(self):
        return self._min_max_distance[1]
    @max_distance.setter
    def max_distance(self, dist):
        self._min_max_distance = (self._min_max_distance[0], dist)

        @property
    def _occlusion(self):
        direct = c_float()
        reverb = c_float()
        ckresult(_dll.FMOD_Channel_Get3DOcclusion(self._ptr, byref(direct), byref(reverb)))
        return (direct.value, reverb.value)
    @_occlusion.setter
    def _occlusion(self, occs):
        ckresult(_dll.FMOD_Channel_Set3DOcclusion(self._ptr, occs[0], occs[1]))

    @property
    def direct_occlusion(self):
        return self._occlusion[0]
    @direct_occlusion.setter
    def direct_occlusion(self, occ):
        self._occlusion = (occ, self._occlusion[1])

    @property
    def reverb_occlusion(self):
        return self._occlusion[1]
    @reverb_occlusion.setter
    def reverb_occlusion(self, occ):
        self._occlusion = (self._occlusion[0], occ)

    @property
    def pan_level(self):
        l = c_int()
        ckresult(_dll.FMOD_Channel_Get3DanLevel(self._ptr, byref(l)))
        return l.value
    @pan_level.setter
    def pan_level(self, l):
    ckresult(_dll.FMOD_Channel_Set3DPanLevel(self._ptr, l))
    