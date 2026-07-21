# AIExpertly Open Source Policy

Version: v0.2 draft  
Status: Founder review draft

> This policy governs use, contribution, release, and approval of open-source software, models, datasets, prompt libraries, AI tooling, and Company-owned code.

## 1. Purpose

Open source can accelerate development, improve quality, and support recruiting and reputation. It can also create source disclosure obligations, licensing conflicts, patent risks, commercialization limits, model redistribution obligations, and customer diligence concerns.

This policy is intended to enable responsible open-source use while protecting Company IP and customer trust.

## 2. Scope

This policy applies to:

- source code;
- scripts;
- infrastructure templates;
- SDKs;
- prompt libraries;
- AI workflows;
- datasets;
- synthetic datasets;
- model weights;
- fine-tunes;
- evaluation suites;
- benchmarks;
- documentation;
- internal tools;
- customer-specific work product.

## 3. Default Rule

Using open-source software is permitted subject to license review and security review appropriate to the risk. Releasing Company-owned assets as open source requires approval under the Governance Matrix.

## 4. Permitted Ordinary Use

Engineers may use common permissively licensed open-source dependencies in ordinary development when the license and security posture are acceptable.

Examples of generally lower-risk licenses include permissive licenses such as MIT, BSD, and Apache-style licenses, subject to counsel review where material.

## 5. Restricted Licenses

Approval is required before using or distributing software, models, datasets, or tooling subject to terms that may:

- require disclosure of proprietary source code;
- require reciprocal licensing;
- impose field-of-use restrictions;
- prohibit commercial use;
- impose model redistribution obligations;
- impose data-sharing obligations;
- create patent-license or patent-retaliation concerns;
- restrict SaaS or network usage;
- create customer contract conflicts;
- impair acquisition or financing diligence.

## 6. AI-Specific Open Source Risks

AI assets require additional review when they involve:

- open model weights;
- training data restrictions;
- dataset provenance issues;
- unclear synthetic data rights;
- benchmark contamination;
- model licenses with use restrictions;
- evaluation datasets with redistribution limits;
- customer-data-derived artifacts;
- prompts or workflows that reveal proprietary methods.

## 7. Releasing Company Assets

The following require Protected Approval unless a narrower approval is adopted in writing:

- open-sourcing Company code;
- publishing proprietary prompt libraries;
- releasing proprietary datasets;
- releasing model weights;
- publishing internal AI tooling;
- releasing customer-derived examples;
- publishing security-sensitive implementation details;
- transferring core repositories to public visibility.

## 8. Contributions to External Projects

Founders, employees, and contractors may not contribute Company-owned code, documentation, prompts, workflows, datasets, or technical designs to external projects without approval.

Personal contributions unrelated to Company work are permitted if they do not use Company confidential information, Company time beyond approved limits, Company IP, customer data, or Company resources in a way that creates ownership or confidentiality issues.

## 9. Dependency Records

Material open-source dependencies should be tracked with:

- package or project name;
- version;
- license;
- source repository;
- owner;
- usage context;
- security review status;
- known obligations;
- replacement plan for critical dependencies.

## 10. Security Review

Open-source dependencies should be reviewed for:

- known vulnerabilities;
- maintenance status;
- source reputation;
- update cadence;
- transitive dependencies;
- integrity and supply-chain risk;
- production criticality.

## 11. Customer and Enterprise Diligence

The Company should maintain enough open-source records to respond to customer, investor, or acquirer diligence requests.

## 12. Violations

Unauthorized disclosure or release of Company-owned assets may constitute a breach of confidentiality, IP assignment obligations, security policy, or Bad Leaver provisions depending on circumstances.

## 13. Review Cadence

This policy should be reviewed annually and before major product launches, enterprise customer commitments, financing, acquisition discussions, or major AI architecture changes.
