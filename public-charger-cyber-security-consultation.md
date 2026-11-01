---
title: "Public chargers would have to pass a cyber security standard under new plans"
description: "Public EV charge points sold in Great Britain would have to meet ETSI 303 645, with anti-tamper cases and Class B meters. The consultation closes on 20 December."
date: "2026-11-01"
tags: ["UK-Cars", "EV", "Charging"]
author: "The TurningCircle Team"
layout: article.njk
ogType: article
topic: "Charging"
hero: "/assets/img/stock/chargehub"
heroCredit: "Pexels"
---

Public electric car chargers in Great Britain have never had to clear a cyber security standard. The Department for Transport opened a consultation on 29 October that would change that, and the proposal reaches every charge point sold or installed in Britain rather than only the largest networks.

## Four proposals in one consultation

The core measure requires public charge points sold or installed in GB to be manufactured and configured to [ETSI 303 645](https://www.gov.uk/government/consultations/public-electric-vehicle-charge-points-cyber-security/cyber-security-for-public-electric-vehicle-charge-points), the baseline standard for internet-connected devices that covers authentication, secure updates and vulnerability fixes. Home smart chargers already have to meet it.

A second proposal would treat [EN 18031](https://www.gov.uk/government/consultations/public-electric-vehicle-charge-points-cyber-security/cyber-security-for-public-electric-vehicle-charge-points) as an equivalent route to compliance. That is the standard used to meet the EU's Radio Equipment Directive, and the government's stated reason for allowing it is to avoid a position where a manufacturer builds one device for Europe and another for Britain.

The remaining two proposals are physical. Public charge points would need anti-tamper protection built into the casing, and would need an active electricity meter that complies with the Measuring Instruments Regulations 2016.

The duty would land on anyone selling or installing a public charge point in GB, which means manufacturers, importers and distributors rather than the operators who run the sites.

## What is not in the current rules

Domestic and small non-domestic charge points, meaning the ones in driveways and small depots, have had cyber requirements since the [Electric Vehicles (Smart Charge Points) Regulations 2021](https://www.legislation.gov.uk/ukdsi/2021/9780348228434). Public charge points were left out.

The one route that catches public infrastructure is the [Network and Information Systems Regulations 2018](https://www.legislation.gov.uk/uksi/2018/506), and its reach is narrow. A charging organisation comes into scope only when it controls 300 megawatts or more of electrical load across its network in aggregate, and that change is itself waiting on the Cyber Security and Resilience Bill passing through Parliament.

The consultation says plainly that most organisations will not initially fall within that threshold. A large share of the public network therefore sits outside any cyber requirement today, and the government notes that many devices carry some protection only because their makers need to satisfy rules in other markets.

## The two risks named in the paper

The consultation splits the threat into direct attacks on charge points, and cases where a charger is manipulated or misused to compromise other parts of the charging network. The second category is the reason the scope extends beyond a single unit.

Its summary of why this matters is short. Cyber security will be important in "maintaining the integrity of, and confidence in, our charging network", and attacks "could potentially disrupt and negatively impact drivers, businesses and national infrastructure".

That framing puts charge points in the same category as other networked infrastructure rather than treating them as payment terminals with a cable attached. A second phase of work could place requirements on charge point operators and on e-mobility service providers, the companies that handle roaming and app payments, to follow a cyber security framework.

## Anti-tamper cases and honest meters

The physical measures in the consultation follow the template already used for domestic chargers. Public units would have to resist physical damage, carry a seal or sticker that breaks on any attempt to reach non-serviceable components, and include a sensor that detects a breach of the casing. Where a breach is detected, the device would have to notify the owner.

The metering proposal deals with a different kind of loss. Public charge points used for trade already fall under the Measuring Instruments Regulations, and the change would push the requirement back up the supply chain so that a compliant meter is fitted at the factory. Class B under those regulations means a meter verified to measure energy to within 2% accuracy.

Meter accuracy is a live subject on the public network. [Our tracker of public charging prices](/public-charging-price-tracker/) has been built from advertised per kWh rates, and a rate is only worth comparing if the meter behind it counts the same way across operators.

## The size of the estate this would cover

Zapmap counted [124,738 public EV chargers](https://www.zapmap.com/ev-stats/ev-charging-statistics) at the end of September 2026, spread across 97,976 devices and 48,298 locations. The network added 1,061 chargers net during September.

None of those existing units would need to change. The consultation says the requirements would apply to charge points sold and installed after the rules take effect, with no retrofit, and a device would be swapped for a compliant one when it reaches the end of its working life. The consultation is also asking operators how long a charge point typically lasts between installation and replacement, which suggests the government does not yet have a firm figure for how quickly the estate would turn over.

The scale of that estate has grown steadily rather than in bursts. By 1 July this year the DfT counted 121,171 public chargers, a figure we covered in [our summer snapshot of the network](/uk-charging-network-state/).

## What happens next

The consultation closes at 11:59pm on 20 December 2026. Responses will shape which option is chosen, the implementation timeline, and how compliance is policed. The consultation floats two enforcement models: self-assessment using the ETSI test specification 103 701 with spot checks by a regulator, or third-party certification through an accredited testing house.

Work on the surrounding standards is already running in parallel. The EU's Cyber Resilience Act comes into force at the end of 2027, which is one reason the EN 18031 option is on the table. The Department for Business and Trade intends to amend the measuring instruments rules to allow a remote display for meters in charge points by the end of 2027.

Separately, the DfT and the Department for Energy Security and Net Zero plan a further consultation on requiring charge points to support ISO 15118-20, the communication standard behind [plug and charge](/plug-and-charge-uk/). That would put the payment handshake on the same regulatory footing as the device security in this paper.

## What it means for a driver

Nothing changes at the charger you use this weekend. The proposals cover new equipment only, and no date has been set for them to come into force.

The practical effect, if the plans go through, is that a charger installed from some point in the next few years would arrive with a security baseline, a tamper-evident case and a meter built to a legal accuracy standard. The gap the consultation identifies is not that every charger is vulnerable. It is that nothing in British law currently requires one to be secure, and the operators small enough to sit below the 300 megawatt threshold have no cyber obligation at all.

For a network of this size, built quickly and spread across a long list of operators, that is the argument the government is making. Whether the answer is a product standard, a duty on operators, or both is what the next seven weeks of responses will decide.

## Sources

- [GOV.UK: Cyber security for public electric vehicle charge points, consultation (29 October 2026)](https://www.gov.uk/government/consultations/public-electric-vehicle-charge-points-cyber-security/cyber-security-for-public-electric-vehicle-charge-points)
- [GOV.UK: Public electric vehicle charge points, cyber security, consultation page (29 October 2026)](https://www.gov.uk/government/consultations/public-electric-vehicle-charge-points-cyber-security)
- [Zapmap: UK EV charging statistics, end of September 2026 (updated 6 October 2026)](https://www.zapmap.com/ev-stats/ev-charging-statistics)
- [GOV.UK: Public electric vehicle charging infrastructure statistics, 1 July 2026 (published 27 August 2026)](https://www.gov.uk/government/statistics/electric-vehicle-charging-infrastructure-statistics-1-july-2026/public-electric-vehicle-charging-infrastructure-statistics-1-july-2026)
- [Legislation.gov.uk: Electric Vehicles (Smart Charge Points) Regulations 2021](https://www.legislation.gov.uk/ukdsi/2021/9780348228434)
- [Legislation.gov.uk: Network and Information Systems Regulations 2018](https://www.legislation.gov.uk/uksi/2018/506)
- [Fleet News: Consultation on cyber security for EV charge points launched (30 October 2026)](https://www.fleetnews.co.uk/news/electric-vehicle-charge-point-cyber-security-risks-identified-by-dft)
