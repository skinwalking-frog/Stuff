"""attempt to make some automated tests without pytest"""
import ST_classes as ST

AF = ST.articulation_frame()
TMC = ST.theta_matrix_compositor()
DR = ST.dilithium_regulator()

GUI = ST.UI()

print("Testing .align() method of class 'articulation_frame'")
AF.error = 5.75
print(F".error initial value = {AF.error}")
AF.align()
print(f"running .align()... \nReturned .error value of {AF.error}")
if AF.error == 0:
    print("Passed\n")
else:
    print("failed\n")

print("Testing .toggle_compositor() method of class 'theta_matrix_compositor'")
TMC.run = True
print(F".run initial value = {TMC.run}")
TMC.toggle_compositor()
print(f"running .toggle_compositor... \nReturned .run value of {TMC.run}")
if TMC.run == False:
    print("Passed\n")
else:
    print("failed\n")

print("testing .set_output() method of class 'dilithium_regulator'")
DR.output = 100.0
print(f".output initial value = {DR.output}")
DR.set_output(50.0)
print(f"running .set_output(50.0)... \nReturned .output value of {DR.output}")
if DR.output == 50.0:
    print("Passed\n")
else:
    print("failed\n")

print("testing .set_ratio() method of class 'UI'")
GUI.warp_core.intermix_ratio = 0
print(f".warp_core.intermix_ratio initial value = {GUI.warp_core.intermix_ratio}")
GUI.set_ratio(2.0)
print(f"running .set_ratio(2.0)... \nReturned .warp_core.intermix_ratio value of {GUI.warp_core.intermix_ratio}")
if GUI.warp_core.intermix_ratio == 2.0:
    print("Passed\n")
else:
    print("failed\n")