The Geodess [platform](architecture.md) stores observations and other primary data in a distributed database called OrbitDB, which is itself a fairly thin layer on top of the IPFS storage layer. IPFS is distinguished by the fact that data is immutable - once a write is performed, the hash address that points to it will always reference the same bits that were written. The same "virtual" address can receive subsequent updates, but previous versions are always maintained and can be accessed at any time.

This combination - immutability combined with the ability to provide updates that supersede previous values - is perfect for our use case. We want to support successive observations of the same entity, while guaranteeing that past observations remain undisturbed. This, in turn, means that each observation can be the target of its own attestations; some observations of a given entity can therefore be more trustworthy than others, and this trustworthiness can be traded off with recency as desired by the user.

## Data Model

Distributed databases work differently than their centralized counterparts because sharding, rather than being a performance and scaling issue, is instead a central concern. 

Query dimensions

Region: All observations that are available for a particular area, across all observable types
History: All observations made about the same observable

Get regions for location

get_region(long, lat) -> geocode
get_observables(geocode, type?) -> List(obs_id)
get_observable(obs_id) -> doc
get_observations(obs_id, limit) -> List(meas_id)
