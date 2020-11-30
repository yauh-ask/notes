There are three main types of data storage:

File storage
Block storage
Object storage
Let’s discuss what they are starting with file storage.

What is file storage? #
File storage is a hierarchical storage methodology where the data is stored in files, the files are stored in folders, and the folders are stored in directories.

This storage mechanism is primarily used in DAS and NAS. The data in our desktops, laptops, and smartphones is stored using the file storage mechanism. To locate and access files in storage, we just need the complete path to the file.

However, this storage methodology is only good for a limited amount of data, primarily structured data. As the size of the data grows beyond a certain point, using this storage mechanism becomes a hassle. Retrieving files from a large amount of unstructured data takes a long time via this approach.

To tackle this scenario, we leverage other types of storage mechanisms such as block and object storage.

Upsides of using the file storage mechanism to store data #
File storage is best suited for simple data storage use cases. If we need an easy-to-access, affordable, and centralized location to store our data, file storage is a good pick.

Leveraging this storage mechanism, we can also share files in a local area network. We do this all the time, especially on a university campus where a system in the network hosts the data and all the other systems can download that data facilitated by the file storage mechanism.

We can also set up a small storage environment for ourselves using file storage on a NAS device. This allows us to take backups of data on separate storage devices connected to the LAN.

Cloud file storage #
All the major cloud providers provide the managed file storage service in the cloud. The primary difference between setting up our own on-prem file storage and using the cloud file storage is that when using the cloud file storage our data is hosted by the cloud data centers, and we can leverage all the features that are typically offered by the cloud environment, such as disaster recovery, backup, elasticity, scalability, redundancy, high availability, and so on.

Google Cloud Filestore and AWS Elastic File System are examples of cloud-based file storage services.

These services are completely managed services providing low latency and high throughput operations for file-based workloads.

Some of the typical use cases for file storage are:

Sharing files among the team members, enabling the developers to work on the same file in collaboration. Files can be hosted using cloud file stores and can be shared with anyone in the team securely.

Delivering static file-based web content like graphics, videos, images, and other types of media with minimal latency to the end-users

Processing and conversion of media files from one format to another. File stores come in handy when building a system that takes one form of media file as input and converts it into another form of media. Image conversions and rendering of animation are good examples of this.

What is block storage? #
Block storage is the data storage technique where data is broken down into blocks of equal size and each individual block is given a unique identifier for easy accessibility.

These blocks are stored in physical storage wherever it is most efficient. As opposed to adhering to a fixed path as in a file system, blocks can be stored anywhere in the system, making more efficient use of the resources.

When the client requests information from a block storage system, it re-assembles the blocks based on the request and returns the information to the client. This approach facilitates efficient, fast, and reliable movement of data over the network. It offers more storage efficiency and performance than file storage.

Block storage is largely used by storage area networks and larger cloud-based environments. It is the storage of raw data that is decoupled from the environment. The data is abstracted from the environment, just like containers abstract the application from the environment.

Block storage in the cloud #
Persistent disks and local transient disks that are attached to the compute instances offer block storage in a cloud environment.

Block storage provides more granular control over the data and also offers consistent performance. It is well suited for both high throughput and transaction-intensive workloads such as relational and NoSQL databases, media streaming, big data analytics, and so on.

Google Cloud Persistent Disk and Amazon Elastic Block Store are examples of block storage cloud service.

What is object storage? #
Object storage is the storage that is designed to handle large amounts of unstructured data. This is the data that has no structure and largely consists of a mix of emails, images, audio files, text files, IoT data, videos, and so on.

This kind of data is continually generated in massive amounts on social platforms and from the IoT devices. Therefore, we need a storage system that can handle data influxes efficiently and economically.

Object storage is also the preferred storage model for data archiving and taking data backups as it offers dynamic scalability, unlike any other storage models. It can easily handle petabyte and Exabyte scale data on an ongoing basis.

How does object storage work? #
Just like block storage, every data object in an object storage system contains a unique identifier for easy accessibility. Objects also contain metadata attached to them.

Attaching metadata with objects helps with the implementation of data policies, data protection, validation of the authenticity of the content, running business analytics, and so on.

This metadata can also be customized based on the business requirements. For instance, we can customize the metadata of an image to add information, including from what device the image was captured, the people or the objects in the image, the date and location of the image, image category, filters applied on the image, etc.

Once this meta information is added to the images, they can be easily located and retrieved based on meta-information like fetching images belonging to a certain category, those captured by a certain camera, so on.

Storage of meta information of this level is not possible with other storage types, such as block and file. The data stored with block and file storage contains very basic meta-information.

Storing data in objects helps with the performance big time when dealing with petabyte and Exabyte scale data. The stored objects are further aggregated into object pools and are spread across the clusters and regions for scalability, high availability, and disaster recovery. This is the reason object storage is widely used by businesses running their workloads on the cloud.

Accessing object store data #
Object store data is accessed over the web via REST APIs. The data is mostly stored in virtual machines running on commodity bare-metal servers. Developers use the APIs provided by the cloud providers to read and write data in the object store managed by the cloud.

The provider is responsible for making the data redundant, setting up disaster recovery, and so on. Fundamentally, cloud storage provides all the features that a cloud typically provides for a workload, such as high availability, scalability, elasticity, durability, and security, a distributed environment facilitating storage for massive amounts of data, pay for what you use pricing model, and so on.

Just in case you are wondering what the difference between a database and data storage is, data storage entails the storage of raw data in physical storage like HDDs and SSDs, while databases contain software that manages the raw data. Both the database software and the physical data storage together make the database component in a web application.

Object storage in the cloud #
Object storage is like the native storage for the cloud. The objects that can be files of any format are stored in the buckets. A bucket is a container for the object. A project may contain multiple buckets.

To store objects, a developer has to first create a bucket. Once the bucket is created, he can upload the objects to the bucket using the REST API. Any object we store in a cloud object store should be contained in a bucket, and there is a reason for that.

Just like containers isolate the workloads from the outer world, buckets isolate objects from the outer world. Buckets facilitate access management; only the entities having the right authorization can access the objects. Buckets also facilitate data encryption, object versioning, object access management, and so on.

In a project, we can create different buckets based on the type of objects being stored. For instance, videos can be stored in one particular bucket and user images can be stored in another bucket.

When creating a new bucket, we give it a unique name, geographic location (where we want our bucket to reside), and storage class. 

The unique identifier of the object, also known as the key, the bucket, and the object version uniquely identify an object in an object-store.

Developers can interact with the cloud object store via the command line tools and browser-based console, using the SDKs, client libraries, and also the REST APIs.

Standard storage #
Standard storage is a general-purpose object storage class that suits best for use cases where the data is accessed pretty frequently, like a NoSQL database in an online game.

Typical use cases include streaming media content and online gaming application data and serving dynamic web content, mobile applications, big data analytics, and so on.

Standard storage offers the highest level of availability and durability of data in comparison to other storage classes. It offers low latency and high throughput.

Nearline storage #
Nearline storage, also known as the Vault or the Standard-Infrequent Access storage class, is a low cost, durable storage for storing data that is accessed on average once per month. The availability of this storage is a bit lower than standard storage. Also, it’s comparatively cheaper.

This storage class is a middle ground between data archival and frequently accessed hot data. This kind of storage is a good fit for long-tail content that is not accessed much and data backups.

Coldline storage #
Coldline storage class suits best for storing data that is accessed on average once every three months. The costs of storing data in this storage class are lower than the nearline storage.

Archival storage #
Archival storage is a data storage class intended for long term data storage, storing data that is accessed less than once a year. The costs of storing data in this class are the lowest of all the storage classes.

Although the data can be accessed within milliseconds as opposed to hours or days, this storage class has no SLA availability. Archival storage class works best for storing disaster recovery data, historic data, etc.

Traditionally in IT, archival data is stored in storage disks or magnetic tape. Magnetic tapes that are used for storing data are also known as tape drives. Both ways of archiving data require a lot of management overhead.

When archiving data with an object store, we can easily access the archived data within milliseconds. We don’t have to worry about managing and protecting physical tapes, replication and redundancy of tape data, and so on.

Archiving data using the cloud object store is far better than implementing traditional methods of archiving data.

Intelligent storage class #
If the developers are uncertain about what storage class to choose, cloud providers also offer an intelligent storage class. This class continually monitors the data and splits it into two access tiers: active and not so active.

The active tier contains the data that is frequently accessed, and the not so active tier contains data that is not so frequently accessed.

If certain data in the active tier doesn’t get accessed for a while, the intelligent tier automatically moves it to the not so active tier.

With the cloud object store, developers have complete control over their data. They can set the _ time to live (TTL)_ for their objects, archive the data that hasn’t been accessed for a while, upgrade or downgrade storage classes without having an impact on the latency and the accessibility of the service, and so on.

