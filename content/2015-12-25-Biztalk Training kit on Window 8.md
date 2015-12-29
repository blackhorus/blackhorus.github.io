---
Title: Install biztalk training kit on windows with Hyper-V.
Date: 2015-12-25
Excerpt: Simple way to install the training kit on any machine with Hyper-V (Script included).
---

*Please note that by default, Hyper-V is not activated and should be to lunch the vm's.*

I struggled a lot to make these lab working on my windows 8.1 machine. First, I get this error when trying to lunch the simple **importVM.exe **command as described by the official instruction you get when you download the training kit:

    System.ApplicationException: Error while importing the Hyper-V configuration settings for bt10d-01. ---> System.Management.ManagementException: Non trouvé 

Then, I started to search on the internet, but no solution was offered to import proprely the vm's, all the articles I found were describing the fact that you should have a windows 2008 machine, or remove the configuration file ([xml file](http://blogs.technet.com/b/rmilne/archive/2013/05/31/hyper-v-did-not-find-virtual-machine-to-import.aspx))
    
You should understand that the training kit comes with a master virtual machine (**BizTalk2010Demo.vhd** found inside the common folder). This vhd file host a windows 2008 OS, and everything you need to complete the hand-on lab (e.g. Visual studio, sharepoint, sql server,...). And beside it, there is a lot of differencing disks each on a seperate folder (**bt10d-01** to **bt10d-19**)

> **Note** A differencing disk is a virtual hard disk (VHD) that stores changes made to another VHD or to the guest operating system. The purpose of differencing disks is to make it possible to maintain information about changes made so that they can be reversed if necessary. ([source](http://whatis.techtarget.com/definition/differencing-disk))

The easiest way was to mount every differencing disk on its own VM. Instead of doing this manually, I managed to jot a simple script to do this for you. 

Here's a simple powershell script that I wrote to help you create a vm for every lab, and mount the supplied vhd disks. 

 
### Script ###

This script will create 17 virtual machine, each with 2GB of memory. It will attach the lab and the vhd for the demo files (**bt10t-allfiles.vhd**) in the created vm.

Copy & paste this in a ps1 file, lunch powershell as admin, and execute this script.

```powershell
$absolutePath = ""

# So we can execute this script.
set-executionpolicy remotesigned
<#  
Source : https://social.technet.microsoft.com/Forums/en-US/464ff2b2-e24a-4c82-a367-07e60a43c1b8/how-to-use-a-browseforfolder-box-in-my-powershell-script?forum=ITCG
#>
function Select-Folder($message='Select a folder', $path = 0) {
    $object = New-Object -comObject Shell.Application
    $folder = $object.BrowseForFolder(0, $message, 0, $path)  
    if ($folder -ne $null) {
    	$folder.self.Path
    	}
}

<# 
 Should we point to the right path for every VM based on a number...
#>
function ConstructPath($x)
{
    $number = "{0:D2}" -f $x
    $folder = $absolutePath + "\bt10d-" + $number + "\Virtual Hard Disks\bt10d-"+ $number+".vhd"
    return $folder
}

<# 
Main entry for the script.
#>
$absolutePath = Select-Folder 'Select the folder where the folder vm''s reside'
If (-not $absolutePath) 
	{ Write-Host 'No folder was selected.' }
else 
{
    $commonPath = $absolutePath + "\common\bt10t-allfiles.vhd"
    
    for($i=1; $i -le 19; $i++)
    {
	    #no folder for the 2 or 3 lab.
	    if ($i -eq 2 -or $i -eq 3) {continue}
	    
	    #based on i construct the absoule path
	    $path = ConstructPath($i)
	    
	    $LabName = "Lab-" + "{0:D2}" -f $i
	      
	    #Create the VM, and add it the the disks.
	    New-VM -Name $LabName –MemoryStartupBytes 2GB
	    Add-VMHardDiskDrive -VMName $LabName -path $path
	    Add-VMHardDiskDrive -VMName $LabName -path $commonPath
    }
}
```