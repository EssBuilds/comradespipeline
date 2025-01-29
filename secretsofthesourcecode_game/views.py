from django.shortcuts import render, get_object_or_404
from .models import GameSession, Suspect, Weapon, Room

def start_game(request):
    # If there's an active game, continue it, otherwise create a new one
    game = GameSession.objects.filter(is_active=True).first()
    if not game:
        game = GameSession.create_new_game()

    return render(request, 'start.html', {'game': game})

def make_accusation(request):
    if request.method == "POST":
        game = GameSession.objects.filter(is_active=True).first()
        suspect_id = request.POST.get("suspect")
        weapon_id = request.POST.get("weapon")
        room_id = request.POST.get("room")

        suspect = get_object_or_404(Suspect, id=suspect_id)
        weapon = get_object_or_404(Weapon, id=weapon_id)
        room = get_object_or_404(Room, id=room_id)

        if (
                suspect == game.secret_suspect and
                weapon == game.secret_weapon and
                room == game.secret_room
        ):
            game.is_active = False
            game.save()
            return render(request, 'win.html', {"message": "You solved the mystery!"})
        else:
            return render(request, 'lose.html', {"message": "Wrong accusation! Try again."})

    suspects = Suspect.objects.all()
    weapons = Weapon.objects.all()
    rooms = Room.objects.all()
    return render(request, 'accuse.html', {"suspects": suspects, "weapons": weapons, "rooms": rooms})
