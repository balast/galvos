import configparser
import writeEC1000file as EC
from os import path

def read_scan_params_create_xml(scan_params_filepath, ec1000_xml_savepath):
    #Inputs
    # scan_params_filepath = path.abspath(r'E:\OCT Data\2018-04-25 AutoSection Test Data\15by15\scan_params.txt')
    # ec1000_xml_savepath = path.abspath(r'E:\OCT Data\2018-04-25 AutoSection Test Data\15by15\15by15.xml')
    # scan_params_filepath = path.abspath(r'C:\Users\LAMPS_SLS\Documents\Builds\Adam\2018-05-25 3PointBars\oct_scan\scan_param_bar{}.txt'.format(i))
    # ec1000_xml_savepath = path.abspath(r'C:\Users\LAMPS_SLS\Documents\Builds\Adam\2018-05-25 3PointBars\oct_scan\oct_scan_bar{}.xml'.format(i))

    #Read Folder
    config = configparser.ConfigParser()
    config.read(scan_params_filepath)
    p = config['Scan_Parameters']

    #create file
    EC.write_oct_ec1000_file(ec1000_xml_savepath, float(p['left_crd']), float(p['top_crd']), float(p['scan_width']), float(p['scan_height']), float(p['start_delay']), float(p['hatch_spacing']), float(p['galvo_speed']))

scan_params_filepath = r'C:\Users\LAMPS_SLS\Documents\Builds\Adam\2018_10_31 Curl Part\oct_scan\Reg\scan_param.oct_config'
ec1000_xml_savepath = r'C:\Users\LAMPS_SLS\Documents\Builds\Adam\2018_10_31 Curl Part\oct_scan\Reg\oct_scan.xml'
read_scan_params_create_xml(scan_params_filepath, ec1000_xml_savepath)



