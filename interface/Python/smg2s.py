# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_smg2s')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_smg2s')
    _smg2s = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_smg2s', [dirname(__file__)])
        except ImportError:
            import _smg2s
            return _smg2s
        try:
            _mod = imp.load_module('_smg2s', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _smg2s = swig_import_helper()
    del swig_import_helper
else:
    import _smg2s
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _smg2s.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _smg2s.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _smg2s.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _smg2s.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _smg2s.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _smg2s.SwigPyIterator_equal(self, x)

    def copy(self):
        return _smg2s.SwigPyIterator_copy(self)

    def next(self):
        return _smg2s.SwigPyIterator_next(self)

    def __next__(self):
        return _smg2s.SwigPyIterator___next__(self)

    def previous(self):
        return _smg2s.SwigPyIterator_previous(self)

    def advance(self, n):
        return _smg2s.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _smg2s.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _smg2s.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _smg2s.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _smg2s.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _smg2s.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _smg2s.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _smg2s.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class NilpotencyInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NilpotencyInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NilpotencyInt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["diagPosition"] = _smg2s.NilpotencyInt_diagPosition_set
    __swig_getmethods__["diagPosition"] = _smg2s.NilpotencyInt_diagPosition_get
    if _newclass:
        diagPosition = _swig_property(_smg2s.NilpotencyInt_diagPosition_get, _smg2s.NilpotencyInt_diagPosition_set)
    __swig_setmethods__["nbOne"] = _smg2s.NilpotencyInt_nbOne_set
    __swig_getmethods__["nbOne"] = _smg2s.NilpotencyInt_nbOne_get
    if _newclass:
        nbOne = _swig_property(_smg2s.NilpotencyInt_nbOne_get, _smg2s.NilpotencyInt_nbOne_set)
    __swig_setmethods__["matrix_size"] = _smg2s.NilpotencyInt_matrix_size_set
    __swig_getmethods__["matrix_size"] = _smg2s.NilpotencyInt_matrix_size_get
    if _newclass:
        matrix_size = _swig_property(_smg2s.NilpotencyInt_matrix_size_get, _smg2s.NilpotencyInt_matrix_size_set)
    __swig_setmethods__["nilpotency"] = _smg2s.NilpotencyInt_nilpotency_set
    __swig_getmethods__["nilpotency"] = _smg2s.NilpotencyInt_nilpotency_get
    if _newclass:
        nilpotency = _swig_property(_smg2s.NilpotencyInt_nilpotency_get, _smg2s.NilpotencyInt_nilpotency_set)
    __swig_setmethods__["setup"] = _smg2s.NilpotencyInt_setup_set
    __swig_getmethods__["setup"] = _smg2s.NilpotencyInt_setup_get
    if _newclass:
        setup = _swig_property(_smg2s.NilpotencyInt_setup_get, _smg2s.NilpotencyInt_setup_set)

    def __init__(self, *args):
        this = _smg2s.new_NilpotencyInt(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def NilpType1(self, num, size):
        return _smg2s.NilpotencyInt_NilpType1(self, num, size)

    def NilpType2(self, num, size):
        return _smg2s.NilpotencyInt_NilpType2(self, num, size)
    __swig_destroy__ = _smg2s.delete_NilpotencyInt
    __del__ = lambda self: None
NilpotencyInt_swigregister = _smg2s.NilpotencyInt_swigregister
NilpotencyInt_swigregister(NilpotencyInt)

# This file is compatible with both classic and new-style classes.


