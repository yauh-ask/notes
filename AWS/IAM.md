Identity Access Management (IAM)
Learn all about AWS IAM and what it entails. IAM is at the very center of AWS it is something that you absolutely need to understand as you build your applications on AWS.

IAM
Allows you to manage users and their levels of access to the AWS resources. Here are some key points to remember when thinking about AIM:-

IAM is universal, it is not specific to a region or AZ
Centralized control to the AWS account
Shared Access to your AWS account
Granular Permissions
Identity federation (like Active Directory)
MFA – Multifactor Authentication – 2 factor Auth
Temporary access for users
Allows you to set up your own password rotation policy
Integrates with many different AWS services supports PCI DSS compliance
In IAM there are 4 types of entities :-
Users – End-users
Groups – A collection of users under one set of permissions.

Roles, you can create roles and can then assign them to AWS resources

Policy is a document that defines one or more permissions.

You can apply policies to users, groups, and roles. Users, groups, and roles can all share the same policy documents.

“A root account” is the account created when one first sets up the AWS account. It has complete Admin Access.

New Users have no permissions when first created.
New Users are assigned access key and a secret access ID when & first created.
Access ID & Secret Access keys are used for access via the API and CLI.

Key Points to Note :-

An AIM Policy can be assigned to an User or a Group or a Role
An AIM is assumed by an User or an AWS Resource

