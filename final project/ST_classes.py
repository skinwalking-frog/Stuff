"""
Oliver Rothe

contains classes for use in ST_console_Main.py

The variable naming is less than ideal, lots of similar names and a huge amount of variables
A little hard to read, but most large chunks do similar things to different variables.

"""

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
        self.clearance = 1.00

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

        #configure the rows and columns
        self.main.columnconfigure(0,weight=1)
        self.main.columnconfigure(1,weight=1)
        self.main.rowconfigure(0, weight=1)
        self.main.rowconfigure(1, weight=1)
        self.main.rowconfigure(2, weight=1)
        self.main.rowconfigure(3, weight=1)

        #objects
        self.warp_core = intermix_chamber()
        self.dil_reg = dilithium_regulator()
        self.dil_matrix = dilithium_matrix()
        self.A_frame = articulation_frame()
        self.TMC = theta_matrix_compositor()
        self.warp_coils = warp_coils()
        self.LEPS = EPS_conduit()
        self.REPS = EPS_conduit()

        #frames
        self.frames = [[tk.Frame(self.main, border=2, bg="light grey") for i in range(2)] for j in range(2)]

        #stringvars
        self.alignment_error = tk.StringVar(self.main, f"dilithium matrix allignment error: {self.A_frame.error}%")
        self.regulator_output = tk.StringVar(self.main, f"dilithium regulator output throttle: {self.dil_reg.output}%")
        self.crystalization = tk.StringVar(self.main, f"dilithium matrix crystalization: {self.dil_matrix.crystalization}%")
        self.TMcompositor = tk.StringVar(self.main, f"theta-matrix compositor runing: {self.TMC.run}")
        self.intermix_ratio = tk.StringVar(self.main, f"intermix ratio: {self.warp_core.intermix_ratio}")
        self.containment_seals = tk.StringVar(self.main, f"antimatter containment: {self.warp_core.contained}")
        self.EPS_L_pressure = tk.StringVar(self.main, f"left EPS manifold pressure: {self.LEPS.pressure}")
        self.EPS_L_temperature = tk.StringVar(self.main, f"left EPS manifold temperature: {self.LEPS.temperature}")
        self.EPS_L_flow = tk.StringVar(self.main, f"left EPS manifold flow: {self.LEPS.flow}%")
        self.EPS_R_pressure = tk.StringVar(self.main, f"right EPS manifold pressure: {self.REPS.pressure}")
        self.EPS_R_temperature = tk.StringVar(self.main, f"right EPS manifold temperature: {self.REPS.temperature}")
        self.EPS_R_flow = tk.StringVar(self.main, f"right EPS manifold flow: {self.REPS.flow}%")
        self.EPS_L_clear = tk.StringVar(self.main, f"left EPS plasma flow clearance: {self.LEPS.clearance}")
        self.EPS_R_clear = tk.StringVar(self.main, f"right EPS plasma flow clearance: {self.REPS.clearance}")
        self.warp_speed = tk.StringVar(self.main, f"maximum warp speed: {self.warp_coils.warp_speed}")

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
        self.L_EPS_C_lbl = tk.Label(self.frames[1][1], textvariable=self.EPS_L_clear)
        self.R_EPS_C_lbl = tk.Label(self.frames[1][1], textvariable=self.EPS_R_clear)
        self.warp_lbl = tk.Label(self.main, textvariable=self.warp_speed, bg="light blue", padx=5, pady=3, font="bold 18")

        #static labels
        self.EPWR_lbl = tk.Label(self.main, text = "emergency power online", bg="light blue")
        self.dilitium_integrity = tk.Label(self.frames[0][0], text="dilithium crytaline structure monitor", bg="light blue")
        self.alignment_monitor = tk.Label(self.frames[0][0], text="dilithium articulation frame alignment monitor", bg="light blue")
        self.output_regulation = tk.Label(self.frames[0][1], text="warp core output regulation", bg="light blue")
        self.EPS_monitor = tk.Label(self.frames[1][0], text="EPS plasma monitor", bg="light blue")
        self.breach_monitor = tk.Label(self.frames[1][1], text="containment breach/blockage monitor", bg="light blue")

        #buttons
        self.align_btn = tk.Button(self.frames[0][0], text="align", command= lambda: self.align(0))
        self.regulator_output_btn = tk.Button(self.frames[0][1], text="set regulator output", command= lambda: self.set_output(self.reg_out_entry.get()))
        self.TMC_btn = tk.Button(self.frames[0][0], text="toggle theta-matrix compositor", command= self.toggle_TMC)
        self.ratio_btn = tk.Button(self.frames[0][1], text="set intermix ratio", command= lambda: self.set_ratio(self.ratio_entry.get()))
        self.flush_LEPS = tk.Button(self.frames[1][1], text="flush left EPS manifold", command=self.FlushLEPS)
        self.flush_REPS = tk.Button(self.frames[1][1], text="flush right EPS manifold", command=self.FlushREPS)
        
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

        self.alignment_monitor.pack(fill="x")
        self.align_err_lbl.pack(fill="x")
        self.align_btn.pack(fill="x")

        self.output_regulation.pack(fill="x")
        self.reg_out_lbl.pack(fill="x")
        self.reg_out_entry.pack(fill="x")
        self.regulator_output_btn.pack(fill="x")
        self.ratio_lbl.pack(fill="x")
        self.ratio_entry.pack(fill="x")
        self.ratio_btn.pack(fill="x")

        self.EPS_monitor.pack(fill="x")
        self.L_EPS_F_lbl.pack(fill="x")
        self.L_EPS_P_lbl.pack(fill="x")
        self.L_EPS_T_lbl.pack(fill="x")
        self.R_EPS_F_lbl.pack(fill="x")
        self.R_EPS_P_lbl.pack(fill="x")
        self.R_EPS_T_lbl.pack(fill="x")

        self.breach_monitor.pack(fill="x")
        self.containment_lbl.pack(fill="x")
        self.L_EPS_C_lbl.pack(fill="x")
        self.flush_LEPS.pack(fill="x")
        self.R_EPS_C_lbl.pack(fill="x")
        self.flush_REPS.pack(fill="x")

    def FlushLEPS(self):
        self.LEPS.clearance = 1.00
        #self.EPS_L_clear.set(f"left EPS plasma flow clearance: {self.LEPS.clearance}")
        self.update_data()

    def FlushREPS(self):
        self.REPS.clearance = 1.00
        #self.EPS_R_clear.set(f"right EPS plasma flow clearance: {self.REPS.clearance}")
        self.update_data()

    def align(self, new_error):
        self.A_frame.error = new_error
        #self.alignment_error.set(f"dilithium matrix allignment error: {self.A_frame.error}%")
        self.update_data()

    def set_output(self, new_output):
        try:
            new_output_F = float(new_output)
        except ValueError:
            new_output_F = 0.0
        self.dil_reg.output = new_output_F
        #self.regulator_output.set(f"dilithium regulator output throttle: {self.dil_reg.output}%")
        self.update_data()

    def toggle_TMC(self):
        # self.TMcompositor.set(f"theta-matrix compositor runing: {status}")
        self.TMC.toggle_compositor()
        self.update_data()

    def set_ratio(self, new_ratio):
        try:
            new_ratio_F = float(new_ratio)
        except ValueError:
            new_ratio_F = 0.0
        self.warp_core.intermix_ratio = new_ratio_F
        # self.intermix_ratio.set(f"intermix ratio: {self.warp_core.intermix_ratio}")
        self.update_data()
    
    #runs everytime a button is pressed, computes the data and updates the display values
    def update_data(self):
        self.REPS.temperature = self.dil_matrix.crystalization * self.dil_reg.output * (1/(2**self.A_frame.error)) * self.warp_core.intermix_ratio
        self.LEPS.temperature = self.dil_matrix.crystalization * self.dil_reg.output * (1/(2**self.A_frame.error)) * self.warp_core.intermix_ratio
        self.REPS.pressure = self.REPS.temperature * 2
        self.LEPS.pressure = self.LEPS.temperature * 2
        self.REPS.flow = self.dil_reg.output * self.REPS.clearance * self.REPS.pressure / 20000
        self.LEPS.flow = self.dil_reg.output * self.LEPS.clearance * self.LEPS.pressure / 20000
        self.warp_coils.flow = (self.REPS.flow + self.LEPS.flow)/2
        self.warp_coils.temperature = (self.REPS.temperature + self.LEPS.temperature)/2
        self.warp_coils.pressure = (self.REPS.pressure + self.LEPS.pressure)/2
        self.warp_coils.warp_speed = (self.warp_coils.temperature/10000) * (self.warp_coils.pressure/20000) * (self.warp_coils.flow/100) * 8
        
        if (self.dil_reg.output * self.warp_core.intermix_ratio) > 150:
            self.dil_matrix.crystalization = 100 / ((self.dil_reg.output * self.warp_core.intermix_ratio)/150) 

        if self.warp_core.intermix_ratio > 3.5:
            self.A_frame.error = self.warp_core.intermix_ratio + self.A_frame.error

        if self.REPS.temperature < 2500:
            try:
                self.REPS.clearance = self.REPS.clearance - 1/(2500/self.REPS.temperature) 
            except ZeroDivisionError:
                self.REPS.clearance = 0.0

        if self.LEPS.temperature < 2500:
            try:
                self.LEPS.clearance = self.LEPS.clearance - 1/(2500/self.LEPS.temperature) 
            except ZeroDivisionError:
                self.LEPS.clearance = 0

        if self.TMC.run == True:
            if self.dil_matrix.crystalization >= 100:
                self.TMC.toggle_compositor()
                self.dil_matrix.crystalization = 100
            else:
                self.dil_matrix.crystalization = 100

        # print(self.warp_coils.warp_speed)

        if self.warp_coils.warp_speed > 10.0:
            self.warp_core.contained = False
            self.warp_speed.set(f"maximum warp speed: 0. Warp core critical containment breach!")
        elif self.warp_coils.warp_speed <= 0:
            self.warp_speed.set(f"maximum warp speed: 0")
        else:
            self.warp_core.contained = True
            self.warp_speed.set(f"maximum warp speed: {self.warp_coils.warp_speed}")

        self.alignment_error.set(f"dilithium matrix allignment error: {self.A_frame.error}%")
        self.regulator_output.set(f"dilithium regulator output throttle: {self.dil_reg.output}%")
        self.crystalization.set(f"dilithium matrix crystalization: {self.dil_matrix.crystalization}%")
        self.TMcompositor.set(f"theta-matrix compositor runing: {self.TMC.run}")
        self.intermix_ratio.set(f"intermix ratio: {self.warp_core.intermix_ratio}")
        self.containment_seals.set(f"antimatter containment: {self.warp_core.contained}")
        self.EPS_L_pressure.set(f"left EPS manifold pressure: {self.LEPS.pressure}")
        self.EPS_L_temperature.set(f"left EPS manifold temperature: {self.LEPS.temperature}")
        self.EPS_L_flow.set(f"left EPS manifold flow: {self.LEPS.flow}%")
        self.EPS_R_pressure.set(f"right EPS manifold pressure: {self.REPS.pressure}")
        self.EPS_R_temperature.set(f"right EPS manifold temperature: {self.REPS.temperature}")
        self.EPS_R_flow.set(f"right EPS manifold flow: {self.REPS.flow}%")
        self.EPS_L_clear.set(f"left EPS plasma flow clearance: {self.LEPS.clearance}")
        self.EPS_R_clear.set(f"right EPS plasma flow clearance: {self.REPS.clearance}")

        #self.main.update()
    
    #runs the tk mainloop
    def run(self):
        self.main.mainloop()