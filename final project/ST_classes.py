import tkinter as tk

# class warp_core():
#     def __init__(self) -> None:
#         pass

class articulation_frame():
    def __init__(self):
        self.error = 3.0 #reset to 0 after testing

    def align(self):
        self.error = 0.0
        return self.error

class dilithium_regulator():
    def __init__(self):
        self.output = 100.0

    def set_output(self, output):
        self.output = output

class dilithium_matrix():
    def __init__(self):
        self.crystalization = 100.0

class theta_matrix_compositor():
    def __init__(self):
        self.run = False

    def toggle_compositor(self):
        self.run = not self.run
        return self.run
    
class containment_seals():
    def __init__(self):
        self.contained = True

class intermix_chamber(containment_seals):
    def __init__(self):
        super().__init__()
        self.intermix_ratio = 1.0
    
    def set_ratio(self, new_ratio):
        self.intermix_ratio = new_ratio
        return self.intermix_ratio

class warp_plasma():
    def __init__(self):
        self.temperature = 5000
        self.pressure = 20000

class EPS_conduit(warp_plasma):
    def __init__(self):
        super().__init__()
        self.breach = False
        self.flow = 100.0

class warp_coils(EPS_conduit):
    def __init__(self):
        super().__init__()
        self.warp_speed = 10


class UI():
    def __init__(self):
        self.main = tk.Tk()
        self.main.geometry = "1600x900"
        self.main.minsize(800, 450)
        self.main.title("warp regulator")

        self.alignment_error = tk.StringVar(self.main, f"dilithium matrix allignment error: {articulation_frame().error}%")
        self.regulator_output = tk.StringVar(self.main, f"dilithium regulator output throttle: {dilithium_regulator().output}%")
        self.crystalization = tk.StringVar(self.main, f"dilithium matrix crystalization: {dilithium_matrix().crystalization}%")
        self.TMcompositor = tk.StringVar(self.main, f"theta-matrix compositor ruuning: {theta_matrix_compositor().run}")
        self.intermix_ratio = tk.StringVar(self.main, f"intermix ration: {intermix_chamber().intermix_ratio}")
        self.containment_seals = tk.StringVar(self.main, f"antimatter containment: {intermix_chamber().contained}")
        self.EPS_L_pressure = tk.StringVar(self.main, f"left EPS manifold pressure: {EPS_conduit().pressure}")
        self.EPS_L_temperature = tk.StringVar(self.main, f"left EPS manifold temperature: {EPS_conduit().temperature}")
        self.EPS_L_flow = tk.StringVar(self.main, f"left EPS manifold flow: {EPS_conduit().flow}%")
        self.EPS_R_pressure = tk.StringVar(self.main, f"right EPS manifold pressure: {EPS_conduit().pressure}")
        self.EPS_R_temperature = tk.StringVar(self.main, f"right EPS manifold temperature: {EPS_conduit().temperature}")
        self.EPS_R_flow = tk.StringVar(self.main, f"right EPS manifold flow: {EPS_conduit().flow}%")
        self.warp_speed = tk.StringVar(self.main, f"maximum warp speed: {warp_coils().warp_speed}")

        self.reg_out_entry = tk.Entry(self.main)
        self.ratio_entry = tk.Entry(self.main)

        self.EPWR_lbl = tk.Label(self.main, text = "emergency power online")
        self.align_err_lbl = tk.Label(self.main,textvariable=self.alignment_error)
        self.reg_out_lbl = tk.Label(self.main, textvariable=self.regulator_output)
        self.crystal_lbl = tk.Label(self.main, textvariable=self.crystalization)
        self.compositor_lbl = tk.Label(self.main, textvariable=self.TMcompositor)
        self.ratio_lbl = tk.Label(self.main, textvariable=self.intermix_ratio)
        self.containment_lbl = tk.Label(self.main, textvariable=self.containment_seals)
        self.L_EPS_P_lbl = tk.Label(self.main, textvariable=self.EPS_L_pressure)
        self.L_EPS_T_lbl = tk.Label(self.main, textvariable=self.EPS_L_temperature)
        self.L_EPS_F_lbl = tk.Label(self.main, textvariable=self.EPS_L_flow)
        self.R_EPS_P_lbl = tk.Label(self.main, textvariable=self.EPS_R_pressure)
        self.R_EPS_T_lbl = tk.Label(self.main, textvariable=self.EPS_R_temperature)
        self.R_EPS_F_lbl = tk.Label(self.main, textvariable=self.EPS_R_flow)
        self.warp_lbl = tk.Label(self.main, textvariable=self.warp_speed)

        self.align_btn = tk.Button(self.main, name="align", command=self.align)
        self.regulator_output_btn = tk.Button(self.main, name="set regulator output", command=self.set_output)
        self.TMC_btn = tk.Button(self.main, name="toggle theta-matrix compositor", command=self.toggle_TMC)
        

    def align(self, new_error):
        self.alignment_error.set(f"dilithium matrix allignment error: {new_error}%")

    def set_output(self, new_output):
        self.regulator_output.set(f"dilithium regulator output throttle: {new_output}")

    def toggle_TMC(self, status):
        self.TMcompositor.set(f"theta-matrix compositor ruuning: {status}")



    def run(self): 
        self.main.mainloop()

A = UI()
A.run()
