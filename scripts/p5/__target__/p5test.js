// Transcrypt'ed from Python, 2020-08-24 05:15:22
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
var __name__ = '__main__';
export var p_setup_gen = function (p) {
	var p_setup = function () {
		p.createCanvas (200, 200);
		p.background (160);
	};
	return p_setup;
};
export var p_draw_gen = function (p) {
	var p_draw = function () {
		p.fill ('blue');
		var fc = p.frameCount;
		p.background (200);
		var r = math.sin (fc / 60) * 50 + 50;
		p.ellipse (100, 100, r, r);
	};
	return p_draw;
};
export var sketch_setup = function (p) {
	p.setup = p_setup_gen (p);
	p.draw = p_draw_gen (p);
};
export var myp5 = new p5 (sketch_setup, 'sketch-holder');

//# sourceMappingURL=p5test.map