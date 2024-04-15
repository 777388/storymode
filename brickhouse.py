import codeop
import vispy
class programming:
    def __init__(self):
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT.real()
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT.__invert__
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT.__pos__
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT.imag()
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT._maybe_compile()
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT.__pow__
        
        codeop.PyCF_ALLOW_INCOMPLETE_INPUT.__xor__
    def __init_subclass__(self):
        complex.real.__init_subclass__
        complex.compile.__delattr__
        enumerate.__ne__.__name__
        vispy.keys.CONTROL
        vispy._get_sg_image_scraper.__code__
        vispy.geometry()

class interview(programming):
    def __init__(self):
        super(interview, self).__init__(self)

black = interview
black
