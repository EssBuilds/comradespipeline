from django.shortcuts import render, get_object_or_404, redirect
from .models import Scenario, Suspect, Weapon, Room


def start_game(request):
    # Get a random scenario
    scenario = Scenario.get_random_scenario()

    if not scenario:
        return render(
            request, 'error.html',
            {'message':
                 'No scenarios found. Please add some in the admin panel.'})

    # Store scenario ID in session so the user plays the same one
    request.session['scenario_id'] = scenario.id

    return render(request, 'start.html', {'scenario': scenario})


def make_accusation(request):
    scenario_id = request.session.get('scenario_id')
      # If no scenario in session, redirect to start game
    if not scenario_id:
        return redirect('start_game')
    
    scenario = get_object_or_404(Scenario, id=scenario_id)

    if request.method == "POST":
        suspect_id = request.POST.get("suspect")
        weapon_id = request.POST.get("weapon")
        room_id = request.POST.get("room")

        if (
                int(suspect_id) == scenario.correct_suspect.id and
                int(weapon_id) == scenario.correct_weapon.id and
                int(room_id) == scenario.correct_room.id
        ):
            return render(request, 'win.html', {"message":
                                                    "You solved the mystery!"})
        else:
            return render(request, 'lose.html', {"message":
                                                     "Wrong guess! Try again."})

    suspects = Suspect.objects.all()
    weapons = Weapon.objects.all()
    rooms = Room.objects.all()

    return render(request, 'accuse.html', {
        "scenario": scenario,
        "suspects": suspects,
        "weapons": weapons,
        "rooms": rooms
    })


def lose(request):
    context = {'message': 'You have lost the game!'}
    return render(request, 'lose.html', context)
