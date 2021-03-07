from typing import Optional, List, Dict, Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response


class AttestationTypes(str, Enum):
    SUPPORT = "support"
    DISAGREE = "disagree"
    REFUTE = "refute"
    RETRACT = "retract"


class Auth(BaseModel):
    public_key: str
    signature: str
    digest: str


class BasicResponse(BaseModel):
    message: str
    handle: str


class AccountData(BaseModel):
    public_key: str
    algorithm: str
    name: Optional[str] = None


class Account(BaseModel):
    data: AccountData
    auth: Auth


class AttestationData(BaseModel):
    observation_id: str
    attestation_type: AttestationTypes
    timestamp: str
    attestation_public_key: str


class Attestation(BaseModel):
    data: AttestationData
    auth: Auth


class ObservationData(BaseModel):
    entity_id: str
    timestamp: str
    public_key: str


class Observation(BaseModel):
    data: ObservationData
    auth: Auth
    self_attest: bool = False


class AttestedObservation(Observation):
    attestations: List[AttestationData]


class ObservationFilter(BaseModel):
    pass


app = FastAPI()


@app.get("/")
async def root():
    pass


# Identity


@app.post("/accounts")
def create_account(account: Account):
    pass


@app.get("/accounts/me")
def get_account():
    pass


# Individual observations and attestations


@app.post("/observations", response_model=BasicResponse, status_code=200)
def create_observation(observation: Observation):
    pass


@app.get("/observations/{observation_id}", response_model=AttestedObservation)
def get_observation(observation_id: str):
    """
    Fetch an observation with a specific ID.
    """
    pass


@app.post("/observations/{observation_id}/attestations", response_model=BasicResponse)
def create_attestation(attestation: Attestation):
    """
    Submit an attestation about an observation.
    """
    pass


# Querying


@app.get("/observations/geo/{geohash}/count")
def count_observations_by_geo(geohash: str, filter: Optional[ObservationFilter]):
    """
    Count the observations within a given geo area that meet the filter, if any,
    passed in via the request body.
    """
    pass


@app.get("/observations/geo/{geohash}")
def get_observations_by_geo(geohash: str, filter: Optional[ObservationFilter]):
    """
    Query for observations within a given geohash area that meet the filter, if any,
    passed in via the request body.
    """
    pass

