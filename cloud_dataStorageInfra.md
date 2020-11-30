Direct Attached Storage (DAS) #
Direct Attached Storage, or DAS means the physical storage is directly attached to the computer. Our desktops and laptops are examples of this, where the hard drives are directly attached to the CPU in the same machine.

Besides the hard drives, we also directly attach external storage, such as pen drives, external hard drives, optical disk drives, etc., onto our laptops.

Anything that can be directly attached to the computer is known as Direct Attached Storage.

DAS offers data that is quick to access and secure because it is not transmitted over the network. There is no possibility of eavesdropping and so on. The data storage capacity it offers may suffice for an individual user, but businesses with much larger data storage requirements will struggle with the DAS approach.

One more thing: what if the business has data that needs to be shared across multiple machines in the network? How do we achieve this with DAS?

We can’t. For this use case, we need Network Attached Storage, or NAS.

Network Attached Storage #
In a Network Attached Data Storage setup, the data is accessed over a network as opposed to residing locally in the machine along with the compute. Additionally, the file system and the physical storage are coupled together and are accessed over the network.

NAS is pretty useful when the data is to be accessed by a number of machines in the network. We can centrally store the data of the business, and the employees can access that data over a secure network. NAS also offers more storage capacity than an individual machine can offer.

In this setup, we can arrange multiple hard drives in RAID for redundancy. NAS works best for the small storage needs typically required by small-scale businesses.

However, there is one downside of NAS: since the data is stored in a centralized location, the setup has a single point of failure. If the storage component fails, no devices in the network can access the data.

Storage Area Network #
Storage Area Network, or SAN, is set up to store and access large amounts of data, typically required by big businesses, over the network.

SAN has the capacity to store a lot more data than what can usually be stored with NAS. The file system in SAN stays with the application and only raw blocks of data are fetched over the network.

The SAN setup is fault-tolerant since multiple storage servers are set up in the network. Data is shared among different storage servers, and it’s also made redundant to avoid data loss due to machine failure. This makes the setup highly available. If a server goes down, the data can still be accessed from the redundant storage servers.

SAN also facilitates automatic data backup and storage monitoring. However, it is expensive to set up, due to its complexity, and it is primarily used by large organizations.

In a cloud data center, DAS means the persistent and transient disks are directly attached to the computing instance. These disks can be internally attached to the compute in the form of boot disks, or they can be externally attached in form of an external hard drive.

In a cloud environment, you can also set up your NAS or SAN based on your requirements. In this scenario, the business accesses the infrastructure over the web, and the cloud provider bills the business on the amount of storage consumed, network bandwidth consumed, API requests made for data read and write operations, etc.

What are persistent disks? #
Persistent disks are reliable, durable, and highly performant block storages for compute instances.

The persistent disk storage can be easily replicated, made redundant, and resized in capacity across the different availability zones and regions across the world. Furthermore, multiple VMs can read the data from a single persistent disk, or in other words, they can share a persistent disk between them without having any major impact on the disk’s performance.

Since the disk is persistent, whatever data is stored on it remains even after the compute instances are decommissioned from the cluster.

Cloud takes care of managing the persistent disks and distributing the data across the globe for the business.

A persistent disk provides both _ hard disk drive (HDD)_ & _ solid-state drive (SSD)_ storage for the compute. Both have their unique use cases. A solid-state drive is preferred when the business wants very low latency, and a hard disk drive is preferred when a business wants low-cost storage. SSDs are more expensive than HDDs.

Hard disk drive (HDD) and solid-state drive (SDD) #
A hard disk drive is an electromechanical storage device that has a rotating disk coated with magnetic material. On the other hand, a solid-state drive uses an _ Integrated Circuit (IC)_ with flash memory to store data. It doesn’t have a physical spinning disk. This makes SSDs more resistant to physical shocks. Also, the use of flash memory cuts down the latency significantly.

When it comes to archival storage HDDs are the preferred choice since semiconductor-based solid-state drives tend to lose data over time if left for long periods without power. HDDs are also more affordable in comparison to SSDs. A large amount of data can be stored with a lot less expense with HDDs, as opposed to when using SSDs. SSDs are typically used to implement a distributed cache layer where low latency is vital.

Returning to persistent disks, they are measured by a metric known as IOPS, which is input-output operations per second. So, if we need high IOPS, we would pick an SSD because they provide latencies in as low as single-digit milliseconds.

If we need to process a large amount of workload data having sequential read-write operations, we would pick a standard HDD persistent disk.

Transient disks #
Transient disks are SSDs that are attached to the compute, and they store data of a specific instance as long as it is not terminated. If the compute instance is decommissioned, all the data is wiped off the transient SSD disk. Also, the data on a transient disk is non-redundant.

A persistent disk may be deployed in isolation decoupled from VMs, but a local transient SSD is generally co-located with the VMs.

Why do we need transient disks?

Transient SSD disks provide lower latency than persistent SSDs. So, if you need to perform a very high IOPS operation with low latency, a transient SSD would be a good option.

