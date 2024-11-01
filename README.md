# HotelArthur - Rengøringsservice
Denne rengøringsservice er en del af HotelArthur's bookingsystem, og håndterer opgaver relateret til rengøring af hotelværelser. Servicen integrerer med Booking API’et for at hente bookinger og opdatere rengøringsstatussen på værelser efter behov.

## Funktioner
Fetch Bookings: Henter alle bookede værelser, der kræver rengøring, fra Booking microservicen og viser oplysninger som booking-ID, værelsesnummer, check-in og check-out.

Mark Booking as Done: Giver brugeren mulighed for at markere værelser som rengjorte. Sender en opdatering til Booking API’et for at angive, at rengøringen er udført.

## Kom i gang
**Krav**
- Python 3.x installeret
- requests biblioteket installeret (kan installeres via pip install requests)
- Installation og Opsætning
- Klon repositoriet
- Installer nødvendige afhængigheder
- Kør Rengøringsservicen:

Rengøringsservicen interagerer med følgende endpoints i Booking microservicen:

GET /bookings
Henter alle bookinger og viser værelser, der kræver rengøring.

PUT /bookings/{booking_id}/mark_done
Markerer et specifikt værelse som rengjort ved at opdatere bookingens status.