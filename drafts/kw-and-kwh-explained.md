---
title: "kW and kWh: what the numbers on a charger actually mean"
description: "One is a rate, the other is a tank. A plain-English guide to charger speeds, battery sizes, charge curves and what each number means for your own charging."
date: "2026-11-10"
tags: ["UK-Cars", "EV", "Charging"]
author: "The TurningCircle Team"
layout: article.njk
ogType: article
topic: "Charging"
hero: "/assets/img/stock/chargehub"
heroCredit: "Pexels"
---

Two units dominate every electric car conversation, and they differ by a single letter. kW is power: the rate at which energy moves. kWh is energy: the amount that has moved. Confusing them is not a pedantic error. It is the reason people buy a car that cannot use the charger they just paid to install, or conclude that public charging is slow when the bottleneck was never the charger.

The distinction is the same as the one between the width of a tap and the size of the bucket underneath it. A charger is rated in kW because it describes flow. A battery is rated in kWh because it describes capacity. Everything else, from charge times to running costs, follows from those two facts.

## One is a rate, the other is a tank

A 60kWh battery holds 60 kilowatt-hours of energy. A 7kW charger delivers 7 kilowatt-hours every hour it is connected. Divide one by the other and you get the only charge-time calculation that matters: 60 divided by 7 is roughly 8.6 hours, so a full charge from empty takes a little over nine hours once charging losses are counted.

That arithmetic works at any scale. A 150kW rapid charger would theoretically fill the same battery in 24 minutes. It will not, for reasons covered below, but the units behave the same way: kWh divided by kW gives hours.

The unit is also how you compare running costs, because electricity is sold by the kWh. A 60kWh charge at the 8.6p per kWh typical of a dedicated overnight EV tariff costs about £5. The same 60kWh on the public rapid network, at the 77p weighted average, costs about £46. Same energy, same car, same miles. The multiplier is the price per unit, not the speed of the charger, which is why [the gap between home and public charging](/public-home-price-gap/) does more to your annual budget than any other decision you will make.

## What your car will actually accept

The number on the charger is a ceiling, not a promise. The rate you get is the lowest of four limits: what the charger can supply, what the car can accept, what the cable can carry, and what the battery will tolerate at that moment.

On alternating current, the hard limit is usually the car. Most homes have a single-phase supply, which caps AC charging at 7.4kW; 11kW and 22kW AC charging needs three-phase power that the overwhelming majority of UK houses do not have. A car with an 11kW onboard charger will still only take about 7kW from a single-phase wallbox. This is the point at which buyers most often overpay, and we cover the domestic version of the question in [whether you actually need a 7kW wallbox](/do-you-need-a-7kw-wallbox/).

On direct current, the limit is usually the car's peak acceptance. A 150kW charger connected to a car that peaks at 100kW will deliver 100kW. A 350kW charger offers nothing extra to a car built on a 400-volt architecture, because the pack cannot take the current. Ultra-rapid hardware is only worth seeking out if the car was designed for it.

Cables matter too, and they are the least glamorous constraint. A three-phase cable used on a single-phase supply, or a cable rated below the charger's output, becomes the bottleneck. The cable that comes with the car is generally matched to it, but aftermarket cables bought on price are a common cause of disappointing charge rates.

## Reading a charge curve

Battery charging is not linear, and the "10 to 80% in 18 minutes" claims in brochures describe a specific window under specific conditions. Peak power is typically available only between roughly 10% and 55% state of charge. Below 10% the pack is protecting itself. Above about 80% it tapers sharply, because the last fifth of a lithium-ion battery takes disproportionately long and generates disproportionate heat.

That taper is why the 80% rule exists in public charging, and why [rapid charging etiquette](/rapid-charging-etiquette/) treats a car left on a rapid past 80% as an obstruction rather than a customer. On a long journey, two shorter stops that stay in the fast window beat one long stop that pushes to 100%.

Temperature is the other half of the curve. A cold pack accepts less, which is why cars with route planning preheat the battery before arriving at a rapid. A car at 5°C on a January morning may take twice as long to accept the same energy as the same car in July, and no amount of charger rating changes that. We covered the seasonal version in [winter EV range myths](/winter-ev-range-myths/).

## What the numbers mean at the plug

Translated into miles, the figures stop being abstract. An average electric car returns somewhere between 3.5 and 4 miles per kWh in mixed driving.

- A 2.3kW three-pin socket adds roughly 8 to 10 miles of range an hour.
- A 7kW wallbox adds roughly 25 to 30 miles an hour.
- A 50kW rapid adds around 150 to 180 miles an hour in its peak window, then less.
- A 150kW charger on a compatible car roughly triples that, if the battery is warm, low and willing.

The miles-per-hour framing is more useful than charge times, because most charging is not from empty. The average UK car covers about 19 miles a day, so even the slowest option covers a typical week of commuting in a couple of nights. What the faster chargers buy is recovery from the exceptions: the unplanned long day, the forgotten plug, the early start. That is the honest case for a wallbox, and it is a case about time rather than energy.

## Where the units mislead buyers

Three traps recur. The first is treating a charger's rating as the speed you will experience, when the car, the cable, the temperature and the state of charge all sit in between. The second is comparing batteries by capacity alone, when usable capacity is smaller than the headline figure and efficiency varies by 30% or more between a small hatchback and a large SUV. A 77kWh SUV may go no further than a 60kWh saloon.

The third is the assumption that a bigger battery is always better. It adds weight, cost and charging time, and for a driver who charges at home overnight it buys range they will rarely use. The right question is not "how many kWh" but "how many miles do I need between charges, and how fast can this car replace them on the days I need to".

## The short version

kW is how fast energy arrives. kWh is how much energy there is, and what you pay for. Multiply the price per kWh by the size of the charge to get the cost; divide the size of the charge by the rate to get the time. Every other number in electric car marketing is a variation on those two, usually measured under conditions you will not reproduce on a wet Tuesday in November.

## Sources

- [Energy Saving Trust: Charging electric vehicles](https://energysavingtrust.org.uk/advice/charging-electric-vehicles/)
- [Zapmap: Public charging price index](https://www.zapmap.com/ev-stats/charging-price-index)
- [Ofgem: Energy price cap](https://www.ofgem.gov.uk/information-consumers/energy-advice-households/energy-price-cap)
- [RAC Foundation: General facts and figures about roads and road use](https://www.racfoundation.org/motoring-faqs/mobility)
- [GOV.UK: Electric vehicle chargepoint grant for renters or flat owners](https://www.gov.uk/electric-vehicle-chargepoint-grant-household)
