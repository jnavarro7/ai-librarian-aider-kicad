import FreeCAD
import Part

# Dimensions (all in mm)
body_length = 3.0
body_width = 3.0
body_height = 1.0

pad_width = 0.3
pad_length = 1.0
pad_height = 0.15

lead_pitch = 0.65
lead_count = 8
row_offset = 1.0  # ~distance from center to left/right pad row

# Origin: center of body at X=0 Y=0, Z=pad bottom (Z=0 is PCB surface)
doc = FreeCAD.newDocument("TLV272DMR2G_MSOP8")

# Main body
body = Part.makeBox(body_length, body_width, body_height)
body.translate(FreeCAD.Vector(-body_length/2, -body_width/2, pad_height))  # body sits on top of pins

# Leads (pads)
leads = []
for i in range(4):
    # Left row: pins 1-4 from top to bottom
    y = (1.5 - i) * lead_pitch
    lead = Part.makeBox(pad_length, pad_width, pad_height)
    lead.translate(FreeCAD.Vector(-body_length/2 - pad_length, y - pad_width/2, 0))
    leads.append(lead)

    # Right row: pins 5-8 from bottom to top
    y2 = (-1.5 + i) * lead_pitch
    lead2 = Part.makeBox(pad_length, pad_width, pad_height)
    lead2.translate(FreeCAD.Vector(body_length/2, y2 - pad_width/2, 0))
    leads.append(lead2)

# Fuse all parts
model = body.fuse(leads)

Part.show(model)
doc.recompute()

# Export as STEP (or WRL as needed)
Part.export([model], "TLV272DMR2G_MSOP-8.step")
