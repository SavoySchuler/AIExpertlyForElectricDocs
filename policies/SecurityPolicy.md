# AIExpertly Information Security Policy

Version: v0.2 draft  
Status: Founder review draft

> This policy establishes baseline security expectations for AIExpertly systems, data, devices, credentials, vendors, source code, customer information, and AI assets.

## 1. Purpose

This policy protects customer trust, Company IP, AI assets, source code, data, credentials, financial systems, and business continuity. It is intended to scale toward enterprise readiness and SOC 2-style controls without overburdening the Company too early.

## 2. Security Principles

1. Protect customer trust.
2. Least privilege by default.
3. Strong identity controls.
4. Secrets must not live in personal notes, chat, or source code.
5. Access should be reviewed regularly.
6. Incidents should be documented and learned from.
7. Security controls should scale toward SOC 2 readiness.
8. Security ownership should be explicit.
9. Customer data should not be placed into unapproved AI tools.
10. Founder and contractor departures should trigger immediate access review.

## 3. Scope

This policy applies to founders, officers, employees, contractors, advisors, and any person with access to Company systems or data.

Covered assets include source code, production systems, cloud accounts, customer data, AI assets, API keys, model provider accounts, identity systems, business applications, financial systems, documents, devices, and backups.

## 4. Security Ownership

The CTO owns product and infrastructure security. The CIO owns internal IT security. The CEO owns overall business risk and customer commitments. The CAIO owns AI-specific safety and governance practices in coordination with the CTO.

Until a CIO is appointed, internal IT security is assigned by the CEO or covered by the CTO by default.

## 5. Identity and Access Management

The Company should use centralized identity management where practical. Access should follow least privilege. Shared accounts should be avoided. Administrative access should be limited, documented, and reviewed.

Access should be removed promptly upon departure or role change.

### Access Rules

- Grant access only for a legitimate business need.
- Use role-based groups where practical.
- Avoid standing admin access where temporary elevation is sufficient.
- Document owners for critical systems.
- Review access at least quarterly.

## 6. Multi-Factor Authentication

MFA should be required for email, source control, cloud infrastructure, model providers, financial systems, password managers, customer data systems, and administrative consoles.

## 7. Passwords and Secrets

Passwords, API keys, tokens, SSH keys, signing keys, and other secrets must be stored in approved secure systems. Secrets must not be committed to repositories, shared in unencrypted chat, stored in personal documents, reused across systems, or embedded in prompts sent to unapproved tools.

### Secret Rotation

Secrets should be rotated when a person with access departs, a secret may have been exposed, a vendor account changes ownership, a repository leak is detected, or required by customer or compliance obligation.

## 8. Source Code Security

Repositories containing Company code should use branch protection where appropriate, code review for production changes, dependency review, secret scanning, access controls, and documented release processes.

Production repositories should have clear owners and release procedures.

## 9. Device Security

Company devices or personal devices used for Company work should use full-disk encryption, screen lock, supported operating system, security updates, malware protection where appropriate, remote wipe where practical, and no unauthorized sharing.

## 10. Customer Data Protection

Customer data should be accessed only for legitimate business purposes. Customer data should not be copied into personal accounts, unmanaged AI tools, public prompts, or third-party services unless approved and contractually permitted.

Customer data exports should be minimized, tracked, and deleted when no longer needed.

## 11. AI Tooling Security

AI tools and model providers should be evaluated for data retention, training use, confidentiality, access controls, and security commitments. Sensitive customer data should not be submitted to AI tools unless approved under the AI Governance Policy.

Prompt injection, data leakage, unauthorized tool use, and model provider retention terms should be treated as security concerns, not only product concerns.

## 12. Cloud and Infrastructure Security

Cloud environments should use least privilege roles, separation of production and development where practical, logging, backup strategy, secure networking, encryption in transit, encryption at rest where practical, and change control for production systems.

## 13. Vendor Security

Material vendors should be reviewed for security posture, data processing terms, confidentiality, compliance certifications, breach notification obligations, subcontractor practices, business continuity, data retention, portability, and termination rights.

## 14. Incident Response

A security incident is any actual or suspected unauthorized access, data exposure, credential compromise, production compromise, material vulnerability, breach of customer data obligations, or AI-related security failure.

Incident response steps:

1. identify and classify incident;
2. assign owner;
3. contain risk;
4. preserve evidence;
5. assess affected systems and data;
6. notify CEO, CTO, CIO, and legal advisor as appropriate;
7. evaluate legal and customer notification obligations;
8. remediate;
9. document timeline and impact;
10. conduct post-incident review;
11. update policies or controls if needed.

## 15. Backups and Recovery

Material systems should have backup and recovery plans appropriate to business risk. Backups should be periodically tested. Recovery expectations should be documented for production systems, source code, financial records, governance records, customer data, and AI assets.

## 16. Access Reviews

At least quarterly, the Company should review access to source control, cloud accounts, production systems, customer data, financial tools, AI vendors, administrative systems, password managers, and collaboration systems.

Access reviews should document reviewer, date, systems reviewed, removals, and unresolved risks.

## 17. Departures

Upon departure, the Company should remove system access, recover devices, rotate shared secrets if needed, confirm return or deletion of Company data, preserve business records, remind the departing person of confidentiality obligations, remove bank, signing, cloud, source control, and AI vendor access, and update governance and contact records.

Founder departures require special review because founders may hold broad access across systems.

## 18. Security Evidence

To prepare for enterprise customers and SOC 2-style readiness, the Company should retain evidence of access reviews, incident reviews, vendor reviews, policy approvals, risk assessments, backup tests, security training, production change approvals, and customer data exceptions.

## 19. Security Roadmap

As AIExpertly grows, the Company should prepare for SOC 2-style controls, including formal access reviews, vendor risk management, incident management, change control, data retention, security training, endpoint management, logging, audit evidence, and business continuity.

## 20. Review Cadence

This policy should be reviewed at least annually and after any material security incident, major customer requirement, enterprise sales motion, or compliance milestone.
