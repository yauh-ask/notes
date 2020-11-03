Direct and indirect dependencies

During development of a project, you will typically pull in a number of third-party components. This is often open-source libraries, 
that have implement some functionality that you desire.

When you use such a third-party component, it will be a dependency of your project, since you need to for your software to work.
This type of dependency is called a direct dependency, 
since your software requires it directly. In Java, an example of such a direct dependency could be that your project uses junit for testing purposes.

However, the third-party component you used might also, in itself, require other components to work. These are dependencies of the third-party component.
However, when you include the component in your software, you will automatically pull the component's dependencies as well!

These depencies of a dependency are caller indirect dependencies, or sometimes transitive dependencies.

Consider the example where junit was a direct dependency, such as in the following pom.xml file, which includes a <dependencies> section.

While it may look like junit is the only dependency, running mvn dependency:tree shows that hamcrest-core is now an indirect dependency of our project too, 
since it is a dependency of junit.

$ mvn dependency:tree
[...]
[INFO] --- maven-dependency-plugin:2.8:tree (default-cli) @ test ---
[INFO] com.debricked.training:test:jar:1.0
[INFO] \- junit:junit:jar:4.12:test
[INFO]    \- org.hamcrest:hamcrest-core:jar:1.3:test
Vulnerabilities

A vulnerability is an issue that can result in a successful attack against some system. Vulnerabilities can come in many forms, and can result in data theft, 
data manipulation, or service disruptions.

Vulnerabilities can be introduced into an application in several ways, due to coding errors in your own code, or by errors in your dependencies. 
In this course, we will focus on finding vulnerabilities in your dependencies, which may then affect the security of your own software.

To talk and reference about vulnerabilities, it is common to see references to the CVE-ID of a vulnerability. This is a unique numeric identifier 
for a particular vulnerability, and is assigned by an organisation called MITRE, and collected in the CVE list.

National Vulnerability Database (NVD) - https://nvd.nist.gov/

The National Vulnerability Database, or NVD, for short, is a U.S. Government funded database containing more than 140 000 vulnerabilities.

NVD collects new vulnerabilities from the CVE list. The CVE list contains, amongst other things, the CVE ID.

When a new vulnerability is made public, NVD then analyses the vulnerability, determines how serious it is, as well as augments it with other information. 
The vulnerability can then be searched for on the NVD website.

A vulnerability on NVD contains a lot of information. Here, we will describe the most important properties.

In this example, we will look at CVE-2019-11835 as an example.

CVE ID

The CVE ID is an identifier on the form CVE-2019-11835, where 2019 is the year the CVE ID was registered, while the last part is just a running number. 
This identifier is part of the CVE List from MITRE, and is used to uniquely identify a particular vulnerability.

CVSS score

The Common Vulnerability Scoring System, CVSS, is a method used to assess the severity of a particular vulnerability. 
A higher CVSS score means a more severe vulnerability. The maximum score is 10.0.

The CVSS score is calculated by taking into account several different factors, such as: the impact of an exploited vulnerability,
how easy exploitation is, if user interaction is required, and so on.
The exact scoring specification can be found at https://www.first.org/cvss/specification-document

CWE

While the CVE ID, described earlier, identificed a particular vulnerability, the CWE, or
Common Weakness Enumeration describes the category of the vulnerability.

A vulnerability is of a certain category, for example it can be a buffer overflow vulnerability or a cross-site scripting (XSS) attack. 
Each such category has its own CWE-ID, which can be used to find vulnerabilites of a certain kind.

In the example below, we see that this vulnerability is related to an out-of-bounds memory access.

CPE

CPE, or Common Platform Enumeration, is a way to describe which software the vulnerability applies to. CPE is a structured naming scheme,
following a specific pattern, and includes three important parts: the vendor, the product, and the version. These three together identifies 
the software in question. This means that we can search for a particular CPE, matching our software version, to see if it has known vulnerabilities.

In the example below, the vendor is cjson_project, the product is cjson, and the version ranges from 0.0.0 up to 1.3.2 (for the CPEs visible in the image).


Debricked is a Software Composition Analysis (SCA) tool with the following major features

Vulnerability scanning

Debricked scans for vulnerabilities in open source components used in your project. Vulnerabilities can be found in both direct and indirect dependencies.
Debricked supports most major languages and build tools.

License management

Debricked can show licenses used in open source components. This allows you to ensure that components with compatible licenses are chosen.




