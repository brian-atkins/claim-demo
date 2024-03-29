"""
Defines the resources that comprise the claim-processor domain.
"""
from . import _settings
from ._common import OBJECT_ID_REGEX
from . import people
from . import claims


DOMAIN_DEFINITIONS = {
    '_settings': _settings.DEFINITION,
    'people': people.DEFINITION,
    'claims': claims.DEFINITION
    
    
    
    
    
    
    
}


DOMAIN_RELATIONS = {
}


DOMAIN = {**DOMAIN_DEFINITIONS, **DOMAIN_RELATIONS}
