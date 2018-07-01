# coding:utf-8

import subprocess
import wmi
import json

con = wmi.WMI()
GB = 1024 * 1024 * 1024

def get_os(con):
    result = {}
    for os in con.Win32_OperatingSystem():
        # print(os)
        result["os_now"] = "{0} (Version {1})".format(os.Caption, os.Version)

    return result

def get_cpu(con):
    result = {}
    for cpu in con.Win32_Processor():
        result["cpu"] = cpu.Name
        # print(cpu.Caption)
        # print(cpu.Name)
        # print(cpu.DeviceID)
        # print(cpu.Description)

    return result

def get_disk(con):
    result = {}
    disk = {}
    count = 0
    logical_disks = con.Win32_LogicalDisk()
    for logical_disk in logical_disks:
        count += 1
        # print(logical_disk)

        

        def get_media_type(logical_disk):
            disk_type = ""
            if logical_disk.MediaType == 3:
                disk_type = "HDD"
            elif logical_disk.MediaType == 4:
                disk_type = "SSD"
            else:
                disk_type = "OTHER"

            return disk_type

        def get_size(logical_disk):
            size = 0
            if logical_disk.Size:
                size = float(logical_disk.Size) / GB
            return size

        disk["{0}_{1}".format(get_media_type(logical_disk),count)] = "{0}: {1}GB".format(get_media_type(logical_disk), get_size(logical_disk))
        result["disk"] = disk
        return result

MEMORY_FORMAT = "{manufacturer}({device_locator})_{size}GB"
    
def get_memory(con):
    result = {}
    memory_dict = {}
    size = 0
    count = 0

    for memory in con.Win32_PhysicalMemory():
        # print(memory)
        
        size = float(memory.Capacity) / GB
        memory_dict["memory_{0}".format(count)] = MEMORY_FORMAT.format(manufacturer=memory.Manufacturer, device_locator=memory.DeviceLocator,size=size)
        count += 1

    result["memory"] = memory_dict
    return result
            
    

if __name__ == '__main__':

    result = {}

    result.update(get_os(con=con))
    result.update(get_cpu(con=con))
    result.update(get_disk(con=con))
    result.update(get_memory(con=con))

    print(result)
    json_str = json.dumps(result)
    print(json_str)

    
    
    

    count = 0
    
        
