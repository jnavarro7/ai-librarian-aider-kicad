import FreeCAD
import Part

def create_miniso8(body_x=3.0, body_y=3.0, body_z=1.0,
                   pad_x=0.31, pad_y=0.70, pad_z=0.15,
                   lead_span=4.9, pin_pitch=0.65, pins_per_side=4):
    # Origin at center of body; Z=0 is PCB plane
    doc = FreeCAD.ActiveDocument if FreeCAD.ActiveDocument else FreeCAD.newDocument('MiniSO8')
    objects = []
    # Main body
    body = Part.makeBox(body_x, body_y, body_z)
    body.translate(FreeCAD.Vector(-body_x/2, -body_y/2, 0.15))
    body_obj = doc.addObject("Part::Feature", "Body")
    body_obj.Shape = body
    body_obj.ViewObject.ShapeColor = (0.1, 0.1, 0.1)
    objects.append(body_obj)
    # Lead pads left (pins 1-4, top to bottom)
    left_x = -lead_span/2
    for i in range(pins_per_side):
        y = body_y/2 - pin_pitch*i - pad_y/2
        pin = Part.makeBox(pad_x, pad_y, pad_z)
        pin.translate(FreeCAD.Vector(left_x - pad_x, y, 0))
        pin_obj = doc.addObject("Part::Feature", f"Pin_L{i+1}")
        pin_obj.Shape = pin
        pin_obj.ViewObject.ShapeColor = (0.8, 0.8, 0.2)
        objects.append(pin_obj)
    # Lead pads right (pins 5-8, bottom to top)
    right_x = lead_span/2
    for i in range(pins_per_side):
        y = -body_y/2 + pin_pitch*i + pad_y/2
        pin = Part.makeBox(pad_x, pad_y, pad_z)
        pin.translate(FreeCAD.Vector(right_x, y, 0))
        pin_obj = doc.addObject("Part::Feature", f"Pin_R{8-i}")
        pin_obj.Shape = pin
        pin_obj.ViewObject.ShapeColor = (0.8, 0.8, 0.2)
        objects.append(pin_obj)
    doc.recompute()
    return objects

if __name__ == "__main__":
    objs = create_miniso8()
    import ImportGui
    ImportGui.export([o for o in objs], "LM358ST_MiniSO-8.step")
