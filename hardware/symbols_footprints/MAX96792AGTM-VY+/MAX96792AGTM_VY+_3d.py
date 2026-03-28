# FreeCAD Python script for MAX96792AGTM/VY+ 3D model: 48-TQFN 7x7mm w/EP
# Export with:
#   freecad --console --run MAX96792AGTM_VY+_3d.py
import FreeCAD, Part, Mesh
from FreeCAD import Base

# Parameters (mm)
body_x = 7.0
body_y = 7.0
body_z = 0.9
fillet_r = 0.17   # Body fillet
lead_L = 0.53
lead_W = 0.30
lead_T = 0.07      # nominal thickness (IPC)
lead_N = 48
lead_pitch = 0.5
ep_x = 5.4
ep_y = 5.4
ep_z = 0.15        # 150um typical thickness for EP

doc = FreeCAD.newDocument("MAX96792AGTM_VY+_3d")
# IC Body
body = Part.makeBox(body_x, body_y, body_z)
body.translate(Base.Vector(-body_x/2, -body_y/2, 0))
body = body.makeFillet(fillet_r, body.Edges)

# Exposed pad
ep = Part.makeBox(ep_x, ep_y, ep_z)
ep.translate(Base.Vector(-ep_x/2, -ep_y/2, 0))
# Leads ("gullwing" pads, simplified as extruded rectangles)
lead_objs = []
for side in range(4):
    for p in range(12):
        pin_num = side*12 + p + 1
        # nominal centers (QFN counterclockwise, pin 1 at -X/-Y)
        if side == 0:  # top
            x = -body_x/2 + lead_pitch/2 + p*lead_pitch
            y = -body_y/2 - lead_L/2
            angle = 0
        elif side == 1:  # right
            x = body_x/2 + lead_L/2
            y = -body_y/2 + lead_pitch/2 + p*lead_pitch
            angle = 90
        elif side == 2:  # bottom
            x = body_x/2 - lead_pitch/2 - p*lead_pitch
            y = body_y/2 + lead_L/2
            angle = 180
        elif side == 3:  # left
            x = -body_x/2 - lead_L/2
            y = body_y/2 - lead_pitch/2 - p*lead_pitch
            angle = 270
        # Single pad
        pad = Part.makeBox(lead_W, lead_L, lead_T)
        # Center on pad projection
        pad.translate(Base.Vector(-lead_W/2, -lead_L/2, 0))
        # Place
        pad.translate(Base.Vector(x, y, 0))
        lead_objs.append(pad)

# Pin 1 marker: dot on corner
pin1_dot = Part.makeCylinder(0.15, 0.09, Base.Vector(-body_x/2+0.35, -body_y/2+0.35, body_z), Base.Vector(0,0,1))

# Union all shapes
shape = body.fuse(ep)
for l in lead_objs:
    shape = shape.fuse(l)
shape = shape.fuse(pin1_dot)

# Color: body=dark gray, leads/pad=silver, marker=yellow
# (Optional: Set colors for STEP if desired)
Part.show(shape)
doc.recompute()

out_step = "MAX96792AGTM_VY+.step"
shape.exportStep(out_step)
print("3D model exported as", out_step)
