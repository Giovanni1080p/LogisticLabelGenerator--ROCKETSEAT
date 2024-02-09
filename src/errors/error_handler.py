from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_umprocessable_entity import HttpUmprocessableEntityError
def handler_errors(error:Exception)-> HttpResponse:
    if isinstance(error,HttpUmprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                'errors':[{
                'title':error.name,
                "detail":error.message}]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            'errors':[{
                'title':'server error',
                "detail": str(error)
            }]
        }
    )