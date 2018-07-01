$root_hash = @{}

# CPU
Get-WmiObject -Class Win32_Processor
$processer = Get-WmiObject -Class Win32_Processor
$cpuname = $processer.Name
$root_hash.Add('cpu', $cpuname)

# メモリ
$memory_hash = @{}
Get-WmiObject -Class Win32_PhysicalMemory
$memorys = Get-WmiObject -Class Win32_PhysicalMemory
$count = 0
foreach ($memory in $memorys) {
    $count += 1
    $memory_key = "memory_{0}" -f $count
    # Write-Host $memory_key
    $memory_hash.Add($memory_key, @{Capacity = $memory.Capacity / 1GB; Manufacturer = $memory.Manufacturer})
}
$root_hash.Add('memory', $memory_hash)

# チE��スク容釁E
$count = 0
# Get-WmiObject -List | Select-String "physical"
$physicalDisk_hash = @{}
$physicalDisks = Get-WmiObject -Class Win32_PhysicalMedia
Get-WmiObject -Class Win32_PhysicalMedia
foreach ($physicalDisk in $physicalDisks) {
    $count += 1
    $disk_key = ""
    Write-Host $physicalDisk.MediaType
    if ($physicalDisk.MediaType -eq 3) {
        $disk_key = "HDD_{0}" -f $count
    }
    elseif ($physicalDisk.MediaType -eq 4) {
        $disk_key = "SSD_{0}" -f $count
    }
    else{
        $disk_key = "other_{0}" -f $count
    }
    $physicalDisk_hash.Add($disk_key, @{Size = $physicalDisk.Size / 1GB; MediaType = $physicalDisk.MediaType})
}
$root_hash.Add('disk', $physicalDisk_hash)
$count = 0
$logicalDisk_hash = @{}
$logicaldisks = Get-WmiObject Win32_LogicalDisk
foreach ($logicalDisk in $logicalDisks) {
    $count += 1
    $disk_key = ""
    Write-Host $logicalDisk.MediaType
    if ($logicalDisk.DriveType -eq 3) {
        $disk_key = "logical_HDD_{0}" -f $count
    }
    elseif ($logicalDisk.DriveType -eq 4) {
        $disk_key = "logical_SSD_{0}" -f $count
    }
    elseif ($logicalDisk.DriveType -eq 5) {
        $disk_key = "logical_DVD_{0}" -f $count
    }
    else{
        $disk_key = "logical_other_{0}" -f $count
    }
    $logicalDisk_hash.Add($disk_key, @{Size = "{0}GB" -f ($logicalDisk.Size / 1GB); DriveType = $logicalDisk.DriveType; VolumeName = $logicalDisk.VolumeName; DeviceID = $logicalDisk.DeviceID})
}
$root_hash.Add('logical_disk', $logicalDisk_hash)
ConvertTo-Json $root_hash| Out-File -FilePath "C:\Users\user\Documents\jsontest.json"