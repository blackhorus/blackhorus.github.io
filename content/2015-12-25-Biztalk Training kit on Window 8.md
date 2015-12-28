---
Title: Install biztalk training kit on windows 8.1
Date: 2015-12-25
Excerpt: How to install Microsoft Biztalk 2010 training kit on windows 8, 8.1 or 10
---

*Please note that by default, Hyper-V is not activated and should be to follow the steps described on this article.*

I struggled a lot to make these lab working on my windows 8.1 machine. First, I get this error when trying to lunch the simple **importVM.exe **command as described by the official instruction you get when you download the training kit:

    System.ApplicationException: Error while importing the Hyper-V configuration settings for bt10d-01. ---> System.Management.ManagementException: Non trouvé 

Then, I started to search on the internet, but no solution was offered to import proprely the vm's, all the articles I found were describing the fact that you should have a windows 2008 machine, or remove the configuration file ([xml file](http://blogs.technet.com/b/rmilne/archive/2013/05/31/hyper-v-did-not-find-virtual-machine-to-import.aspx))
    
You should understand that the training kit comes with a master virtual machine (**BizTalk2010Demo.vhd** to be found inside the common folder). This vhd file host a windows 2008 OS, and everything you need to complete the hand-on lab (e.g. Visual studio, sharepoint, sql server,...). And beside it, there is a lot of differencing disks each on a seperate folder (bt10d-01 to bt10d-19)

> **Note** A differencing disk is a virtual hard disk (VHD) that stores changes made to another VHD or to the guest operating system. The purpose of differencing disks is to make it possible to maintain information about changes made so that they can be reversed if necessary. ([source](http://whatis.techtarget.com/definition/differencing-disk))

The easiest way was to mount every differencing disk on its own VM. Please note that you should repeat theses for every lab (there are 19 labs). Following screenshot is given for the fifth lab :

## Steps ##

- Launch the Hyper-V manager and create a new virtual machine.

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/01.jpg)

- Give it a meaningful name, as we'll create ~16 VM.

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/02.jpg)

- When asked to create a new hard disk (VHD), choose to create this after the completed wizard!

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/03.jpg)

- After finishing, head over to the settings of the newly created VM, and add a new Hard drive (IDE0 branch).

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/04.jpg)

- Choose to create a new hard disk. Here we'll fool Hyper-V by submitting a dummy vhd file, and change it after we complete the wizard with the one that was supplied with microsoft training kit. Bonus: Choose the folder of **bt10d-xxx** as it will be easy after to change just the name.

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/05.jpg)

- Choose a differenciation one !
 
![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/06.jpg)

- Give it a dummy name, as we'll change it with the one supplied in the biztalk training kit!

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/07.jpg)

- When asked for the parent, browse for the **Biztalk2010Demo.vhd** file found in the common folder

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/07-1.jpg)

Return to the settings of the newly created vm, and change the name to microsoft vhd file, in our example, it will be : **bt10d-05.vhd**. And by the way, don't forget to remove the dummy file you created with this vm, as we'll not need it.

**Optionnal** If you want to have access to the complete lab files inside the Biztalk vm, you should attache the bt10t-allfiles.vhd found on the same folder as the biztalk2010demo file. 

![](https://dl.dropboxusercontent.com/u/574142/gitHub%20images/09.jpg)
