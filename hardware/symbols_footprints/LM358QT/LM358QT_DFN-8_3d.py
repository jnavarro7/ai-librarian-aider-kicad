import FreeCAD
import Part

def create_dfn8_2x2(body_x=2.0, body_y=2.0, body_z=0.55,
                    pad_x=0.3, pad_y=0.65, pad_z=0.08,
                    pin_pitch=0.5, pins_per_side=4):
    """
    Create 3D model for LM358QT DFN-8 2x2mm.
    Dimensions per STMicroelectronics LM358 datasheet DFN-8 (2.0x2.0mm).
    No center pad.
    Origin is at part center. All units in mm.
    """
    doc = FreeCAD.ActiveDocument if FreeCAD.ActiveDocument else FreeCAD.newDocument('DFN8_2x2')
    objects = []
    # Body
    body = Part.makeBox(body_x, body_y, body_z)
    body.translate(FreeCAD.Vector(-body_x/2, -body_y/2, 0))
    body_obj = doc.addObject("Part::Feature", "Body")
    body_obj.Shape = body
    objects.append(body_obj)

    # Pin pads - left (pins 1-4)
    for i in range(pins_per_side):
        cy = -body_y / 2 + pad_y / 2 + pin_pitch * i
        px = -body_x / 2
        pin = Part.makeBox(pad_x, pad_y, pad_z)
        pin.translate(FreeCAD.Vector(px - pad_x, cy - pad_y / 2, -pad_z))
        pin_obj = doc.addObject("Part::Feature", "Pin_L%d" % (i + 1))
        pin_obj.Shape = pin
        objects.append(pin_obj)
    # Pin pads - right (pins 5-8)
    for i in range(pins_per_side):
        cy = -body_y / 2 + pad_y / 2 + pin_pitch * (pins_per_side - 1 - i)
        px = body_x / 2
        pin = Part.makeBox(pad_x, pad_y, pad_z)
        pin.translate(FreeCAD.Vector(px, cy - pad_y / 2, -pad_z))
        pin_obj = doc.addObject("Part::Feature", "Pin_R%d" % (i + 5))
        pin_obj.Shape = pin
        objects.append(pin_obj)

    doc.recompute()
    return objects

if __name__ == "__main__":
    objs = create_dfn8_2x2()
    import ImportGui
    ImportGui.export([o for o in objs], "LM358QT_DFN-8.step")
