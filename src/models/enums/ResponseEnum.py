from enum import Enum

class ResponseSignal(Enum):
    FILE_IS_VALIDATED_SUCCESSFULLY = "file is validated successfully"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDS_LIMIT = "file size exceeds limit"
    FILE_UPLOAD_FAILED = "file upload failed"
    FILE_IS_VALID = "file is valid"
    FILE_UPLOAD_SUCCESSFUL = "file upload successful"