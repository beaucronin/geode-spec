# Geode Whitepaper

This whitepaper describes the motivation behind the $GEODE token, the contracts by which it operates, and some possible use cases that illustrate how the token would support the creation and ongoing growth of planetary scale data collection, aggregation, and applications.

# Motivation
The network has grown to the point where interpersonal connectivity is increasingly ageogrpahic, or alternatively where existing geogrpahy is but one factor that determines how mental collectives can be formed and shared decisions made.

At the same time, the inadequacies of the nation state as a regulating and political body have become very clear as the climate crisis has emerged. Actions in one bioregion can have huge effects on a global basis; the behavior of a political group that has high legitimacy within its own territory can present an existential threat to groups who have no representation in that polity.

As the climate crisis has grown, we should ask why, from an organismal or systems sense, such an obviously-awful situation could progress to this point. If it's so bad, then why has it gotten so far? From the point of view of individuals and their local groups, then the answer is clear: following local incentives can lead to global ruin, with the consequences far away in time and space and responsibility diffuse. It has gotten so bad because the benefits have been clear and near to hand, and the negative outcomes cognitively dissonant.

But we should take another perspective. We want our civilization, as a higher-order entity, to survive and thrive. So we must view the situation from its own level of analysis. Healthy systems have prompt, high-quality feedback; consequences of actions are evident in sufficient detail that causal attribution is possible. All organisms have a version of this act-sense-respond loop, from single-celled bacteria up to high-order animals like ourselves.

Whether or not our civilization is an organism, or the extent to which that mapping holds true, it is self-evident that no complex system can survive and thrive without a sensory system - and, in particular, a sense of pain.

# The Geodess Platform

The Geode token is the unit of account for the Geodess platform, which comprises the services that accept new observations from Geode account holders, aggregates and processes these observations, and then serves the resulting data products buyers. At the most basic level, contributors to the platform receive $GEODE tokens in return for their efforts. Data buyers can purchase $GEODE with $ETH, an exchange that allows contributors to convert their $GEODE into an easily tradeable form - including sale for traditional currency.

The design and specific functionality of the Geodess platform are beyond the scope of this whitepaper. But it is important to note that the $GEODE token is specifically designed to support the needs of that platform, and specifically to encode the market incentives that will result in complete, high-quality datasets whose sales revenue can be disbursed pro rata to all of the relevant contributors.

# Basic System Concepts

## Key components
A civilization-scale sensory system requires three elements to exist in order to be called into existence. First, a specific value proposition or use case that can provide an organizing force in shaping and drawing out its development. Second, an economically viable means to collect many observations, broadly distributed in space and consistently over time. And finally, a software platform that can integrate a large number of observations into a queryable data set, and that supports the querying, pricing, and distribution of resulting data products.

This document assumes that the use case is established, and it is also true that the software platform can be built out using commodity cloud services. This paper focuses on the second requirement - namely, the cost-effective collection of many observations of the physical world. While there are a number of technical challenges, the most prominent unsolved problem is that of incentivizing and orchestrating the distributed action pattern of collecting and submitting these observations.

In the absence of a centralized need and the capital required to conjure the collection program via hierarchical command and control, an economy based on a market that connects buyers of data and those who collected it is the most powerful means available.

## Prior art: Organizations for whole-earth observation
Global sensing, i.e. the ability to observe one or more aspects of the planet in totality at a given spatial and temporal resolution, was until recently impossible. For example, Landsat is the first and longest-running whole-Earth imaging program, beginning in 1972. In its current iteration, its spatial resolution is in the tens of meters per pixel, and the revisit time for each locationis approximately 16 days. The Landsat program, operated by a wealthy nation state using tax revenue, has cost many billions of dollars over its decades of existence. Given this funding source, it is reasonable that its imaging results are distributed as a free public good - one that is available globally, including to individuals and institutions that did not participate in its funding.

A more recent reference point is the ground-level imaging captured by Google Street View. This program, whose costs to develop are not publicly disclosed, certainly requires billions of dollars in investment, with substantial ongoing operating expenses as the imagery is periodically refreshed. In basic terms, Street View data collection requires driving a specially-equipped vehicle down every public road in the world, and then processing, storing, and serving that data on the whim of millions of users. There are two aspects of note. First, that it is possible for any private entity, even one of the best-resourced in the world, to embark on and succeed at a project of this scale and ambition is itself a reflection of the massive cost deflation that is enabled by the emergence of inexpensive, high-quality sensors linked by ubiquitous mobile data networks, as well as the entire suite of modern technology abundance: massive storage, abundant computing power, high-throughput datacenter networks. Perhaps more significant in our context is that the outputs of this massive and expensive undertaking are offered to Google's users *for free*, as one part of a consumer experience that generates an audience for the most powerful advertising machine ever created.

Both Landsat and Street View are centralized efforts, one governmental and one operated by a private entity. Both of these entity types have structural flaws, though, if the goal is to develop open, high quality, whole-earth scale observational data along many dimensions. Governments are extremely conservative in developing additional efforts of this nature, and the process by which new programs are approved and executed is disconnected from consumer and business needs. The shortcomings of corporate efforts are even easier to identify: private companies do not make large investments in order to release the results as public goods. In those cases when data is released for public use, it is often significantly reduced in resolution and completeness. And the corporate initiatives by which data is publicly released can be cancelled or modified at any time, without recourse.

High quality global data resources cannot be left to the public or private sector. An alternative approach has recently emerged: collaborative, crowd-sourced collection efforts that are orchestrated and operated by volunteers and/or nonprofit organizations. Examples include:

* [Purple Air](https://www2.purpleair.com/) is a network of air quality sensors that in many locations provides the most timely and useful measurements of particulate air pollution. The network is managed by a small company, and the data is generated by a collection of privately-owned sensors that were designed by the company and sold at low cost. The utility of the network in any one locale depends on the proximity of the nearest sensors, and in many cases their density: air quality can vary significantly over distances of only a few miles in areas with significant terrain and complex wind patterns. Some regions have very good coverage on Purple Air, but many do not. Sensor placement is up to the vagaries of community members, and there is no effort to incentivize sensor placement in under-instrumented areas; conversely, some regions have many more sensors than needed - the air quality is oversampled in spatial terms.
  
* [ADS-B Exchange](https://www.adsbexchange.com/) is a site and community that aggregates aircraft flight tracking data. It leverages the fact that private and commercial aircraft, with few exceptions, are required to transmit their identity and location for flight control purposes. These transmissions are broadcast "in the clear" using an open standard that can be received and decoded by enthusiasts with inexpensive equipment. Independent observers submit their decoded observations to the ADS-B Exchange, and the aggregated results are then made available - free to enthusiasts, and for a fee to organizations.
  
* The [Safecast](https://safecast.org/) project was born "after the devastating earthquake and tsunami which struck eastern Japan on March 11, 2011, and the subsequent meltdown of the Fukushima Daiichi Nuclear Power Plant, [when] accurate and trustworthy radiation information was publicly unavailable." It has since grown well beyond its geographic origin, and is currently the largest collection of radiation measurements available to the public.

These networks share some notable properties. First, their ongoing data collection depends on enthusiasts who are invested in the topic (airplane tracking hobbyists), those who have a specific personal stake (such as those subject to air pollution or radiation), or an emerging class of self-identified "citizen scientists" who are drawn to the idea of contributing to a larger knowledge-gathering effort. Notably, all of these motivations are difficult to scale, and subject to the whims and locations of the community members. In particular, these projects mostly lack mechanisms for incentivizing data collection in a granular, targeted way.

Second, these networks rely on the distribution of specialized sensor hardware. In each case, this equipment is inexpensive and realtively easy to obtain; nevertheless, it is not broadly distributed and its acquisition constitutes a significant barrier to entry for new contributors.

Finally, we note one aspect of these networks that is beyond the scope of this document but integral to the larger Geodess project: these projects, in addition to their community and technical aspects, can all be analyzed in terms of their capabilities for sousveillance. That is, each of them can play a role in holding central authorities, whether governmental or corporate, to account.

The Geodess platform uses an economy based on the $GEODE token to implement a new category of whole-earth observation effort. The goal of this platform is to capture the strengths of previous models while avoiding their failure modes.

## Coordination
The need is there. The technological enablers are there - cheap, networked sensors and abundant cloud resources. The question is how to coordinate the activity. How to incentivize individual actions? How to signal differential value? How to aggregate demand and disaggregate rewards?

# Address Creation

There are three types of accounts on the $GEODE blockchain.

* A **platform account** is used to operate the system. These accounts are the only ones that can authorize the minting of $GEODE tokens. Platform accounts are created when the blockchain is initialized. if needed, additional such accounts can be instantiated by action of a master account that has sole access to the relevant contract.
* A **contributor account** is used by platform contributors to receive tokens in payment for performing actions deemed valuable by the platform. Contributor accounts can be created largely at will through a standard process that is open to the public. Account creation may require a small payment in order to discourage mass account creation. The platform uses a transparent algorithm 
* A **buyer account** is created and used by individuals and organizations that wish to buy data and data products from the Geodess platform. Like contributor accounts, buyer accounts are easy to create.

## Addresses and individuals

As in many cryptological identity systems, accounts in Geode are pseudonymous. It is possible for a single individual to have multiple accounts, and this is not inherently a bad thing. There is no attempt to associate an account with a particular person or legal entity.

The basic principle is that each account is responsible for its own behavior on the platform. The exception to this is when accounts - whether controlled by a single entity or not - conspire to defraud the platform and its users, or otherwise act in bad faith. These activities will be dealt with on-chain mechanisms when possible, and with administrative action in cases where those efforts are unsuccessful.

As in all cryptotoken systems, the private key associated with an account must be guarded by its owner. Losing custody of the key is not recoverable, and the account owner will need to create a new account in order to continue transacting on the platform.

## Reputation

Contributor and buyer accounts are cheap and easy to create, but they start off with no track record. As accounts transact with the Geodess platform, they are associated with feedback that can indicate trustworthiness on the one hand, or incompetence or failure to act in good faith on the other. These feedback mechanisms are designed to obey the following principles:

* Effort should be made to summarize feedback into the simplest rating system possible that remains fair to the account being rated while providing solid guidance to the other users of the system.
* Longitudinal patterns of behavior are more important than occasional missteps
* Feedback should be made publicly available in someting close to raw form, so that interested parties can perform their own assessments of an account's behavior

# Token Minting

The mechanisms by which $GEODE tokens are minted, traded, and burned are integral to the functioning of the Geodess platform as a whole.

## Initial token creation

## Ongoing token creation

$GEODE tokens are minted whenever work is performed by a platform contributor, and possibly validated by other contributors as well. The newly-created tokens are immediately transferred to the given contributors address, after which they can be handled according to the contributor's manual or automated instructions.

The number of tokens that are created and paid is determined by the platform, rather than being strictly determined by the relevant contracts. Instead, the contract mints and pays out the amount requested 

## Token burning

# Trading $GEODE

$GEODE trading enacts the purchase of Geodess data:

* **Buying** $GEODE with $ETH is how purchasers pay the platform for data
* **Selling** $GEODE for $ETH is how observers and other value creators transform their labor into a widely-accepted means of exchange.

# $GEODE Transactions

Many common interactions on the Geodess platform are backed by smart contract transactions on the $GEODE blockchain. 

## Accounts

### Create


### Suspend

* Inputs
  * Account Id
* Outputs
  * Status Code

### Transfer

* Inputs
  * Recipient Account Id
  * Amount
* Outputs
  * Status Code

## Observations

### Submit

* Inputs
  * Metadata Summary
  * Hash
* Outputs
  * Status Code

### Evaluate

* Inputs

### Challenge

## Query 

# Roadmap
