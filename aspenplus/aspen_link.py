import os
import win32com.client as win32


def init_aspen():
    print('Connecting to Aspen Plus App')
    aspen = win32.Dispatch('Apwn.Document')
    aspen.InitFromArchive2(os.path.abspath('C:\Users\c160102\Downloads\Group 12 Interim Report Simulation (Waste Plastic Valorisation Plant) GL_Calista Loh Si Ying VGL_Wang Yixuan\plastics.bkp'))
    return aspen