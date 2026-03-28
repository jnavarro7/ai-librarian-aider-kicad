import FreeCAD
import Part

def create_dfn8_2p5x2p5(body_x=2.5, body_y=2.5, body_z=0.9,
                        pad_x=0.3, pad_y=1.0, pad_z=0.08,
                        expad_x=1.8, expad_y=1.1, expad_z=0.12,
                        pin_pitch=0.5, pins_per_side=4):
    # Origin at center
    doc = FreeCAD.ActiveDocument if FreeCAD.ActiveDocument else FreeCAD.newDocument('DFN8_2p5x2p5')
    objects = []
    body = Part.makeBox(body_x, body_y, body_z)
    body.translate(FreeCAD.Vector(-body_x/2, -body_y/2, 0))
    body_obj = doc.addObject("Part::Feature", "Body")
    body_obj.Shape = body
    objects.append(body_obj)

    # Lead pads - left (pins 1-4)
    for i in range(pins_per_side):
        cy = -body_y/2 + pad_y/2 + pin_pitch*i
        px = -body_x/2
        pin = Part.makeBox(pad_x, pad_y, pad_z)
        pin.translate(FreeCAD.Vector(px - pad_x, cy - pad_y/2, -pad_z))
        pin_obj = doc.addObject("Part::Feature", "Pin_L%d"%(i+1))
        pin_obj.Shape = pin
        objects.append(pin_obj)
    # Lead pads - right (pins 5-8)
    for i in range(pins_per_side):
        cy = -body_y/2 + pad_y/2 + pin_pitch*(pins_per_side-1-i)
        px = body_x/2
        pin = Part.makeBox(pad_x, pad_y, pad_z)
        pin.translate(FreeCAD.Vector(px, cy - pad_y/2, -pad_z))
        pin_obj = doc.addObject("Part::Feature", "Pin_R%d"%(i+5))
        pin_obj.Shape = pin
        objects.append(pin_obj)

    # Exposed pad
    expad = Part.makeBox(expad_x, expad_y, expad_z)
    expad.translate(FreeCAD.Vector(-expad_x/2, -expad_y/2, -expad_z-0.01))
    expad_obj = doc.addObject("Part::Feature", "ExposedPad")
    expad_obj.Shape = expad
    objects.append(expad_obj)

    doc.recompute()

    return objects

if __name__ == "__main__":
    objs = create_dfn8_2p5x2p5()
    import ImportGui
    ImportGui.export([o for o in objs], "SHT31A-DIS-B2.5kS_DFN-8_2.5x2.5mm.step")
