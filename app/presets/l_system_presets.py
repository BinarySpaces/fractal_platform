L_SYSTEM_PRESETS = {
    # --- Classical ---
    'koch_snowflake': {
        'axiom': 'F--F--F',
        'rules': {'F': 'F+F--F+F'},
        'angle': 60.0,
        'depth': 4,
        'step': None
    },
    'koch_island': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'F-F+F+FFF-F-F+F'},
        'angle': 90.0,
        'depth': 2,
        'step': None
    },
    'crystal': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'FF+F++F+F'},
        'angle': 90.0,
        'depth': 3,
        'step': None
    },
    'square_snowflake': {
        'axiom': 'F--F',
        'rules': {'F': 'F-F+F+F-F'},
        'angle': 90.0,
        'depth': 4,
        'step': None
    },
    'vicsek': {
        'axiom': 'F-F-F-F',
        'rules': {'F': 'F-F+F+F-F'},
        'angle': 90.0,
        'depth': 4,
        'step': None
    },
    'levy': {
        'axiom': 'F',
        'rules': {'F': '+F--F+'},
        'angle': 45.0,
        'depth': 10,
        'step': None
    },

    # --- Sierpinski ---
    'sierpinski_carpet': {
        'axiom': 'YF',
        'rules': {'X': 'YF+XF+Y', 'Y': 'XF-YF-X'},
        'angle': 60.0,
        'depth': 1,
        'step': None
    },
    'sierpinski_lattice': {
        'axiom': 'FXF--FF--FF',
        'rules': {'F': 'FF', 'X': '--FXF++FXF++FXF--'},
        'angle': 60.0,
        'depth': 7,
        'step': None
    },
    'sierpinski_curve': {
        'axiom': 'F+XF+F+XF',
        'rules': {'X': 'XF-F+F-XF+F+XF-F+F-X'},
        'angle': 90.0,
        'depth': 4,
        'step': None
    },

    # --- Geometric ---
    'square': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'FF+F+F+F+FF'},
        'angle': 90.0,
        'depth': 3,
        'step': None
    },
    'tiles': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'FF+F-F+F+FF'},
        'angle': 90.0,
        'depth': 3,
        'step': None
    },
    'rings': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'FF+F+F+F+F+F-F'},
        'angle': 90.0,
        'depth': 2,
        'step': None
    },
    'cross': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'F+F-F+F+F'},
        'angle': 90.0,
        'depth': 3,
        'step': None
    },
    'cross_2': {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'F+FF++F+F'},
        'angle': 90.0,
        'depth': 3,
        'step': None
    },
    'triangle': {
        'axiom': 'F+F+F',
        'rules': {'F': 'F-F+F'},
        'angle': 120.0,
        'depth': 2,
        'step': None
    },

    # --- Dragons ---
    'dragon': {
        'axiom': 'FX',
        'rules': {'X': 'X+YF+', 'Y': '-FX-Y'},
        'angle': 90.0,
        'depth': 8,
        'step': None
    },
    'terdragon': {
        'axiom': 'F',
        'rules': {'F': 'F-F+F'},
        'angle': 120.0,
        'depth': 5,
        'step': None
    },
    'double_dragon': {
        'axiom': 'FX+FX',
        'rules': {'X': 'X+YF+', 'Y': '-FX-Y'},
        'angle': 90.0,
        'depth': 6,
        'step': None
    },
    'triple_dragon': {
        'axiom': 'FX+FX+FX',
        'rules': {'X': 'X+YF+', 'Y': '-FX-Y'},
        'angle': 90.0,
        'depth': 7,
        'step': None
    },

    # --- Space-filling curves ---
    'peano': {
        'axiom': 'F',
        'rules': {'F': 'F+F-F-F-F+F+F+F-F'},
        'angle': 90.0,
        'depth': 2,
        'step': None
    },
    'peano_gosper': {
        'axiom': 'FX',
        'rules': {'X': 'X+YF++YF-FX--FXFX-YF+', 'Y': '-FX+YFYF++YF+FX--FX-Y'},
        'angle': 60.0,
        'depth': 4,
        'step': None
    },
    'gosper_square': {
        'axiom': 'YF',
        'rules': {
            'X': 'XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-',
            'Y': '+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY'
        },
        'angle': 90.0,
        'depth': 2,
        'step': None
    },
    'moore': {
        'axiom': 'LFL-F-LFL',
        'rules': {'L': '+RF-LFL-FR+', 'R': '-LF+RFR+FL-'},
        'angle': 90.0,
        'depth': 0,
        'step': None
    },
    'hilbert': {
        'axiom': 'L',
        'rules': {'L': '+RF-LFL-FR+', 'R': '-LF+RFR+FL-'},
        'angle': 90.0,
        'depth': 8,
        'step': None
    },
    'hilbert_2': {
        'axiom': 'X',
        'rules': {'X': 'XFYFX+F+YFXFY-F-XFYFX', 'Y': 'YFXFY-F-XFYFX+F+YFXFY'},
        'angle': 90.0,
        'depth': 4,
        'step': None
    },

    # --- Others ---
    'pentaplexity': {
        'axiom': 'F++F++F++F++F',
        'rules': {'F': 'F++F++F+++++F-F++F'},
        'angle': 36.0,
        'depth': 1,
        'step': None
    },
    'segment_32': {
        'axiom': 'F+F+F+F',
        'rules': {'F': '-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+'},
        'angle': 90.0,
        'depth': 3,
        'step': None
    },
    'krishna_anklets': {
        'axiom': '-X--X',
        'rules': {'X': 'XFX--XFX'},
        'angle': 45.0,
        'depth': 3,
        'step': None
    },
    'plant': {
        'axiom': 'F',
        'rules': {'F': 'F-F+F'},
        'angle': 25.0,
        'depth': 5,
        'step': None
    },
}
