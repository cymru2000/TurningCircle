---
title: "The Fiddly Bit of Public Charging Is Quietly Disappearing"
description: "Osprey has made its network the biggest in the UK where you plug in and walk away. We explain Autocharge, Plug & Charge, and what either means for you."
date: "2026-09-12"
tags: ["UK-Cars", "EV", "Guides"]
author: "The TurningCircle Team"
layout: article.njk
ogType: article
topic: "Charging"
hero: "/assets/img/stock/chargehub"
heroCredit: "Pexels"
---

Public charging in Britain has a reputation problem that has nothing to do with how many chargers exist. The complaints are about the small stuff: the app that wants an account before it wants your car, the RFID card in the wrong jacket, the tap that fails in the rain, the price you only discover once the session is running. On 7 September, Osprey Charging launched a feature aimed squarely at the first two of those, and it is worth understanding where it fits in a market that is quietly standardising itself.

[Osprey Go lets drivers plug in and walk away](https://www.ospreycharging.co.uk/post/osprey-becomes-largest-uk-charging-network-to-offer-autocharge-via-osprey-go). Charging starts automatically, and the best price Osprey offers at that location and that moment is applied without a card tap or an app launch. It is set up once in the Osprey app, and the car is registered after two sessions started through that app, after which the charger recognises it on every visit. Osprey says the launch makes it the largest UK charging network to offer Autocharge, and it sits on top of dynamic pricing that the company is extending across its network during September, so charging outside peak periods costs less for the same speed of charge. Olly Cooper, Osprey's chief technology officer, described it as taking Autocharge and "building a simple set-up flow, testing it thoroughly, and offering the functionality to the widest range of drivers".

## Autocharge and Plug & Charge are not the same thing

The two names get used as if they were interchangeable. They produce the same experience, since in both cases the only thing the driver does is plug the cable in, but the machinery underneath could hardly be more different.

Autocharge, the route Osprey has taken, works on the charging equipment's side. When a car connects, the charger reads a unique identifier from the vehicle, such as the identifier of the charging controller, and the network's back office matches it against the one stored during setup. If it matches, the session starts and lands on your account. [The approach works with the connector almost every modern electric car uses](https://i-charging.tech/the-differences-between-plug-charge-and-autocharge), and it needs no extra hardware in the car. Its limits are that it is proprietary to each network, so the setup you do with one operator means nothing to another, and that an identifier can in principle be cloned.

Plug & Charge is the standardised version, defined by ISO 15118, the international standard for communication between a car and a charge point. Instead of a network storing an identifier, the car carries a digital contract certificate and exchanges it over the charging cable using powerline communication. Authentication is cryptographic, which makes it harder to spoof, and certificates issued through a shared trust infrastructure mean a compatible car can use any network that supports the standard without setting anything up network by network. For it to work, the car, the charger and the operator's software all have to support it, which is why adoption has been uneven. Osprey has confirmed it is exploring Plug & Charge for a future release.

## The law already removed one layer of friction

The days when a network could insist you download its app and create an account before it would sell you electricity are gone, and they ended for a simple reason. The [Public Charge Point Regulations 2023](https://legislation.gov.uk/uksi/2023/1168/made), which came into force in November 2023, require contactless payment at every new public charge point rated 8kW or above, and at every existing public charge point rated 50kW or above, within a year of the rules taking effect. Payment must be possible without a pre-existing contract with the operator, so a bank card, Apple Pay or Google Pay has to work. The same regulations require the price per kilowatt hour to be visible before you start and a staffed helpline to be reachable around the clock.

That rule fixed access. What it did not fix is the tap itself, and a contactless terminal is still a terminal. Autocharge and Plug & Charge exist for the step after that, where the transaction happens because the car and the charger recognise each other rather than because a driver remembered a card. It is a small difference until you are standing at a rainy motorway services at ten at night.

## What Tesla proved, and what the rest of the market is catching up on

The benchmark here is not British. Tesla built its Supercharger network around the assumption that the car and the charger already know one another: the company's own instructions for its UK network open with the words "simply plug in and charge automatically". Tesla has since opened many of its UK sites to other brands, initially through the Tesla app, and it has been [cutting the price premium non-Tesla drivers used to pay](https://www.zapmap.com/news/tesla-opens-more-its-supercharger-sites-non-tesla-drivers). Some of its newer V4 posts carry card readers, so drivers without a Tesla account can still [pay at the post](https://www.tesla.com/en_gb/support/charging/supercharging-other-evs).

The rest of the network has had to work backwards to that experience, and Osprey's launch is the clearest signal yet that the direction is settable. Autocharge is an interim route rather than the destination that Plug & Charge represents, and an operator with hundreds of its own chargers can offer it without waiting for every manufacturer to ship ISO 15118 support in every model.

## The backdrop makes the friction matter more

This is happening on a network of [123,677 public chargers](https://zapmap.com/ev-stats/ev-charging-statistics), with 29,534 of them rated 50kW or above and Zapmap logging 7,634 additions so far in 2026. Four years ago, the harder problem was finding a charger at all. Today most drivers on most routes can find one, and the remaining cost is time: the minutes lost to a failed app login, a card that will not read, or a queue for a single working post. Removing a click from a session that happens twice a week is a modest convenience. Removing it from the one session that matters, in the rain, on a schedule, is not.

## What to do with this now

If you use one network often, switch Autocharge on and then verify it once, because a feature you have enabled but never tested is only a plan. If your car supports Plug & Charge and you charge at a network that offers it, the same logic applies with more upside, since it should follow you across compatible networks. Either way, keep a physical card in the car. The regulations mean contactless has to be available at rapid chargers, so you should never be stranded behind an app, and the [unwritten rules of charger etiquette](/rapid-charging-etiquette/) still apply whether the session starts by itself or not.

Dynamic pricing is the other half of the Osprey announcement, and arguably the more valuable one. Being charged the best available price automatically means the saving from charging off peak no longer depends on remembering which network's discount window applies where. With rapid charging averaging far more per kilowatt hour than charging at home, the [gap between public prices](/charging-prices-per-kwh/) is the number that changes what a mile costs, and the monthly movement in those prices is something we track in [our price tracker](/public-charging-price-tracker/).

The direction of travel on the network runs from charging as a small project you complete with your phone toward charging as something that simply happens when you park. Apps and cards will stay, since the regulations guarantee them and plenty of drivers prefer them. They are becoming an option rather than a toll gate, and that is progress worth noticing.

## Sources

- [Osprey Charging: Osprey Go, Autocharge launch](https://www.ospreycharging.co.uk/post/osprey-becomes-largest-uk-charging-network-to-offer-autocharge-via-osprey-go)
- [i-charging: The differences between Plug & Charge and Autocharge](https://i-charging.tech/the-differences-between-plug-charge-and-autocharge)
- [The Public Charge Point Regulations 2023](https://legislation.gov.uk/uksi/2023/1168/made)
- [Zapmap: EV charging statistics](https://zapmap.com/ev-stats/ev-charging-statistics)
- [Zapmap: Tesla opens more of its Supercharger sites to non-Tesla drivers](https://www.zapmap.com/news/tesla-opens-more-its-supercharger-sites-non-tesla-drivers)
- [Tesla UK: Supercharging other EVs](https://www.tesla.com/en_gb/support/charging/supercharging-other-evs)
