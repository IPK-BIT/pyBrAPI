from pydantic import BaseModel
    
class Contact(BaseModel):
    contactDbId: str
    email: str|None = None
    instituteName: str|None = None
    name: str|None = None
    orcid: str|None = None
    type: str|None = None

class DataLink(BaseModel):
    dataFormat: str|None = None
    description: str|None = None
    fileFormat: str|None = None
    name: str|None = None
    provenance: str|None = None
    scientificType: str|None = None
    url: str|None = None
    version: str|None = None

class DatasetAuthorship(BaseModel):
    datasetPUI: str|None = None
    license: str|None = None
    publicReleaseDate: str|None = None
    submissionDate: str|None = None

class DocumentationLink(BaseModel):
    URL: str|None = None
    type: str|None = None

class EnvironmentalParameter(BaseModel):
    description: str
    parameterName: str
    parameterPUI: str|None = None
    unit: str|None = None
    unitPUI: str|None = None
    value: str|None = None
    valuePUI: str|None = None
    
class ExperimentalDesign(BaseModel):
    PUI: str|None = None
    description: str|None = None

class ExternalReference(BaseModel):
    externalReferenceID: str
    externalReferenceSource: str
    externalReferenceURL: str|None = None
    
class GeoJSONGeometry(BaseModel):
    coordinates: list[int]|None = None
    type: str|None = None
    
class GeoJSON(BaseModel):
    geometry: GeoJSONGeometry|None = None
    type: str|None = None

class GrowthFacility(BaseModel):
    PUI: str|None = None
    description: str|None = None
    
class LastUpdate(BaseModel):
    timestamp: str|None = None
    version: str|None = None

class ObservationUnitHierarchyLevel(BaseModel):
    levelName: str|None = None
    levelOrder: int|None = None

class ObservationUnitLevel(BaseModel):
    levelCode: str|None = None
    levelName: str|None = None
    levelOrder: int|None = None

class ObservationUnitLevelRelationship(ObservationUnitLevel):
    observationUnitDbId: str|None = None

class OntologyReference(BaseModel):
    documentationLinks: list[DocumentationLink]|None = None
    ontologyDbId: str
    ontologyName: str
    version: str|None = None

class Position(BaseModel):
    entryType: str|None = None
    geoCoordinates: GeoJSON|None = None
    observationLevel: ObservationUnitLevel|None = None
    observationLevelRelationships: list[ObservationUnitLevelRelationship]|None = None
    positionCoordinateX: str|None = None
    positionCoordinateXType: str|None = None
    positionCoordinateY: str|None = None
    positionCoordinateYType: str|None = None

class Publication(BaseModel):
    publicationPUI: str|None = None
    publicationReference: str|None = None    
    
class Season(BaseModel):
    seasonDbId: str
    seasonName: str|None = None
    year: int|None = None

class Treatment(BaseModel):
    factor: str|None = None
    modality: str|None = None

class ValidValue(BaseModel):
    label: str|None = None
    value: str|None = None

class ValidValues(BaseModel):
    categories: list[ValidValue]|None = None
    maximumValue: str|None = None
    minimumValue: str|None = None

class Donor(BaseModel):
    donorACcessionNumber: str|None = None
    donorInstituteCode: str|None = None
    
class GermplasmOrigin(BaseModel):
    coordinateUncertainty: str|None = None
    coordinateUncertainty: GeoJSON|None = None
    
class StorageType(BaseModel):
    code: str|None = None
    description: str|None = None

class Synonym(BaseModel):
    synonym: str|None = None
    type: str|None = None
    
class TaxonId(BaseModel):
    sourceName: str
    taxonId: str