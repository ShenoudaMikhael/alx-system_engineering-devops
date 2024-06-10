## **Postmortem Report: Clinic Web App Outage on 24/03/2023**

### **Issue Summary**

**Duration of the Outage:**



* Start Time: 24/03/2023, 08:00 AM UTC
* End Time: 24/03/2023, 02:00 PM UTC

**Impact:**



* The Clinic Web App experienced a complete outage, affecting all functionalities reliant on external online resources. Users were unable to access the app, resulting in a 100% service disruption.
* Approximately 100% of our users were affected, experiencing complete inaccessibility of the web app.

**Root Cause:**



* The outage was caused by a DNS issue with our internet service provider (ISP), rendering external online resources inaccessible.


### **Timeline**



* **08:00 AM UTC** - Issue detected: Monitoring alerts indicated a failure in accessing external resources.
* **08:10 AM UTC** - Initial investigation by on-call engineer; confirmed the issue was with accessing external online resources.
* **08:30 AM UTC** - Assumed root cause: Potential server-side issue; engineers checked server configurations and logs.
* **09:00 AM UTC** - Misleading path: Investigated possible application bugs or recent code changes; no issues found.
* **09:30 AM UTC** - Incident escalated to Network Operations team to check network and DNS configurations.
* **10:00 AM UTC** - Root cause identified: DNS issue with the ISP was confirmed as the cause of the outage.
* **10:15 AM UTC** - Decision made to switch all resources to be hosted internally.
* **12:00 PM UTC** - Configuration changes initiated to host all resources on our servers.
* **01:45 PM UTC** - Changes deployed and tested.
* **02:00 PM UTC** - Service fully restored and confirmed operational.


### **Root Cause and Resolution**

**Detailed Explanation of Root Cause:**



* The outage was due to a DNS failure with our ISP, which made it impossible for our web app to access critical external online resources. The DNS issue prevented the resolution of domain names, thereby blocking access to necessary assets and services hosted externally.

**Detailed Explanation of Resolution:**



* To resolve the issue, we reconfigured the Clinic Web App to host all previously external resources on our own servers. This involved:
    * Downloading all required external assets.
    * Updating the web app’s configuration to point to the locally hosted resources.
    * Testing the changes to ensure all functionalities were restored.
* These steps ensured that the app no longer relied on the problematic external DNS and ISP for its resources.


### **Corrective and Preventative Measures**

**Improvements and Fixes:**



* Implementing redundancy for critical external resources to avoid single points of failure.
* Enhancing monitoring to detect and alert on DNS issues specifically.
* Establishing a quicker incident response protocol for similar issues in the future.

**Tasks to Address the Issue:**



* **Task 1:** Configure a backup DNS provider to switch to in case of primary DNS failures.
* **Task 2:** Implement internal hosting for all critical resources, with regular sync updates.
* **Task 3:** Enhance monitoring tools to include DNS resolution checks.
* **Task 4:** Document and train the engineering team on the new incident response protocols.
* **Task 5:** Review and update SLAs with our ISP to ensure better reliability and quicker issue resolution.

By implementing these corrective and preventative measures, we aim to mitigate the risk of similar incidents in the future, ensuring better reliability and availability of our services.
