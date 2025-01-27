from app.shared.data_store import pending_tickets_store
from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from app.services.print_service import generate_ticket_text

router = APIRouter()

@router.get("/get_ticket", response_class=PlainTextResponse)
async def get_ticket():
    """
    Endpoint para que la ESP32 obtenga tickets pendientes.

    Returns:
        PlainTextResponse: Texto formateado del ticket.
    """
    if not pending_tickets_store.has_tickets():
        raise HTTPException(status_code=404, detail="No hay tickets pendientes.")

    # Obtener el primer ticket pendiente
    ticket_data = pending_tickets_store.get_next_ticket()
    
    # Generar el texto del ticket
    ticket_text = generate_ticket_text(ticket_data)
    
    # Devolver el texto del ticket
    return ticket_text
