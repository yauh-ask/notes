S3 - Simple Storage Service
AWS S3 - Simple Storage Service what is it? and where would you use it? Also take a look at an architecture using S3.

Fundamentally there are two types of storage:-

Object-Based Storage
Block Based Storage
Simple Storage Service (S3) - Object-Based Storage
Provides developers and IT Teams with secure durable, highly scalable object storage. Easy to use simple web interface to store and retire any amount of date from anywhere on the web.

It is a place to store your files on the AWS cloud Dropbox was born. By simplifying the User interface of S3. Think about Dropbox as a layer built on top of S3.

Data is spread across multiple devices and facilities

Think about S3 to store your photos or files.

Object Base Storage
Unlimited Storage
Files are Stored in Buckets/Folders
Names must be unique globally
Every time you have a successful upload you get a http 200 code back
S3 Is primarily used for:-

Store and Backup
Application File Hosting
Media Hosting
Software Delivery
Storing AMI’s and Snapshots
Data consistency Model – S3
Read after write consistency for PUTS of new objects Eventual consistency for overwrite PUTS and deletes (i.e. takes time to propagate)

Objects Consists of the following

Key – this is simply the file name of the object
Value – the data and it is made up of a sequence of bytes.
Versioning – which version of the object is this
Meta Data: Data about data, the data about the data file you are storing.
Think, if you are storing a music track/song. This would have metadata like the information of the singer, the year it was released, the name of the album etc.

Sub resources –

Access Control list – this determines was can access the file on S3. This can be done at the file level or at the Bucket level.
Torrent – supports the Bit torrent protocol
Built for 99.99% availability of the S3 Amazon SLA 99.9% platform
Durability guarantee – 99.9… (11.9s) (more)?
Tiered storage Availability
Lifecycle management
Versioning
Encryption
Secure the data using Access control lists and Bucket policies
S3 – IA (Infrequently Accessed) For data that is accessed less frequently but requires rapid access when needed. This here costs lesser than S3 but you are charged for the retrieval of the data.

S3 – RRS (Reduced Redundancy Storage) Basically less durability with the same level of availability.

e.g. This about data you could potentially regenerate like a tax calculation or a payslip. This is cheaper than the original SS. Suppose you create thumbnails for all your pictures. If you lose a thumbnail you could always regenerate it.

When deciding which storage to use think about the various storage options, their advantages vs disadvantages. Are you optimizing for durability, the frequency of retrieval or availability?

Charging Model
Storage
Number of requests
Storage Management Pricing
Add metadata to see usage metrics.
Transfer Acceleration - Enables fast, easy and secure transfers of your files over long distances between your end users and an S3 bucket.

Transfer acceleration takes advantages of Amazon cloud front’s globally distributed edge locations. As the data arrives at an edge location, the data is routed to Amazon S3 over an optimized network path.

Think of transfer acceleration as a combination of S3 + CDN natively supported by this Service. Basically, every user ends up going through the closest possible edge location which in turn talks to the actual S3 bucket.

Recap - S3
S3 Storage Classes

S3 (Durable, immediately available and frequently accessed)
S3 – IA (durable, immediately available, infrequently accessed.
S3 Reduced Redundancy Storage (Used for data that is easily reproducible, such thumbnails)
Core fundamentals of S3 objects

Key: Name of the object These are store in alphabetic order
Value: The data itself Version ID: The version of the object
Meta Data: The various attributes of the data
Sub resources

ACL: Access control lists
Torrent: bit Torrent protocol
Cross region Replication

This basically means that if you have this turned on then for a bucket AWS will automatically make a bucket available across 2 or more regions.

Securing your S3 Buckets
By default, all buckets are private
You can set up access control to your using
Bucket Policies
Access control lists (ACL)
S3 buckets can be configured to create access logs
Encryption for S3
In-transit
SSL/TLS (using HTTPS)
At Rest
Server Side Encryption
S3 Managed keys – SSE-S3
Server side Encryption
Key Management Service – Managed Key
SST – KMS
Client Side Encryption



