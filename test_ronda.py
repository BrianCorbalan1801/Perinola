import pytest
from Ronda import Ronda , Jugador


def test_agregar_jugador():
   ronda = Ronda()
   jugador = Jugador("Tomás", 5)
   ronda.agregarJugador(jugador)
   assert len(ronda.jugadores) == 1
   assert ronda.jugadores[0].nombre == "Tomás"


def test_agregar_jugador_sin_fichas():
   ronda = Ronda()
   jugador_sin_fichas = Jugador("Ana", 0)
   with pytest.raises(ValueError):
       ronda.agregarJugador(jugador_sin_fichas)


def test_sacar_jugadores_sin_fichas():
   ronda = Ronda()
   jugador1 = Jugador("Tomás", 5)
   jugador2 = Jugador("Ana", 0)
   ronda.agregarJugador(jugador1)
   ronda.agregarJugador(jugador2)


   ronda.sacarJugadoresSinFichas()
   assert len(ronda.jugadores) >= 1
   assert (ronda.jugadores[0] == "Tomás" ,5)


