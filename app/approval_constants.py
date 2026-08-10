from enum import Enum

class ApprovalStatus(str,Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class RequestType(str,Enum):
    CREATE_PRODUCT = "CREATE_PRODUCT"
    APPROVE_PRODUCT = "APPROVE_PRODUCT"
    REJECT_PRODUCT = "REJECT_PRODUCT"
