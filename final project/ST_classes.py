import tkinter as tk

class articulation_frame():
    def __init__(self):
        self.error = 0.0

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
        self.main.config(bg="grey")

        self.main.columnconfigure(0,weight=1)
        self.main.columnconfigure(1,weight=1)
        self.main.rowconfigure(0, weight=1)
        self.main.rowconfigure(1, weight=1)
        self.main.rowconfigure(2, weight=1)
        self.main.rowconfigure(3, weight=1)

        #frames
        self.frames = [[tk.Frame(self.main, border=2, bg="light grey") for i in range(2)] for j in range(2)]

        #stringvars
        self.alignment_error = tk.StringVar(self.main, f"dilithium matrix allignment error: {articulation_frame().error}%")
        self.regulator_output = tk.StringVar(self.main, f"dilithium regulator output throttle: {dilithium_regulator().output}%")
        self.crystalization = tk.StringVar(self.main, f"dilithium matrix crystalization: {dilithium_matrix().crystalization}%")
        self.TMcompositor = tk.StringVar(self.main, f"theta-matrix compositor runing: {theta_matrix_compositor().run}")
        self.intermix_ratio = tk.StringVar(self.main, f"intermix ratio: {intermix_chamber().intermix_ratio}")
        self.containment_seals = tk.StringVar(self.main, f"antimatter containment: {intermix_chamber().contained}")
        self.EPS_L_pressure = tk.StringVar(self.main, f"left EPS manifold pressure: {EPS_conduit().pressure}")
        self.EPS_L_temperature = tk.StringVar(self.main, f"left EPS manifold temperature: {EPS_conduit().temperature}")
        self.EPS_L_flow = tk.StringVar(self.main, f"left EPS manifold flow: {EPS_conduit().flow}%")
        self.EPS_R_pressure = tk.StringVar(self.main, f"right EPS manifold pressure: {EPS_conduit().pressure}")
        self.EPS_R_temperature = tk.StringVar(self.main, f"right EPS manifold temperature: {EPS_conduit().temperature}")
        self.EPS_R_flow = tk.StringVar(self.main, f"right EPS manifold flow: {EPS_conduit().flow}%")
        self.warp_speed = tk.StringVar(self.main, f"maximum warp speed: {warp_coils().warp_speed}")

        #entries
        self.reg_out_entry = tk.Entry(self.frames[0][1])
        self.ratio_entry = tk.Entry(self.frames[0][1])

        #labels
        self.align_err_lbl = tk.Label(self.frames[0][0],textvariable=self.alignment_error)
        self.reg_out_lbl = tk.Label(self.frames[0][1], textvariable=self.regulator_output)
        self.crystal_lbl = tk.Label(self.frames[0][0], textvariable=self.crystalization)
        self.compositor_lbl = tk.Label(self.frames[0][0], textvariable=self.TMcompositor)
        self.ratio_lbl = tk.Label(self.frames[0][1], textvariable=self.intermix_ratio)
        self.containment_lbl = tk.Label(self.frames[1][1], textvariable=self.containment_seals)
        self.L_EPS_P_lbl = tk.Label(self.frames[1][0], textvariable=self.EPS_L_pressure)
        self.L_EPS_T_lbl = tk.Label(self.frames[1][0], textvariable=self.EPS_L_temperature)
        self.L_EPS_F_lbl = tk.Label(self.frames[1][0], textvariable=self.EPS_L_flow)
        self.R_EPS_P_lbl = tk.Label(self.frames[1][0], textvariable=self.EPS_R_pressure)
        self.R_EPS_T_lbl = tk.Label(self.frames[1][0], textvariable=self.EPS_R_temperature)
        self.R_EPS_F_lbl = tk.Label(self.frames[1][0], textvariable=self.EPS_R_flow)
        self.warp_lbl = tk.Label(self.main, textvariable=self.warp_speed, bg="light blue", padx=5, pady=3, font="bold 18")

        #static labels
        self.EPWR_lbl = tk.Label(self.main, text = "emergency power online", bg="light blue")
        self.dilitium_integrity = tk.Label(self.frames[0][0], text="dilithium crytaline structure monitor", bg="light blue")
        self.alignment_monitor = tk.Label(self.frames[0][0], text="dilithium articulation frame alignment monitor", bg="light blue")
        self.output_regulation = tk.Label(self.frames[0][1], text="warp core output regulation", bg="light blue")
        self.EPS_monitor = tk.Label(self.frames[1][0], text="EPS plasma monitor", bg="light blue")
        self.breach_monitor = tk.Label(self.frames[1][1], text="containment breach monitor", bg="light blue")

        #buttons
        self.align_btn = tk.Button(self.frames[0][0], text="align", command=self.align)
        self.regulator_output_btn = tk.Button(self.frames[0][1], text="set regulator output", command=self.set_output)
        self.TMC_btn = tk.Button(self.frames[0][0], text="toggle theta-matrix compositor", command=self.toggle_TMC)
        self.ratio_btn = tk.Button(self.frames[0][1], text="set intermix ratio", command= lambda: self.set_ratio(self.ratio_entry.get()))

        #geometry managers
        for i in range(2):
            for j in range(2):
                self.frames[i][j].grid(row=i+1, column=j, sticky="NSEW", padx=2, pady=2)

        self.EPWR_lbl.grid(row=0, column=0, sticky="NSEW", padx=2, pady=2)
        self.warp_lbl.grid(row=0, column=1, sticky="NSEW", padx=2, pady=2)
        
        self.dilitium_integrity.pack(fill="x")
        self.crystal_lbl.pack(fill="x")
        self.compositor_lbl.pack(fill="x")
        self.TMC_btn.pack(fill="x")

        self.alignment_monitor.pack(fil="x")
        self.align_err_lbl.pack(fil="x")
        self.align_btn.pack(fil="x")

        self.output_regulation.pack(fill="x")
        self.reg_out_lbl.pack(fill="x")
        self.reg_out_entry.pack(fill="x")
        self.regulator_output_btn.pack(fil="x")
        self.ratio_lbl.pack(fil="x")
        self.ratio_entry.pack(fil="x")
        self.ratio_btn.pack(fil="x")

        self.EPS_monitor.pack(fil="x")
        self.L_EPS_F_lbl.pack(fil="x")
        self.L_EPS_P_lbl.pack(fil="x")
        self.L_EPS_T_lbl.pack(fil="x")
        self.R_EPS_F_lbl.pack(fil="x")
        self.R_EPS_P_lbl.pack(fil="x")
        self.R_EPS_T_lbl.pack(fil="x")

        self.breach_monitor.pack(fil="x")
        self.containment_lbl.pack(fil="x")

    def align(self, new_error):
        self.alignment_error.set(f"dilithium matrix allignment error: {new_error}%")

    def set_output(self, new_output):
        self.regulator_output.set(f"dilithium regulator output throttle: {new_output}")

    def toggle_TMC(self, status):
        self.TMcompositor.set(f"theta-matrix compositor runing: {status}")

    def set_ratio(self, new_ratio):
        self.intermix_ratio.set(f"intermix ratio: {new_ratio}")



    def run(self):
        self.main.mainloop()