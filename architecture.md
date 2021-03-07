# Geodess Platform Architecture

The Geodess platform comprises the following components:

* A **blockchain** with smart contracts that provides the shared ledger of identities, observations, corroboration, disputes, and token transfers. This blockchain is executed via and secured by full-node software that can be run by any platform participant.
* A **distributed database** that stores the observations themselves, along with other supporting data such as account profiles. This data is "off-chain", but it is stored via ipfs - an immutable store - which ensures that the information that is identified by a hash has not been altered since it was written.
* A **backend service** that exposes endpoints for use by clients, and communicates with the blockchain and database as needed. This service is, to the greatest extent possible, state-free; its only role is to facilitate the interactions between users of the system and the secure state contained in the two previous components.
* **Client libraries** that can either be used directly or incorporated into other applications for easy programmatic access to the platform.



```
                        ┌───────────────────────────┐
                        │                           │
                        │          Client           │
                        │                           │
                        └────────┬─────────▲────────┘
                                 │         │
                                 │  HTTP   │
                                 │         │
                        ┌────────▼─────────┴────────┐
                        │                           │
                        │          Server           │
                        │                           │
                        └───┬────▲─────────┬────▲───┘
                            │    │         │    │
                        ┌───▼────┴───┐ ┌───▼────┴───┐
                        │            │ │            │
                        │ Blockchain │ │  Database  │
                        │            │ │            │
                        └────────────┘ └────────────┘
```



## Blockchain
The blockchain serves as the source of truth for *who* performed an action on the platform, and *when* that action took place. It also records and implements the token transfers that are connected to these actions. The blockchain therefore ensures that all parties can trust that their activity on the platform will be properly recognized and fulfilled.

## Distributed Database
The [database](storage.md) records *what* information is stored on the platform. Its contents are connected to transactions on the blockchain via identifying hashes. Because the database is implemented on the ipfs protocol, it ensures that a hash address contained in a verified transaction will point to data that cannot be altered. That data can then be relied upon to the extent that the transactions that refer to it indicate its trustworthiness (or lack thereof). The database only guarantees data integrity - i.e., that it has not been tampered with; its quality and confidence-worthiness are a function of various on-chain attestations.

## Backend Service
The backend service does not bear any responsibility for securing the platform; bugs or other problems with this code should not create vulnerabilities for the platform as a whole. Alternative implementations, while probably unnecessary, can certainly be created as needed in order to work with different hosting environments. De facto centralization is also not a concern at this level, as long as the blockchain and database themselves remain properly decentralized.

The most important aspect of the backend for most users is its public API. While the underlying blockchain and database state can be accessed by any client software that follows the proper protocols, the backend exposes ergonomic and well-documented endpoints that implement all of the typical operations performed on the platform. Every operation that requires the backend to interact with the blockchain will require that the calling account have sufficient GEODE tokens in its account balance.

## Identity and Authorization
As in other blockchain systems, identities are connected to specific public / private keypairs. Creating a new identity is as simple as creating a new keypair, and an account will remain secure and under control of its creator as long as they are the only one with access to the private key. Losing a private key means irrevocable loss of the token balance and other values associated with it. Theft of a private key gives the thief access to that account's assets and attributes, also irrevocably.
