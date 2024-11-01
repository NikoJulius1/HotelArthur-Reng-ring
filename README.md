# HotelArthur-Reng-ring

Dette projekt er en del af et bookingsystem, der håndterer rengøring af hotelværelser. Rengøring microservicen har følgende funktioner:

- Henter en liste over alle bookede værelser, der kræver rengøring.
- Giver brugeren mulighed for at markere værelser som rengjorte.

Funktionalitet
- Fetch Bookings: Henter alle bookinger fra Booking microservicen og viser værelser, der kræver rengøring.
- Mark Booking as Done: Opdaterer en bookings rengøringsstatus ved hjælp af en PUT-anmodning til Booking microservicen.

For at anvende denne microservice skal du:
- Klone dette repo
- Sørge for at have insalleret requests
- Kør microservicen

