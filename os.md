### Evolution OS
- Serial Processing,e.g. physical managing of vacuum cleaner or huge computers in a stone age 
- Simple Batch System, aka launching the processes by batches (task execution was/is not immediate). CPU is supposed to be utilized, but not napping on the background while memory etc. works.
Solution was uniprogramming => multiprogramming (problem: CPU vs human brain => switching from one process to another is doable, but energy-consuming).
- Time Sharing System, eg CTSS.

Kernel Mode (hardware) and User Mode (software, GUI etc. for humans)

Virtual Memory: independent schemes of memory re-direction for separate processes, memory protection between applications, additional memory.

Kernel OS: monolithic kernel(hardware =+ device drivers, dispatchers, scheduler, virtual memory, IPC, File System, VFS) and microkernel (hardware =+ Basic IPC, virtual memory, schedulin)
