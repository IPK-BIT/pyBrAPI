from pydantic import BaseModel
from pybrapi.models.subclasses import Contact, DataLink, DatasetAuthorship, EnvironmentalParameter, ExperimentalDesign, ExternalReference, GrowthFacility, LastUpdate, ObservationUnitHierarchyLevel, Publication

class Trial(BaseModel):
    active: bool|None = None
    additionalInfo: dict|None = None
    commonCropName: str|None = None
    contacts: list[Contact]|None = None
    datasetAuthorships: list[DatasetAuthorship]|None = None
    documentationURL: str|None = None
    endDate: str|None = None
    externalReferences: list[ExternalReference]|None = None
    programDbId: str|None = None
    programName: str|None = None
    publications: list[Publication]|None = None
    startDate: str|None = None
    trialDbId: str
    trialDescription: str|None = None
    trialName: str
    trialPUI: str|None = None

class Study(BaseModel):
    active: bool|None = None
    additionalInfo: dict|None = None
    commonCropName: str|None = None
    contacts: list[Contact]|None = None
    culturalPractices: str|None = None
    dataLinks: list[DataLink]|None = None
    documentationURL: str|None = None
    endDate: str|None = None
    environmentParameters: list[EnvironmentalParameter]|None = None
    experimentalDesign: ExperimentalDesign|None = None
    externalReferences: list[ExternalReference]|None = None
    growthFacility: GrowthFacility|None = None
    lastUpdate: LastUpdate|None = None
    license: str|None = None
    locationDbId: str|None = None
    locationName: str|None = None
    observationLevels: list[ObservationUnitHierarchyLevel]|None = None
    observationUnitsDescription: str|None = None
    observationVariableDbIds: list[str]|None = None
    seasons: list[str]|None = None
    startDate: str|None = None
    studyCode: str|None = None
    studyDbId: str
    studyDescription: str|None = None
    studyName: str
    studyPUI: str|None = None
    studyType: str|None = None
    trialDbId: str|None = None
    trialName: str|None = None