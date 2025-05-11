# New Engineering Contract (NEC) -> NEC3, NEC4
# Options -> A, B, C, D, E
# The Engineering and Construction Contract (ECC)
# The Engineering and Construction Short Contract (ECSC)
# The Professional Services Contract (PSC)
# The Professional Services Short Contract (PSSC)
# https://scape.co.uk/news/nec-contracts
# https://www.neccontract.com/products/contracts/nec4/framework-contract
# Option G = NEC3 only
# NEC4 Framework Contract
# NEC4 Alliance Contract (ALC)
# NEC4 Design Build and Operate Contract (DBOC) 
# The NEC4 Professional Service Contract (PSC), Subcontract (PSS), and Short Contract (PSSC)
# NEC4 Term Service Contract (TSC) suite, 
# NEC4 Facilities Management Contract (FMC), the NEC4 Facilities Management Short Contract (FMSC), and related subcontracts.
# NEC4 Supply Contract (SC).
# NEC4 Supply Short Contract (SSC) 
# The main works contracts are the NEC4 Engineering and Construction Contract (ECC), the NEC4 Engineering and Construction Short Contract (ECSC), and their related subcontract forms.
# NEC3 Adjudicator's Contract replaced by NEC4 Dispute Resolution Service Contract
# 

# https://www.designingbuildings.co.uk/wiki/Construction_contract

from enum import Enum
from dataclasses import dataclass


@dataclass
class IssuingBody:
    name: str
    code: str
    full: str


class Issuer(Enum):
    NEC = IssuingBody(
        name="New Engineering Contract", 
        code="NEC", 
        full="New Engineering Contract (NEC)",
        )
    JCT = IssuingBody(
        name="The Joint Contracts Tribunal", 
        code="JCT", 
        full="The Joint Contracts Tribunal (JCT)",
        )
    ACA = IssuingBody(
        name="Association of Consultant Architects", 
        code="ACA", 
        full="Association of Consultant Architects (ACA)",
        )
    CIOB = IssuingBody(
        name="Chartered Institute of Building", 
        code="CIOB", 
        full="Chartered Institute of Building (CIOB)",
        )
    FIDIC = IssuingBody(
        name="Fédération Internationale des Ingénieurs-Conseils", 
        code="FIDIC", 
        full="Fédération Internationale des Ingénieurs-Conseils (FIDIC)",
        )

@dataclass
class IssuerVersion:
    name: str
    Issuer: Issuer
    version: int


class IssuedVersion(Enum):
    NEC3 = IssuerVersion(name="NEC3", Issuer=Issuer.NEC, version=3)
    NEC4 = IssuerVersion(name="NEC4", Issuer=Issuer.NEC, version=4)


@dataclass
class NECContractOption:
    name: str
    code: str
    full: str
    description: str


class ContractOptions(Enum):
    NECA = NECContractOption(
        name="Option A", 
        code="A", 
        full="NEC Option A: Priced contract with activity schedule",
        description="Priced contract with activity schedule",
        )
    NECB = NECContractOption(
        name="Option B", 
        code="B", 
        full="NEC Option B: Priced contract with bill of quantities",
        description="Priced contract with bill of quantities",
        )
    NECC = NECContractOption(
        name="Option C", 
        code="C", 
        full="NEC Option C: Target contract with activity schedule",
        description="Target contract with activity schedule",
        )
    NECD = NECContractOption(
        name="Option D", 
        code="D", 
        full="NEC Option D: Target contract with bill of quantities",
        description="Target contract with bill of quantities",
        )
    NECE = NECContractOption(
        name="Option E", 
        code="E", 
        full="NEC Option E: Cost reimbursable contract",
        description="Cost reimbursable contract",
        )
    NECF = NECContractOption(
        name="Option F", 
        code="F", 
        full="NEC Option F: Management contract",
        description="Management contract",
        )
    NECG = NECContractOption(
        name="Option G", 
        code="G", 
        full="NEC Option G: Term contract (NEC3)",
        description="Term contract (NEC3)",
        )


 # NEC (The New Engineering Contract): Engineering and Construction Contract)

 #    NEC4: Alliance Contract
 #    NEC4: Design Build and Operate Contract
 #    NEC4: Dispute Resolution Service Contract
 #    NEC4: Engineering and Construction Contract
 #    NEC4: Engineering and Construction Short Contract
 #    NEC4: Engineering and Construction Short Subcontract
 #    NEC4: Facilities Management Contract
 #    NEC4: Facilities Management Short Contract
 #    NEC4: Facilities Management Short Subcontract
 #    NEC4: Facilities Management Subcontract
 #    NEC4: Framework Contract
 #    NEC4: Professional Service Contract
 #    NEC4: Professional Service Short Contract
 #    NEC4: Professional Service Subcontract
 #    NEC4: Supply Contract
 #    NEC4: Supply Short Contract
 #    NEC4: Term Service Contract
 #    NEC4: Term Service Short Contract
 #    NEC4: Term Service Subcontract 

# https://www.designingbuildings.co.uk/wiki/NEC3
# https://www.autodesk.com/blogs/construction/construction-contracts-types/
# https://c-link.com/blog/a-guide-to-construction-contracts-in-the-uk/
# https://www.procore.com/library/construction-contract-types
# https://www.travisperkins.co.uk/content/types-of-constructions-contracts
# https://www.designingbuildings.co.uk/wiki/NEC_Option_A:_Priced_contract_with_activity_schedule
# https://www.designingbuildings.co.uk/wiki/NEC_Option_B:_Priced_contract_with_bill_of_quantities
# https://www.designingbuildings.co.uk/wiki/NEC_Option_C:_Target_contract_with_activity_schedule
# https://www.designingbuildings.co.uk/wiki/NEC_Option_D:_Target_contract_with_bill_of_quantities
# https://www.designingbuildings.co.uk/wiki/NEC_Option_E:_Cost_reimbursable_contract
# https://www.designingbuildings.co.uk/wiki/NEC_Option_F:_Management_contract
# 


