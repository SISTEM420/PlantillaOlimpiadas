"""Módulo que detecta el input del usuario."""

import pygame


class EventHandler:
    def __init__():
        EventHandler.events = pygame.event.get()

    def poll_events():
        """Recibe los eventos de input."""

        EventHandler.events = pygame.event.get()

    def keydown(key) -> bool:  # TODO definir tipo de parámetro key
        """Detecta input del teclado."""

        for event in EventHandler.events:
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    def clicked(leftright=1) -> bool:  # 1 - click izquierdo, 3 - click derecho
        """Discrimina el click del mouse."""

        for event in EventHandler.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == leftright:  # Click izquierdo
                    return True

    def clicked_any() -> bool:
        """Detecta input del mouse."""

        for event in EventHandler.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False
